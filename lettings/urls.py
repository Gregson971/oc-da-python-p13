from django.urls import path

from . import views


# Namespace for the lettings app
app_name = 'lettings'

urlpatterns = [
    path('lettings/', views.lettings_index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
