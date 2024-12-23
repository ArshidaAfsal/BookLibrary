from django.contrib import admin
from account.models import UserProfile,loginTable

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(loginTable)
