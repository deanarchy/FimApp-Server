from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import Budget, Category
from .serializers import UserSerializer, BudgetSerializer, CategorySerializer
from .permissions import IsBudgetOwner, IsCategoryOwner, CreateOnlyOrAdmin

# Create your views here.
class ListUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    

class DetailUserView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class ListBudgetView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated, CreateOnlyOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailBudgetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBudgetOwner]
    serializer_class = BudgetSerializer


class ListCategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, CreateOnlyOrAdmin]

    
    def perform_create(self, serializer):
        serializer.save(budget=self.request.user.budget)
        

class ListCategoriesViewbyUser(generics.ListAPIView):        
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsCategoryOwner]

    def get_queryset(self):
        queryset = Category.objects.all()
        queryset = queryset.filter(budget=self.kwargs.get('budget'))
        return queryset

        
class DetailCategoriesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCategoryOwner]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
