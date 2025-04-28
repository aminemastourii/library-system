from django.urls import path
from .views import BorrowerSignUpView, CompleteProfileView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', BorrowerSignUpView.as_view(), name='signup'),
    path('complete-profile/', CompleteProfileView.as_view(), name='complete-profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
