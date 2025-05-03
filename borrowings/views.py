from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from books.models import Book
from borrowings.models import Borrowing
from django.http import JsonResponse

class BorrowBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user

        if Borrowing.objects.filter(borrower=user, book=book, end_date__gte=timezone.now()).exists():
            messages.error(request, "You have already borrowed this book.")
            return redirect('book_detail', pk=pk)
        
        if Borrowing.objects.filter(borrower=user, end_date__gte=timezone.now()).count() >= 5:
            messages.error(request, "You have reached your borrowing limit.")
            return redirect('book_detail', pk=pk)

        if book.stock <= 0:
            messages.error(request, "Book not available.")
            return redirect('book_detail', pk=pk)

        Borrowing.objects.create(borrower=user, book=book)
        messages.success(request, f"You borrowed '{book.title}' successfully!")
        return redirect('book_detail', pk=pk)
    
class ReturnBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk, borrower=request.user)
        borrowing.book.stock += 1
        borrowing.book.save()
        borrowing.delete()
        
        messages.success(request, f"You have successfully returned '{borrowing.book.title}'.")
        
        # Check if it's an AJAX request
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'success',
                'message': f"You have successfully returned '{borrowing.book.title}'."
            })
            
        return redirect(reverse_lazy('dashboard'))