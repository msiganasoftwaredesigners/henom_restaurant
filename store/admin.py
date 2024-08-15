from django.contrib import admin
from store.models import Product, ProductImage
import nested_admin
from msigana_ecommerce.admin_site import admin_site

class ProductImageInline(nested_admin.NestedTabularInline):
    model = ProductImage
    fields = ('image', 'is_main')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2 if obj is None else 0
        return extra

class ProductAdmin(nested_admin.NestedModelAdmin):
    prepopulated_fields = {'product_slug': ('product_name',)}
    list_display = ('product_name',)
    inlines = [ProductImageInline]
    readonly_fields = ['product_owner']

    # Exclude the optional fields from being displayed in the admin form
    exclude = ['product_phone', 'product_stock', 'product_views_count', 'product_brand', 'product_is_available', 'product_owner']

    class Media:
        js = ('js/admin.js',)

    def save_model(self, request, obj, form, change):
        if not change:  # the object is being created, so set the user
            obj.product_owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(product_owner=request.user)
        return qs

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # remove the product_owner field from the form if the user is not a superuser
        if not request.user.is_superuser:
            form.base_fields.pop('product_owner', None)
        return form

    def add_view(self, request, form_url='', extra_context=None):
        return super().add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super().change_view(request, object_id, form_url, extra_context)

    def render_change_form(self, request, context, *args, **kwargs):
        return super().render_change_form(request, context, *args, **kwargs)

admin_site.register(Product, ProductAdmin)
