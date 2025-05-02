from django.urls import path
from .views import BorrowBookView

urlpatterns = [
    path('borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow_book'),
]