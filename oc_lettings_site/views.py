from django.shortcuts import render


# Add documentation here
def index(request):
    return render(request, 'index.html')
