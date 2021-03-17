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
    permission_classes = [permissions.IsAdminUser]
    

class DetailUserView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class ListBudgetView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [CreateOnlyOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailBudgetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    permission_classes = [IsBudgetOwner]
    serializer_class = BudgetSerializer


class ListCategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CreateOnlyOrAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        budget = Budget.objects.get(pk=request.user.budget)
        budget.free_amount -= int(request.data.get('amount'))
        budget.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        serializer.save(budget=self.request.user.budget)

        
class DetailCategoriesView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCategoryOwner]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
