from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published')
    list_display_links = ('rubric', 'title', 'content')
    search_fields = ('rubric', 'title', 'content')

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Rubric, RubricAdmin)
admin.site.register(Bb, BbAdmin)

