class Ingredient:
    """
    This is a wrapper class for the various ingredients. It is used both by the Inventory and Beverage classes.
    """
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.qty

    def resize_quantity(self, new_qty):
        self.qty = new_qty
