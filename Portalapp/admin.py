from django.contrib import admin
from .models import Category, Blog
from django_summernote.admin import SummernoteModelAdmin



class NewsAdmin (SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display= ('title', 'text_min',)
    list_display_links = ('title', 'text_min')
    search_fields=('title', 'content')
    summer_note_fields = ('content','text_min')



admin.site.register(Category)
admin.site.register(Blog, NewsAdmin)