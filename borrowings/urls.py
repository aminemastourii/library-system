from django.urls import path
from .views import BorrowBookView, PaymentView, ReturnBookView

urlpatterns = [
    path('borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow_book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return_book'),
    path('payment/', PaymentView.as_view(), name='payment_page'),  # Payment page


]