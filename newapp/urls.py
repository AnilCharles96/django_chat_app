from django.urls import path, include
from django.views.generic import TemplateView
from newapp import views
from django.contrib.auth import views as auth_views


app_name = 'newapp'

urlpatterns = [
    path('register/',views.RegisterView,name='register'),
    path('',views.HomeView,name='home'),
    path('login/',views.LoginView,name="login"),
    path('accounts/logout/',auth_views.LogoutView.as_view(),{'next_page':'/'},name='auth_logout'),
    path('snippet/',views.snippet)
    
    
]
