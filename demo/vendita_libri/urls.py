from django.urls import path
from . import views

urlpatterns = [
    path('libri/', views.LibroListView.as_view(), name='libro-list'),
    path('libri/ordinati/', views.LibroOrderView.as_view(), name='libro-ordinati'),
]
