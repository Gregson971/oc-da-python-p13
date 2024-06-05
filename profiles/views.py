from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    View that displays a list of profiles

    args:
        request: HttpRequest object

    returns:
        HttpResponse object, displaying a list of profiles
    """

    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View that displays a profile

    args:
        request: HttpRequest object
        username: str, username of the profile to display

    returns:
        HttpResponse object, displaying a profile
    """

    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
