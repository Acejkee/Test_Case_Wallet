from django.contrib import admin
from .models import Wallet


@admin.register(Wallet)
class CustomMPTTModelAdmin(admin.ModelAdmin):
    pass