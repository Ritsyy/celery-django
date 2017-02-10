from django.contrib import admin
from .models import Image, Album

# Register your models here.
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]
    list_display_links =  ["title"]    
    list_editable = ["image"]
    list_filter = ["title", "image"]
    search_fields = ["title", "image"]

    class Meta:
        model = Image

class AlbumModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_display_links =  ["title", "description"] 
    list_filter = ["title", "description"]
    search_fields = ["title", "description"]
    
    class Meta:
        model = Album

class ImageInline(admin.StackedInline):
    model = Image

class AlbumInline(admin.StackedInline):
    inlines = [ ImageInline, ]

admin.site.register(Image, ImageModelAdmin)
admin.site.register(Album, AlbumModelAdmin)