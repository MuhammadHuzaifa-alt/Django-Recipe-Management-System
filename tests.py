from django.test import TestCase
# Create your tests here.
from .models import Recipe

class RecipeTest(TestCase):
    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            recipe_name="Tea",
            recipe_description="Hot tea"
        )
        self.assertEqual(recipe.recipe_name, "Tea")