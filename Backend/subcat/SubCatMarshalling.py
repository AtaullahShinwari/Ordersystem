from flask_restx import fields
from Backend.configs.base import api

"""Anlegen von transferierbaren Strukturen"""
subcat_marshalling = api.model('UpperCat', {
    "id_": fields.Integer(readOnly=True),
    "sub_category": fields.String(),
    "upper_category": fields.Integer(),
})
 