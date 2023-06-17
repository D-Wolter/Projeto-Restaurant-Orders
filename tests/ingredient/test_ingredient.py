from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    ANIMAL_DERIVED = "ANIMAL_DERIVED"
    LACTOSE = "LACTOSE"
    CHEESE = Ingredient('queijo mussarela')

    animal_restriction = Ingredient(ANIMAL_DERIVED)
    lactose_restriction = Ingredient(LACTOSE)

    assert hash(animal_restriction) == hash(animal_restriction)
    assert hash(animal_restriction) != hash(lactose_restriction)

    assert animal_restriction == animal_restriction
    assert animal_restriction != lactose_restriction

    assert repr(animal_restriction) == f"Ingredient('{ANIMAL_DERIVED}')"

    assert animal_restriction.restrictions == set()

    assert CHEESE.__eq__(LACTOSE) is False
    assert CHEESE.__eq__(CHEESE) is True

    with pytest.raises(TypeError, match="missing 1 required"):
        Ingredient()
