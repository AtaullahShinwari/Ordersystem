from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
order_marshalling = api.model('Order', {
    "quantity": fields.Integer(),
    "annotation": fields.String(),
    "table_": fields.Integer(readOnly=True),
    "product": fields.Integer(readOnly=True),
    "id_": fields.Integer(readOnly=True),
})
 