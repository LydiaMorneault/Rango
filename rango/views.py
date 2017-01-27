from django.http import HttpResponse
from django.shortcuts import render

# This is one view called index
# Each view takes in an HttpRequest parameter
# All views return an HttpResponse object, which takes in a string which will be displayed
def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # The key boldmessage is the same as in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

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