from django.contrib import admin
from .models import MenuCategory, MenuGroup, MenuItem
from msigana_ecommerce.admin_site import admin_site
from django.utils.text import slugify
from django.utils.html import strip_tags
from django import forms
from django.db.models import Q

def generate_slug(name):
    """
    Generates a slug from the given name.
    """
    return slugify(strip_tags(name))

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = generate_slug(obj.name)
        
        if MenuCategory.objects.filter(slug=obj.slug).exists():
            if not change or (change and obj.pk):
                return
            else:
                obj.pk = None

        super().save_model(request, obj, form, change)

class MenuGroupAdminForm(forms.ModelForm):
    class Meta:
        model = MenuGroup
        fields = '__all__'
        exclude = ['date']  # Exclude 'date' field from the admin form

class MenuGroupAdmin(admin.ModelAdmin):
    form = MenuGroupAdminForm
    list_display = ('id', 'name', 'menu_type', 'slug', 'date')
    search_fields = ('name', 'menu_type__name', 'slug')

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = generate_slug(obj.name)
        
        if MenuGroup.objects.filter(menu_type=obj.menu_type, slug=obj.slug).exists():
            if not change or (change and obj.pk):
                return
            else:
                obj.pk = None

        super().save_model(request, obj, form, change)

class MenuItemAdminForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['menu_group'].queryset = MenuGroup.objects.filter(menu_type=self.instance.menu_type)


class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemAdminForm
    list_display = ('id', 'name', 'menu_type', 'menu_group', 'price', 'slug')
    list_filter = ('menu_type', 'menu_group')
    search_fields = ('name', 'menu_type__name', 'menu_group__name', 'slug')
    autocomplete_fields = ('menu_type', 'menu_group')
    prepopulated_fields = {"slug": ("name",)}

    def save_model(self, request, obj, form, change):
        # If slug is not set, generate it based on the name
        if not obj.slug:
            obj.slug = generate_slug(obj.name)

        # Check if a MenuItem with the same slug, menu_type, and menu_group exists
        if MenuItem.objects.filter(menu_type=obj.menu_type, menu_group=obj.menu_group, slug=obj.slug).exists():
            if not change:
                # If it's not a change (i.e., new object), assign a new pk to avoid collision
                obj.pk = None

        # Save the object to the database
        super().save_model(request, obj, form, change)


admin_site.register(MenuItem, MenuItemAdmin)
admin_site.register(MenuCategory, MenuCategoryAdmin)
admin_site.register(MenuGroup, MenuGroupAdmin)
