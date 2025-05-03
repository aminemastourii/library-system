from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.auth.views import LoginView
from books.models import Book
from borrowings.models import Borrowing
from .models import User, BorrowerProfile
from .forms import BorrowerSignUpForm, CompleteProfileForm
from django.http import HttpResponse
from django.template.loader import render_to_string

class HomeView(TemplateView):
    template_name = 'users/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        overdue_borrowings = Borrowing.objects.filter(end_date__lt=timezone.now())
        for borrowing in overdue_borrowings:
            borrowing.book.stock += 1  
            borrowing.book.save()
            borrowing.delete() 
        context = super().get_context_data(**kwargs)

        search_query = self.request.GET.get('search', '')
        books = Book.objects.all()
        if search_query:
            books = books.filter(
                Q(title__icontains=search_query) | Q(category__icontains=search_query)
            )
       
        sort_method = self.request.GET.get('sort', 'default')
        if sort_method == 'default':
            books = books.order_by('title')  
        elif sort_method == 'borrowed':
            books = books.annotate(borrow_count=Count('borrowing')).order_by('-borrow_count')
            
        context['books'] = books
        context['borrowings'] = Borrowing.objects.filter(borrower=self.request.user)
        context['top_borrowed_books'] = (
            Book.objects.annotate(borrow_count=Count('borrowing'))
            .order_by('-borrow_count')[:3]
        )
        context['current_sort'] = sort_method
        context['search_query'] = search_query
       
        return context
        
    def get(self, request, *args, **kwargs):
        # Check if this is an AJAX request
        if request.GET.get('ajax') == 'true':
            context = self.get_context_data(**kwargs)
            html = render_to_string(self.template_name, context, request=request)
            return HttpResponse(html)
        return super().get(request, *args, **kwargs)


class SignUpView(CreateView):
    model = User
    form_class = BorrowerSignUpForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
    
        login(self.request, user)  
        return redirect('complete_profile')


class CompleteProfileView(FormView):
    template_name = 'users/complete_profile.html'
    form_class = CompleteProfileForm
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('signup')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.is_borrower = True
        user.save()

        
        if not BorrowerProfile.objects.filter(user=user).exists():
            BorrowerProfile.objects.create(
                user=user,
                birthday=form.cleaned_data['birthday']
            )

        return super().form_valid(form)
    

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('dashboard')