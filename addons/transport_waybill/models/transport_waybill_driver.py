from odoo import models, fields


class Driver(models.Model):
    _name = "transport_waybill.driver"
    # _inherit = ['mail.thread']
    _description = "Driver"
    _order = "id desc, name"

    name = fields.Char(required=True)
    phone = fields.Char()
    telegram_user_id = fields.Char()
    vehicle_ids = fields.Many2many("transport_waybill.vehicle")
