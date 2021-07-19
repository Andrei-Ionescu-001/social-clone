from django.contrib import admin
from  . import models
# Register your models here.

# class PostMemberInline(admin.TabularInline):
#     model=models.Post
admin.site.register(models.Post)