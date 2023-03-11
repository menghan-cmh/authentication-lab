from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from .models import Snippet

# Register your models here.
admin.site.register(Snippet)
TokenAdmin.raw_id_fields = ('user',)