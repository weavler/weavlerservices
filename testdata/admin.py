from django.contrib import admin

# Register your models here.

from .models import DemoProduct

admin.site.register(DemoProduct)
