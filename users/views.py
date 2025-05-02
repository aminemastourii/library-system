from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.db.models import Count
from django.contrib.auth.views import LoginView
from books.models import Book
from borrowings.models import Borrowing
from .models import User, BorrowerProfile
from .forms import BorrowerSignUpForm, CompleteProfileForm

class HomeView(TemplateView):
    template_name = 'users/home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # Get the sorting method from the query parameters
        sort_method = self.request.GET.get('sort', 'default')

        # Default sorting: by book title
        if sort_method == 'default':
            context['books'] = Book.objects.all().order_by('title')

        # Sorting by borrowing count
        elif sort_method == 'borrowed':
            context['books'] = (
                Book.objects.annotate(borrow_count=Count('borrowing'))
                .order_by('-borrow_count')
            )
        context['borrowings'] = Borrowing.objects.filter(borrower=self.request.user)

        context['top_borrowed_books'] = (
            Book.objects.annotate(borrow_count=Count('borrowing'))
            .order_by('-borrow_count')[:3]
        )
        context['current_sort'] = sort_method
       
        return context
    


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