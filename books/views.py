from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from borrowings.models import Borrowing
from django.utils import timezone


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'



class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        book = self.get_object()
        context['is_available'] = book.is_available()
        context['can_borrow'] = book.is_available() and Borrowing.objects.filter(
            borrower=user, end_date__gte=timezone.now()).count() < 5
        context['borrow_limit_reached'] = Borrowing.objects.filter(
            borrower=user, end_date__gte=timezone.now()).count() >= 5
        context['already_borrowed'] = Borrowing.objects.filter(borrower=user, book=book, end_date__gte=timezone.now()).exists()
        return context



class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publish_date', 'category']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publish_date', 'category']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')