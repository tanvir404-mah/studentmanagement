from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('result/', views.result, name='result'),
    path('routine/', views.routine, name='routin'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('contact/', views.contact, name='contact'),
    path('lab/', views.lab, name='lab'),
    path('club/', views.club, name='club'),
    path('developer/', views.developer, name='developer'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    ]