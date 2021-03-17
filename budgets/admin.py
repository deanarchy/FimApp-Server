from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import Group

from .models import User, Category, Budget
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
class BudgetInline(admin.StackedInline):
    model = Budget
    can_delete = False
    verbose_name_plural = 'Budgets'
    
    
class UserAdmin(UA):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        (None, {
           'classes': ('wide', ),
           'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),              
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

class BudgetAdmin(admin.ModelAdmin):
   list_display = ('user', 'free_amount', 'dob')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'budget')

admin.site.register(User, UserAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.unregister(Group)
