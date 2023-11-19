from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    # list_filter = ('transaction_date',)
    # empty_value_display = '-empty-'
    # search_fields = ('amount', 'category', 'user', 'transaction_date')
