from django.shortcuts import render


def index(request):
    """
    View that displays the home page

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying the home page
    """

    return render(request, 'index.html')
