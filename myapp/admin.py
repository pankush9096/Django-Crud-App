from django.contrib import admin
from .models import Login, Python, students, Register

# Register your models here.

admin.site.register(Login)
admin.site.register(Python)
admin.site.register(students)
admin.site.register(Register)