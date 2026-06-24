from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def recipe(request):

    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )

        return redirect('/recipe/')

    recipes = Recipe.objects.all()

    # Search
    search = request.GET.get('search')

    if search:
        recipes = recipes.filter(recipe_name__icontains=search)

    context = {'recipes': recipes}

    return render(request, "recipies.html", context)


def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()

    return redirect('/recipe/')


def update_recipe(request, id):

    recipe = Recipe.objects.get(id=id)

    if request.method == "POST":

        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description

        if recipe_image:
            recipe.recipe_image = recipe_image

        recipe.save()

        return redirect('/recipe/')

    context = {
        'recipe': recipe
    }

    return render(request, 'recipe_update.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does't exist")
            return redirect('/login/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect("/recipe/")
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")
            return render(request, 'register.html' )
        
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        messages.success(request, "Account created successfully")
        return redirect('/login/')
    return render(request, 'register.html')