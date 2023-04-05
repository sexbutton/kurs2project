from django.contrib import admin
from .models import Product, Category, Cart, Type
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","image_show","price","description","date", "category"]
    
    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='60' />".format(obj.img.url))
        return None

    image_show.__name__ = "Картинка"




admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Type)


