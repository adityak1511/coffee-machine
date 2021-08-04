from marshmallow import Schema, fields

"""
This file contains Schema classes which are used for input validation.
"""


class MachineOutletSchema(Schema):
    count_n = fields.Int(required=True)


class CoffeeMachineSchema(Schema):
    outlets = fields.Nested(MachineOutletSchema, required=True)
    total_items_quantity = fields.Dict(required=True)
    beverages = fields.Dict(required=True)


class InputSchema(Schema):
    machine = fields.Nested(CoffeeMachineSchema, required=True)
