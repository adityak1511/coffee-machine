from ingredient_class import Ingredient


class Beverage:
    """
    This class is responsible for managing the functionalities of a beverage drink.
    """
    def __init__(self, name, quantity_map):
        self.name = name
        self._ingredients = {}
        for name, qty in quantity_map.items():
            self._ingredients[name] = Ingredient(name, qty)

    def get_name(self):
        return self.name

    def yield_ingredients(self):
        for name, _ingredient in self._ingredients.items():
            yield _ingredient
