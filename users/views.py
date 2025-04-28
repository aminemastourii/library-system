from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .models import User, BorrowerProfile
from .forms import BorrowerSignUpForm, CompleteProfileForm


class BorrowerSignUpView(CreateView):
    model = User
    form_class = BorrowerSignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('complete-profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_borrower = True  # Mark user as borrower
        user.save()
        login(self.request, user)  # Log the user in directly after signup
        return super().form_valid(form)


class CompleteProfileView(LoginRequiredMixin, FormView):
    template_name = 'users/complete_profile.html'
    form_class = CompleteProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
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
        return reverse_lazy('home')