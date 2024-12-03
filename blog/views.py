from django.shortcuts import render
from django.views.generic import ListView
from .models import Publication
# Create your views here.

class HomePageView(ListView):
    model = Publication
    template_name = 'publication_list.html'
    
