from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
order_marshalling = api.model('Person', {
    "id_": fields.Integer(readOnly=True),
    "email": fields.String(),
    "google_user_id": fields.String(readOnly=True),
})
 