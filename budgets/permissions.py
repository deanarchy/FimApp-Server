from rest_framework import permissions


class IsBudgetOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsCategoryOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.budget.user == request.user or request.user.is_staff


class CreateOnlyOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True

        return request.user.is_staff
