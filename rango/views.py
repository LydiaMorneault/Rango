from django.http import HttpResponse

# This is one view called index
# Each view takes in an HttpRequest parameter
# All views return an HttpResponse object, which takes in a string which will be displayed
def index(request):
    return HttpResponse("Rango says hey there partner!")