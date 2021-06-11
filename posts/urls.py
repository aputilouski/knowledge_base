from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_slug>/', views.category_list, name='category_list'),
    path('<str:category_slug>/<str:post_slug>/', views.post, name='post'),
]