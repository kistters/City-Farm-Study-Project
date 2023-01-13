import pytest

from cityfarm import Farmer, StreetFair


@pytest.mark.parametrize("ingredient,quantity", [
    ("tomato", 10),
    ("cheese", 2),
])
def test_farmer_producing_ingredients(ingredient, quantity):
    ingredients = Farmer('Will').produce_ingredient(item=ingredient, quantity=quantity)
    assert len(ingredients) == quantity
    assert ingredient in ingredients


def test_request_ingredients_at_street_fair_incrementing_the_demand():
    requested_ingredients = ["bread", "cut_of_meat", "cheese", "tomato", "onion", "lettuce", "cheese", "cheese"]
    street_fair = StreetFair()
    street_fair.request_ingredients(requested_ingredients)
    assert sorted(street_fair.demand) == sorted(requested_ingredients)
    assert street_fair.demand.count("cheese") == requested_ingredients.count("cheese")


def test_increase_ingredient_at_street_fair_incrementing_the_offer():
    produced_ingredients = ["cheese", "cheese", "cheese"]
    street_fair = StreetFair()

    street_fair.increase_ingredient(produced_ingredients)

    assert sorted(street_fair.supply) == sorted(produced_ingredients)
    assert street_fair.supply.count("cheese") == produced_ingredients.count("cheese")


def test_summary_at_street_fair_demand_and_offer():
    requested_ingredients = ["bread", "cut_of_meat", "cheese", "tomato", "onion", "lettuce", "cheese"]
    produced_ingredients = ["cheese", "leafy_green", "tomato", "cheese"]
    street_fair = StreetFair()

    street_fair.request_ingredients(requested_ingredients)
    street_fair.increase_ingredient(produced_ingredients)

    assert street_fair.summary() == {
        'demand': {'cheese': 2, 'bread': 1, 'cut_of_meat': 1, 'tomato': 1, 'onion': 1, 'lettuce': 1},
        'supply': {'cheese': 2, 'leafy_green': 1, 'tomato': 1}
    }
