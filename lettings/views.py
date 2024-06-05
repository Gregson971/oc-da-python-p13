import logging

from sentry_sdk import capture_exception
from django.shortcuts import render

from .models import Letting


logger = logging.getLogger(__name__)


def lettings_index(request):
    """
    View that displays a list of lettings

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying a list of lettings
    """

    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        capture_exception(e)
        logger.error(f"An error occurred: {e}")
        raise


def letting(request, letting_id):
    """
    View that displays a letting

    args:
        request: HttpRequest object
        letting_id: int, id of the letting to display

    returns:
        HttpResponse object, displaying a letting
    """

    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist as e:
        capture_exception(e)
        logger.error(f"Letting not found: {e}")
        raise
    except Exception as e:
        capture_exception(e)
        logger.error(f"An error occurred: {e}")
        raise
