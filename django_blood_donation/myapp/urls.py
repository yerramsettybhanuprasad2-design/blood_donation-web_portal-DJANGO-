from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('find-donor/', views.find_donor, name='find_donor'),
    path('register/', views.register, name='register'),
    path('request-blood/', views.request_blood, name='request_blood'),
    path('view-requests/', views.view_blood_requests, name='view_blood_requests'),
    path('delete-request/<int:pk>/', views.delete_blood_request, name='delete_blood_request'),
    path('login/', auth_views.LoginView.as_view(template_name='view_requests.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='view_blood_requests'), name='logout'),

]

