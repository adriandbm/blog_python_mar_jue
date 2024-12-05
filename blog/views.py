from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Publication
# Create your views here.

class HomePageView(ListView):
    model = Publication
    template_name = 'publication_list.html'


class PublicationCreateView(CreateView):
    model = Publication
    template_name = 'publication_new.html'
    fields = ['title', 'author', 'body']
    
