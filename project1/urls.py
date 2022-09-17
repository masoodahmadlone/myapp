from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('budget/', views.budget, name='budget'),
    path('latest/', views.latest, name='latest'),
    path('footer/', views.footer, name='footer'),
    path('navbar/', views.navbar, name='navbar'),
    path('portfolio/', views.portfolio, name='portfolio'),
   
] 