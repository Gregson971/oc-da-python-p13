from django.shortcuts import render
from .models import Profile


# Add documentation here
def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Add documentation here
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
