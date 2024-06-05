import logging

from sentry_sdk import capture_exception
from django.shortcuts import render


logger = logging.getLogger(__name__)


def index(request):
    """
    View that displays the home page

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying the home page
    """

    try:
        return render(request, 'index.html')
    except Exception as e:
        capture_exception(e)
        logger.error(f"An error occurred: {e}")
        raise
