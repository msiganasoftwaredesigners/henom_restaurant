from django.shortcuts import render
from .models import MenuCategory, MenuItem
from collections import defaultdict

def menu_view(request):
    # Get all menu categories
    categories = MenuCategory.objects.all()

    # Get all food items
    food_items = MenuItem.objects.filter(menu_type__name='food')

    # Group food items by menu_group
    food_menu_groups = defaultdict(list)
    for item in food_items:
        food_menu_groups[item.menu_group].append(item)

    # Get all drink items
    drink_items = MenuItem.objects.filter(menu_type__name='drink')

    # Group drink items by menu_group
    drink_menu_groups = defaultdict(list)
    for item in drink_items:
        drink_menu_groups[item.menu_group].append(item)

    context = {
        'categories': categories,
        'food_menu_groups': dict(food_menu_groups),
        'drink_menu_groups': dict(drink_menu_groups),
    }

    return render(request, 'menu.html', context)
