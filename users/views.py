from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
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
        context['books'] = Book.objects.all()
        context['borrowings'] = Borrowing.objects.filter(borrower=self.request.user)
        return context


class SignUpView(CreateView):
    model = User
    form_class = BorrowerSignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('complete_profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        self.request.session['temp_username'] = user.username 
        login(self.request, user)  
        return super().form_valid(form)


class CompleteProfileView( FormView):
    template_name = 'users/complete_profile.html'
    form_class = CompleteProfileForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        username = self.request.session.get('temp_username')
        if not username:
           return redirect('signup')  

        user = User.objects.get(username=username) 
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.is_borrower = True 
        user.save()
        birthday = form.cleaned_data['birthday']
        BorrowerProfile.objects.create(
                user=user,
                birthday=birthday,
                
            )
        return super().form_valid(form)
    

class CustomLoginView(LoginView):
    template_name='users/login.html'
    def get_success_url(self):
        return reverse_lazy('dashboard')