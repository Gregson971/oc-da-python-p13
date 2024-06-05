from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    View that displays a list of lettings

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying a list of lettings
    """

    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    View that displays a letting

    args:
        request: HttpRequest object
        letting_id: int, id of the letting to display

    returns:
        HttpResponse object, displaying a letting
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
