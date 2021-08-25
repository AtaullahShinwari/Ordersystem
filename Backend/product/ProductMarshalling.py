from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
product_marshalling = api.model('Product', {
    "id_": fields.Integer(readOnly=True),
    "name": fields.String(),
    "price": fields.String(readOnly=True),
    "description":fields.String(),
    "menu_id":fields.Integer(readOnly=True)
})
 