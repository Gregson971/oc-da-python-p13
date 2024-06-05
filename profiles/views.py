import logging

from sentry_sdk import capture_exception
from django.shortcuts import render

from .models import Profile


logger = logging.getLogger(__name__)


def profiles_index(request):
    """
    View that displays a list of profiles

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying a list of profiles
    """

    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        capture_exception(e)
        logger.error(f"An error occurred: {e}")
        raise


def profile(request, username):
    """
    View that displays a profile

    args:
        request: HttpRequest object
        username: str, username of the profile to display

    returns:
        HttpResponse object, displaying a profile
    """

    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist as e:
        capture_exception(e)
        logger.error(f"Profile not found: {e}")
        raise
    except Exception as e:
        capture_exception(e)
        logger.error(f"An error occurred: {e}")
        raise
