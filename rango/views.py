from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

# This is one view called index
# Each view takes in an HttpRequest parameter
# All views return an HttpResponse object, which takes in a string which will be displayed
def index(request):
    # Query the database for a list of all categories stored
    # Order by number of likes in descending order
    # Retrieve the top 5 or if <5, all of them
    # Place list in context_dict which will be passed to template engine


    # Construct a dictionary to pass to the template engine as its context
    # The key boldmessage is the same as in the template
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context_dict)


def about(request):
    # Construct a dictionary to pass to the template engine as its context
    # The key boldmessage is the same as in the template
    context_dict = {'boldmessage': "Rango says here is the about page."}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use
    return render(request, 'rango/about.html', context=context_dict)