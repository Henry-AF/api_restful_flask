from api import ma
from marshmallow import Schema, fields

class CarSchemas(ma.Schema):
    class Meta():
        fields = ('_id', 'modelo', 'marca', 'ano')
    _id = fields.Str()
    modelo = fields.Str(required=True)
    marca = fields.Str(required=True)
    ano = fields.Str(required=True)
