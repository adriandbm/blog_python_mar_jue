from django.contrib import admin
from .models import Publication

# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display= (
        "title",
        "author",
    ) 
    list_filter = (
        "author", "title",
    )
    search_fields= (
        "title",
        "body",
        "author__username"
    )
admin.site.register(Publication, PublicationAdmin) 