from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
order_marshalling = api.model('Order', {
    "id_": fields.Integer(readOnly=True),
    "upper_category": fields.String(),
    "subcategory": fields.String(),
})
 