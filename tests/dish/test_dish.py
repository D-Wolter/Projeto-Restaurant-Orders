from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_presun = Dish("lasanha presunto", 25.90)
    dish_berinj = Dish("lasanha berinjela", 27.00)

    msg1 = 'Dish price must be float.'
    msg2 = 'Dish price must be greater then zero.'
    msg3 = "missing 2 required positional arguments: 'name' and 'price'"

    dish_berinj.add_ingredient_dependency(Ingredient("massa de ravioli"), 120)

    assert dish_berinj.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.GLUTEN,
        }

    assert dish_berinj.name == "lasanha berinjela"
    assert dish_berinj.price == 27.0

    assert dish_berinj != dish_presun
    assert dish_berinj == dish_berinj

    assert repr(dish_berinj) == "Dish('lasanha berinjela', R$27.00)"
    assert repr(dish_berinj) != "Dish('lasanha presunto', R$25.90)"

    assert hash(dish_berinj) == hash(dish_berinj)
    assert hash(dish_berinj) != hash(dish_presun)

    assert dish_berinj.get_ingredients() == {Ingredient("massa de ravioli")}

    with pytest.raises(TypeError, match=msg3):
        Dish()

    with pytest.raises(TypeError, match=msg1):
        Dish("lasanha presunto", "25.90")

    with pytest.raises(ValueError, match=msg2):
        Dish("lasanha berinjela", -27.00)
