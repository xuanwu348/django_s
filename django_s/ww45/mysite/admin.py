from django.contrib import admin
from mysite.models import Maker, PModel, Product, PPhoto 

# Register your models here.
class MakerPost(admin.ModelAdmin):
    list_display = ("name", "country")

class PModelPost(admin.ModelAdmin):
    list_display = ("maker", "name")

class ProductPost(admin.ModelAdmin):
    list_display = ("pmodel","nickname","year")

class PPhotoPost(admin.ModelAdmin):
    list_display = ("product", "description")


admin.site.register(Maker, MakerPost)
admin.site.register(PModel, PModelPost)
admin.site.register(Product, ProductPost)
admin.site.register(PPhoto, PPhotoPost)
