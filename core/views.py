from django.shortcuts import render
from django.views.generic import DetailView, ListView

from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, TrigramSimilarity
from .models import Book 

def main_page(request,*args,**kwargs):
    return render(request,template_name ="core/main.html")

class BookDetailView(DetailView):
    model = Book
class BookListView(ListView):
    model = Book
    template_name = "core/book_search.html"

class BookSearchView(ListView):
    template_name = "core/book_search.html"
    def get_queryset(self):
        """if query not provided return all books"""
        search_vector =( SearchVector("title","author",weight="A") 
                + SearchVector("description", weight="B"))
        query = SearchQuery(self.request.GET.get('query'), search_type="websearch")
        #trigram_similarity =TrigramSimilarity('author', query)
        #return Book.objects.annotate(rank=SearchRank(search_vector,query)+trigram_similarity).filter(rank__gte=0.3).order_by('-rank')
        return Book.objects.annotate(rank=SearchRank(search_vector,query)).filter(rank__gte=0.1).order_by('-rank') 
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query_requested"] = self.request.GET.get('query')
        return context
     
