from django.shortcuts import render
from django.views.generic import DetailView, ListView
# Create your views here.

from .models import Book 

def main_page(request,*args,**kwargs):
    return render(request,template_name ="core/main.html")

class BookDetailView(DetailView):
    model = Book
class BookListView(ListView):
    model = Book

