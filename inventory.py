from ingredient_class import Ingredient


class Inventory:

    """
    This class manages the ingredient inventory for the coffee machine.
    It exposes 2 public methods: fetch_ingredient and refill_ingredient.
    It is also responsible for displaying the low quantity warning if any ingredient's quantity goes below 10%.
    """

    LOW_INVENTORY_THRESHOLD_PERCENT = 10

    def __init__(self, total_items_quantity):
        self._inventory = {}
        self._capacity = {}
        for name, quantity in total_items_quantity.items():
            self._inventory[name] = Ingredient(name, quantity)
            self._capacity[name] = Ingredient(name, quantity)

    def fetch_ingredient(self, ingredient):
        """
        Fetches the requested ingredient from the inventory.
        Raises relevant exceptions in case we are not able to do so.
        """
        self._validate_ingredient(ingredient)
        self._validate_quantity(ingredient)
        self._resize_ingredient(ingredient)
        self._check_inventory(ingredient)
        return ingredient.get_quantity()

    def refill_ingredient(self, ingredient):
        """
        Exposes a method for refilling a particular ingredient in teh inventory.
        We can never go above the initial supplied capacity for any ingredient.
        """
        name = ingredient.get_name()
        add_qty = ingredient.get_quantity()
        current_qty = self._inventory[name].get_quantity()
        final_qty = self._sanitize_ingredient_qty(ingredient, current_qty + add_qty)
        self._inventory[name].resize_quantity(final_qty)

    def _resize_ingredient(self, ingredient):
        name = ingredient.get_name()
        qty = ingredient.get_quantity()
        curr_qty = self._inventory[name].get_quantity()
        self._inventory[name].resize_quantity(curr_qty - qty)

    def _check_inventory(self, ingredient):
        name = ingredient.get_name()
        initial_qty = self._capacity[name].get_quantity()
        current_qty = self._inventory[name].get_quantity()
        if (current_qty / initial_qty) * 100 <= self.LOW_INVENTORY_THRESHOLD_PERCENT:
            self._show_low_quantity_indicator(name)

    @classmethod
    def _show_low_quantity_indicator(cls, name):
        print(f'[INVENTORY ALERT] {name} quantity is low. Please refill.')

    def _validate_ingredient(self, ingredient):
        if ingredient.get_name() not in self._inventory:
            raise Exception(f'Ingredient {ingredient.get_name()} is not available in the inventory')

    def _validate_quantity(self, ingredient):
        if self._inventory[ingredient.get_name()].get_quantity() < ingredient.get_quantity():
            raise Exception(f'Ingredient {ingredient.get_name()} is not sufficient')

    def _sanitize_ingredient_qty(self, ingredient, qty):
        capacity = self._capacity[ingredient.get_name()].get_quantity()
        if qty > capacity:
            return capacity
        return qty
