from django.contrib import admin
from .models import User1

# Register your models here.
@admin.register(User1)
class User1Admin(admin.ModelAdmin):
    list_display=('Fullname','email','address','mobile')