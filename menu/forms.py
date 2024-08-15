from django import forms
from .models import MenuItem

class MenuItemForm(forms.ModelForm):
    menu_group = forms.ChoiceField()

    class Meta:
        model = MenuItem
        fields = ['menu_type', 'menu_group', 'name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'menu_type' in self.data:
            try:
                menu_type_id = int(self.data.get('menu_type'))
                self.fields['menu_group'].choices = [(item.menu_group, item.menu_group) for item in MenuItem.objects.filter(menu_type_id=menu_type_id).distinct()]
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['menu_group'].choices = [(item.menu_group, item.menu_group) for item in MenuItem.objects.filter(menu_type=self.instance.menu_type).distinct()]
        else:
            self.fields['menu_group'].choices = []
