from django.contrib import admin
from django.http.request import HttpRequest
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__name', 'status')
    list_editable = ('is_featured',)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(About,AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)
