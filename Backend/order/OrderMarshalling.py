from flask_restx import fields
from app.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
order_marshalling = api.model('Order', {
    "quantity": fields.Integer(),
    "annotation": fields.String(),
    "tablenumber": fields.Integer(readOnly=True),
    "product_id": fields.Integer(readOnly=True),
    "order_status": fields.Boolean(readOnly=True),
    "id_": fields.Integer(readOnly=True),
})
 