from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/emailsignup/',  views.RegisterUserView2.as_view(), name='register')
]