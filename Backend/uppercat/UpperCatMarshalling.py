from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
upperCat_marshalling = api.model('UpperCat', {
    "id_": fields.Integer(readOnly=True),
    "upper_category": fields.String(),
})
 