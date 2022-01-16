from django.contrib import admin
from .models import User, Department
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
class UserAdminConfig(UserAdmin):
    ordering = ('lname',)
    list_display = ('id', 'lname', 'fname', 'email', 'department_id', 'is_active', 'staff', 'admin',)
    list_filter = ('department_id', 'staff', 'admin',)
    search_fields = ('lname', 'fname', 'email',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal Info'), {'fields': ('lname', 'fname',)}),
        (_('Permissions'), {'fields': ('is_active', 'staff', 'admin',)}),
        (_('Group'), {'fields': ('groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fname', 'lname', 'department', 'password1', 'password2'),
        }),
    )


admin.site.register(User, UserAdminConfig)
admin.site.register(Department)
