from django.contrib import admin
from .models import *


class AddressInlineAdmin(admin.TabularInline):
    model = AddressIssuance

    def get_extra(self, request, obj=None, **kwargs):
        return 1 if obj else 1



class ProductAdmin(admin.ModelAdmin):
    inlines = [AddressInlineAdmin]
    fields = ('name', 'type', 'date_delivery', 'file')
    list_display = ('name', 'type')
    list_filter = ('type', 'date_delivery')
    search_fields = ('name', 'date_delivery')


admin.site.register(Product, ProductAdmin)