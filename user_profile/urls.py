from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.AuthorizationView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
]
