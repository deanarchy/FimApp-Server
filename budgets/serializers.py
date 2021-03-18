from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Budget, Category


class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = get_user_model()
        fields = ['email']


class BudgetSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category')
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Budget
        fields = ['user', 'first_name', 'last_name', 'free_amount', 'dob', 'categories']
        

class CategorySerializer(serializers.ModelSerializer):
    budget = serializers.ReadOnlyField(source='budget.user.email')
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'amount', 'budget']
