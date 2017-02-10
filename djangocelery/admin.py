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

class ImageInline(admin.StackedInline):
    model = Image

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_display_links =  ["title", "description"] 
    list_filter = ["title", "description"]
    search_fields = ["title", "description"]
    inlines = [ ImageInline, ]    
    
    class Meta:
        model = Album

admin.site.register(Image, ImageModelAdmin)
admin.site.register(Album, AlbumAdmin)