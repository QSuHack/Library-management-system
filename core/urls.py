from django.urls import path
from core.views import main_page, BookDetailView, BookListView

urlpatterns = [
    path('', main_page, name="main-page"),
    path('book/<int:pk>', BookDetailView.as_view(), name="book-detail" ),
    path('catalogue/', BookListView.as_view(), name="book-catalogue" ),
]
