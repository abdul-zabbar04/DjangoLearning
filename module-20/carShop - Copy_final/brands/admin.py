from django.contrib import admin
from brands import models
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('name',)}
    list_display=['name', 'slug']
admin.site.register(models.BrandModel, BrandAdmin)
