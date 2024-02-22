from django.contrib import admin
from .models import register, Feedback ,Admin

# Register your models here.
admin.site.register(register)
admin.site.register(Feedback)
admin.site.register(Admin)
