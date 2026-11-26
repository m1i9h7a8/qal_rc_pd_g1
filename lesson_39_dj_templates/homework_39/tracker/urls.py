from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions, name='transactions'),
    path('transactions/<int:trans_id>/', views.transaction_detail, name='transaction-detail'),
    path('transactions/add/', views.placeholder, name='add-transaction'),
    path('transactions/<int:trans_id>/edit/', views.placeholder, name='edit-transaction'),
    path('transactions/<int:trans_id>/delete/', views.placeholder, name='delete-transaction'),
    path('budgets/', views.budgets, name='budgets'),
    path('budgets/add/', views.placeholder, name='add-budget'),
    path('budgets/<int:budget_id>/edit/', views.placeholder, name='edit-budget'),
    path('budgets/<int:budget_id>/delete/', views.placeholder, name='delete-budget'),
    path('reports/', views.reports, name='reports'),
    path('about/', views.about, name='about'),
]
