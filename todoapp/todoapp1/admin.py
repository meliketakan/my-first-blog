from django.contrib import admin
from .models import Formsayfasi

class ContactAdmin(admin.ModelAdmin):
    list_display=["name","surname","email"]
admin.site.register(Formsayfasi,ContactAdmin)