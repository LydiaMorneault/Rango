from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm

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

# This is one view called index
# Each view takes in an HttpRequest parameter
# All views return an HttpResponse object, which takes in a string which will be displayed

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

def add_category(request):
    form = CategoryForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)   #Redirects to index page

    else:
        print(form.errors)

    # Renders form with every type of error msg or w/e, displays errors
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page=form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category':category}
    return render(request, 'rango/add_page.html', context_dict)

def register(request):
    # a boolean value for telling the template whether the registration was successful
    # True when registration succeeds
    registered = False

    # if it's an HTTP POST we're interested in it
    if request.method == 'POST':
        #gets info from raw form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # if they're both valid
        if user_form.is_valid() and profile_form.is_valid():
            #save data to database
            user = user_form.save()

            #hash password with set password and update
            user.set_password(user.password)
            user.save()

            #commit=False because we'll set it ourselves
            profile = profile_form.save(commit=False)
            profile.user = user

            #does user have a profile pic?
            if 'picture' in request.FILES:
                #get it from input form
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True

            else: #Not an HTTP POST
                user_form = UserForm()
                profile_form = UserProfileForm()

        return render(request, 'rango/register.html', {'user_form':user_form,'profile_form':profile_form, 'registered': registered})







