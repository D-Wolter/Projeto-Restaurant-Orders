from models.ingredient import Ingredient
from models.dish import Dish
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding="utf-8", newline='') as file:
            self.ingredients = set()
            all_dishes = csv.DictReader(file, delimiter=",", quotechar='"')
            recipes = {}

            for recipe in all_dishes:
                ingredient_key = recipe["ingredient"]
                ingredient_instance = Ingredient(ingredient_key)
                self.ingredients.add(ingredient_instance)

                dish_name = recipe["dish"]
                dish_price = float(recipe["price"])

                if dish_name not in recipes:
                    dish_instance = Dish(dish_name, dish_price)
                    recipes[dish_name] = dish_instance

                ingredient_quantity = int(recipe["recipe_amount"])
                recipes[dish_name].add_ingredient_dependency(
                    ingredient_instance, ingredient_quantity
                )

        self.dishes = set(recipes.values())
