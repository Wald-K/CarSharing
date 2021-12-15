from marshmallow import Schema, fields



class CarSchema(Schema):
    id = fields.Str(required=True)
    model = fields.Str(required=True)
    production_date = fields.DateTime(format="%Y-%m-%d", required=False)
    licence_number = fields.Str(required=True)

