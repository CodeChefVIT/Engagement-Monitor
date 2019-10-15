from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'slug', 'one','two','three','created_on')
    list_filter = ("user_name",)
    search_fields = ['file_name', 'one','two','three']
    prepopulated_fields = {'slug': ('file_name',)}
  
admin.site.register(Post, PostAdmin)