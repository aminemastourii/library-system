from django.urls import path
from .views import DashboardView, HomeView, SignUpView, CompleteProfileView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('complete_profile/', CompleteProfileView.as_view(), name='complete_profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
