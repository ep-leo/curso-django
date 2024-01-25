from django.shortcuts import render
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    """
    Render the home page with a list of recipes.

    :param request: The HTTP request.
    :return: The rendered home page.
    """
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category(request,category_id):
    """
    Retrieves recipes based on the given category ID and renders them on the home page.
    
    Args:
        request: The HTTP request object.
        category_id: The ID of the category to filter recipes by.
    
    Returns:
        The rendered home page with the filtered recipes.
    """
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

def recipe(request, id):
    """
    Function to render a recipe view page.

    Args:
        request: The HTTP request object.
        id: The ID of the recipe.

    Returns:
        The rendered recipe view page.
    """
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })