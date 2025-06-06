from django.contrib import admin
from .models import User, OneTimePasscode

class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number')
    list_editable = ('first_name', 'last_name', 'phone_number')

admin.site.register(User, AdminUser)
admin.site.register(OneTimePasscode)
# Register your models here.
