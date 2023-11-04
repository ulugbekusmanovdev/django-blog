from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:category_id>/', views.category, name='category'),
    path('blogs/<slug:slug>/', views.blogs, name='blogs'),
    path('blogs/search', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
]