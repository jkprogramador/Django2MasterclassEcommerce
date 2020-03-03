from django.contrib import admin

from .models import Order, Product

admin.site.site_header = 'E-commerce site'
admin.site.site_title = 'ABC Shopping'
admin.site.index_title = 'Manage ABC Shopping'

class ProductAdmin(admin.ModelAdmin):

  def change_category_to_default(self, request, queryset):
    queryset.update(category = 'default')
  
  list_display = ('title', 'price', 'discount_price', 'category', 'description', 'image')
  search_fields = ['title', 'category']
  actions = ['change_category_to_default']
  change_category_to_default.short_description = 'Default category'
  fields = ['title', 'price']
  list_editable = ['image', 'category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
