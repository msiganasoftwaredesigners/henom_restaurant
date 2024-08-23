from django.shortcuts import render
from .models import MenuCategory, MenuItem, MenuGroup
from collections import defaultdict

def menu_view(request):
    # Get all menu categories
    categories = MenuCategory.objects.all()

    # Get all food items, ordered by menu_group's date
    food_menu_groups = defaultdict(list)
    for group in MenuGroup.objects.filter(menu_type__name='food').order_by('date'):
        food_items = MenuItem.objects.filter(menu_type=group.menu_type, menu_group=group)
        food_menu_groups[group] = list(food_items)

    # Get all drink items, ordered by menu_group's date
    drink_menu_groups = defaultdict(list)
    for group in MenuGroup.objects.filter(menu_type__name='drink').order_by('date'):
        drink_items = MenuItem.objects.filter(menu_type=group.menu_type, menu_group=group)
        drink_menu_groups[group] = list(drink_items)

    context = {
        'categories': categories,
        'food_menu_groups': dict(food_menu_groups),
        'drink_menu_groups': dict(drink_menu_groups),
    }

    return render(request, 'menu.html', context)
