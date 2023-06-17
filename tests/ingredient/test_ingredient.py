from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient('queijo mussarela')

    assert ingredient_1.name == 'queijo mussarela'
