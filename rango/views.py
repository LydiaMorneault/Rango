from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime



# This is one view called index
# Each view takes in an HttpRequest parameter
# All views return an HttpResponse object, which takes in a string which will be displayed
def index(request):
    # Query the database for a list of all categories stored
    # Order by number of likes in descending order
    # Retrieve the top 5 or if <5, all of them
    # Place list in context_dict which will be passed to template engine

    page_list = Page.objects.order_by('-views')[:5]

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories' : category_list, 'pages': page_list}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # Construct a dictionary to pass to the template engine as its context
    # The key boldmessage is the same as in the template
    context_dict = {'boldmessage': "Rango says here is the about page."}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception
        # So the .get() method returns one model instance or raises an exception
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all the associated pages
        # filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        # will display the no category message for us
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)



