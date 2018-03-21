# from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Snippet

# class SnippetInline(admin.StackedInline):
#     model = Snippet
#     extra = 3


class SnippetAdmin(admin.ModelAdmin):
    model = Snippet
    fieldsets = [
        ('Title',               {'fields': ['title']}),
        ('Code',               {'fields': ['code']}),
        ('linenos',               {'fields': ['linenos']}),
        ('language',               {'fields': ['language'],'classes': ['collapse']}),
        ('style',               {'fields': ['style'],'classes': ['collapse']}),
        
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [SnippetInline]

admin.site.register(Snippet, SnippetAdmin)