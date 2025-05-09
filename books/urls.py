from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, FreePreviewView, ReadingView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('reading/<int:pk>/', ReadingView.as_view(), name='reading_view'),  # Reading view
    path('preview/<int:pk>/', FreePreviewView.as_view(), name='free_preview'),  # Free preview page

]
