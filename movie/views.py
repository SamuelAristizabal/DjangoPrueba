from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'Greg Lim'})
def about(request):
    return HttpResponse('<h1>About who?</h1>')