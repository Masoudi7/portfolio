from django.contrib import admin
from .models import Article
# Register your models here.
class Articleadmin(admin.ModelAdmin):
    list_display=('title','slug','publish','status')
    list_filter=('publish','status')
    search_fields=('title','description')
    prepopulated_fields={'slug':('title',)}
    ordering=['-publish','status']
    
admin.site.register(Article,Articleadmin)
