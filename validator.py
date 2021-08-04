from marshmallow import ValidationError
from schemas import InputSchema


class InputProcessor:
    """
    This validates and returns the input data in the form in which our code expects it.
    In case we supply an invalid input, we output the relevant error messages using the third-party
    marshmallow library.
    """
    def get_input_params(self, payload):
        outlet_count = None
        total_items_quantity = None
        beverage_dicts = None
        payload = self._validate(payload)
        if not payload:
            return False, outlet_count, total_items_quantity, beverage_dicts
        outlet_count = payload['machine']['outlets']['count_n']
        total_items_quantity = payload['machine']['total_items_quantity']
        beverage_dicts = payload['machine']['beverages']
        return True, outlet_count, total_items_quantity, beverage_dicts

    @classmethod
    def _validate(cls, payload):
        try:
            payload = InputSchema().load(payload)
        except ValidationError as err:
            print(err.messages)
            return None
        return payload
