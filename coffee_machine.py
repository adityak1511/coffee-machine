from beverage_manager import Beverage
from inventory import Inventory


class CoffeeMachine:
    """
    This is the core coffee machine class composed of the machine inventory and the supplied input beverages.
    It can serve outlet_count number of beverages at a time.
    """
    def __init__(self, outlet_count, total_items_quantity, beverage_dicts):
        self._outlet_count = outlet_count
        self._inventory = Inventory(total_items_quantity)
        self._beverages = {}
        for name, quantity_map in beverage_dicts.items():
            self._beverages[name] = Beverage(name, quantity_map)

    def serve_beverages(self):
        """
        The main method responsible for serving the beverages. It interacts with the machine's inventory to
        fetch the required ingredients for a beverage and outputs the prepared drink if it is possible to do so.
        """
        for idx, beverage_name in enumerate(self._beverages):
            if idx >= self._outlet_count:
                print(f'Sorry, can only serve {self._outlet_count} at a time. Please try again later.')
                continue
            print(f'Serving {beverage_name}...')
            beverage = self._beverages[beverage_name]
            is_prepared = True
            for ingredient in beverage.yield_ingredients():
                try:
                    self._inventory.fetch_ingredient(ingredient)
                except Exception as err:
                    print(err)
                    is_prepared = False
                    break
            if is_prepared:
                print(f'{beverage_name} is prepared\n')
            else:
                print(f'{beverage_name} could not be prepared\n')
