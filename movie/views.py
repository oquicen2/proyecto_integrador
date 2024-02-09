from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
#   return HttpResponse('<h1> Welcome to home page</h1>')
#   return render(request,'home.html')
#    return render(request,'home.html',{'name': 'Orleis Quiceno velasqeuz'})

    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie = Movie.objects.filter(title__contains=searchTerm)
    else:
        movie = Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm, 'movie':movie})


def About(request):
    return HttpResponse('<h1> Welcome to About page</h1</h1>')

