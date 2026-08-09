from odoo import models, fields


class Vehicle(models.Model):
    _name = "transport_waybill.vehicle"
    _description = "Vehicle"
    _order = "id desc, name"

    name = fields.Char(required=True)
    license_plate = fields.Char(required=True)
