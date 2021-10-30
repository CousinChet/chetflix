from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


# Admin users panel listing users

class AccountAdmin(UserAdmin):
    list_display = (
        'username',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
        'is_admin',
        'see_pg13',
        'see_r',
        'r_edit',
        'email',
        'date_joined',
        )

    search_fields = ('username', 'email')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
