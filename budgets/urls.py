from django.urls import path

from .views import (
    ListBudgetView, DetailBudgetView,
    ListUserView, DetailUserView,
    ListCategoriesView, DetailCategoriesView
)

urlpatterns = [
    path('budget/', ListBudgetView.as_view(), name='budget-list'),
    path('budget/<str:pk>/', DetailBudgetView.as_view(), name='budget'),
    path('category/', ListCategoriesView.as_view(), name='category-list'),
    path('category/<int:pk>/', DetailCategoriesView.as_view(), name='category'),
    path('user/', ListUserView.as_view(), name='user-list'),
    path('user/<str:pk>/', DetailUserView.as_view(), name='user'),
]
