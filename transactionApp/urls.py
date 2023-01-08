from django.contrib import admin
from django.urls import path
from .views import transactionView, index, transactionSearchView

urlpatterns = [
    path('index', index, name='index'),
    path('', transactionView.as_view(), name='transactionView'),
    path('search', transactionSearchView.as_view(), name='transactionSearchView'),
]