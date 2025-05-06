from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from borrowings.models import Borrowing
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages


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



class FreePreviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        # Assuming book.content is a list or string of pages
        preview_pages = book.get_pages(0, 10)  # Implement this in your model
        return render(request, 'books/preview.html', {
            'book': book,
            'pages': preview_pages,
        })


class ReadingView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user
        now = timezone.now()

        try:
            borrowing = Borrowing.objects.get(borrower=user, book=book, end_date__gte=now)
        except Borrowing.DoesNotExist:
            messages.error(request, "You haven't borrowed this book or your access expired.")
            return redirect('book_detail', pk=pk)

        start_page = 0
        end_page = borrowing.pages_borrowed

        book_pages = book.get_page_range(start_page, end_page)

        return render(request, 'books/reading.html', {
            'book': book,
            'pages': book_pages,
            'end_date': borrowing.end_date
        })


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