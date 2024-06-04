from django.urls import path

from . import views

# Namespace for the profiles app
app_name = 'profiles'

urlpatterns = [
    path('profiles/', views.profiles_index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
]
