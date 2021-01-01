from django.contrib import admin
from language.models import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id','name','definition','family','code','status']
    list_filter = [ 'family','status']
    search_fields = ['name','description','family']
    ordering = ['id']
    readonly_fields = ('id',)


admin.site.register(Language,LanguageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','definition','status']
    search_fields = ['name','definition']
    ordering = ['id']
    readonly_fields = ('id',)

admin.site.register(Category,CategoryAdmin)



class WordAdmin(admin.ModelAdmin):
    fields = ['name', 'definiton', 'word_image', 'category', 'language', 'status']
    list_display = ['id','name', 'definiton', 'image_tag', 'category', 'language', 'status']
    list_filter = [ 'category','language', 'status']
    search_fields = ['name','definiton','category__name']
    ordering = ['id']
    readonly_fields = ('id','image_tag',)
    list_per_page = 20

admin.site.register(Word,WordAdmin)
