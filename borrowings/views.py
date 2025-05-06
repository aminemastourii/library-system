from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from books.models import Book
from borrowings.forms import BorrowForm
from borrowings.models import Borrowing
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BorrowForm
from books.models import Book
from borrowings.models import Borrowing  # if not already imported

class BorrowBookView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BorrowForm(total_pages=book.total_pages)
        return render(request, 'borrowings/book_detail.html', {'form': form, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        user = request.user

        # Business rule checks
        if Borrowing.objects.filter(borrower=user, book=book, end_date__gte=timezone.now()).exists():
            messages.error(request, "You have already borrowed this book.")
            return redirect('book_detail', pk=pk)

        if Borrowing.objects.filter(borrower=user, end_date__gte=timezone.now()).count() >= 5:
            messages.error(request, "You have reached your borrowing limit.")
            return redirect('book_detail', pk=pk)

        if book.stock <= 0:
            messages.error(request, "Book not available.")
            return redirect('book_detail', pk=pk)

        form = BorrowForm(request.POST,total_pages=book.total_pages)
        if form.is_valid():
            duration = int(form.cleaned_data['duration'])
            pages = form.cleaned_data['pages']

            # Store intent in session before payment
            request.session['borrow_intent'] = {
                'book_id': book.id,
                'duration': duration,
                'pages': pages
            }

            return redirect('payment_page')  # Replace with your actual payment URL name
        else:
            return render(request, 'borrowings/book_detail.html', {'form': form, 'book': book})


class PaymentView(View):
    def get(self, request):
        borrow_intent = request.session.get('borrow_intent')
        if not borrow_intent:
            messages.error(request, "No borrowing request found.")
            return redirect('dashboard')  # or some fallback

        book = get_object_or_404(Book, id=borrow_intent['book_id'])
        pages = int(borrow_intent['pages'])
        duration = int(borrow_intent['duration'])

        # Example pricing model: $0.10 per page per 7 days
        price_per_page_per_day = 0.01
        total_price = pages * duration * price_per_page_per_day

        return render(request, 'borrowings/payment.html', {
            'book': book,
            'pages': pages,
            'duration': duration,
            'total_price': round(total_price, 2)
        })

    def post(self, request):
        borrow_intent = request.session.get('borrow_intent')
        if not borrow_intent:
            messages.error(request, "No borrowing request found.")
            return redirect('dashboard')

        book = get_object_or_404(Book, id=borrow_intent['book_id'])
        user = request.user
        pages = int(borrow_intent['pages'])
        duration = int(borrow_intent['duration'])

        # Mock payment confirmation (replace with actual logic)
        payment_successful = True

        if payment_successful:
            start_date = timezone.now()
            end_date = start_date + timezone.timedelta(days=duration)

            borrowing = Borrowing.objects.create(
                borrower=user,
                book=book,
                start_date=start_date,  
                end_date=end_date,
                pages_borrowed=pages,
                is_paid=True
            )

            # Optional: Decrease stock
            
            book.save()

            # Clear session
            del request.session['borrow_intent']

            messages.success(request, "Payment successful. You can now read the book!")
            return redirect('reading_view', pk=book.id)
        else:
            messages.error(request, "Payment failed.")
            return redirect('payment_page')

    
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