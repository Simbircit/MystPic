from django.contrib import admin
from .models import Profile, Category, Mystery, Comment
# Register your models here.

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Mystery)
admin.site.register(Comment)
