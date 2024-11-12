from django.shortcuts import render

def index(request):
    return render(request, 'rest/index.html')
