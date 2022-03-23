from django.contrib import admin
from .models import ImagenBase
# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    readonly_fiels = ('created','updated')

admin.site.register(ImagenBase,ImagenAdmin)