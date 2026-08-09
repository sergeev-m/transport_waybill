from odoo import fields, models, api


class TransportWaybillSendWizard(models.TransientModel):
    _name = "transport_waybill.send.wizard"
    _description = "Send Waybill Wizard"

    waybill_id = fields.Many2one(
        "transport_waybill.waybill",
        required=True,
        readonly=True,
    )

    driver_id = fields.Many2one(
        related="waybill_id.driver_id",
        readonly=True
    )

    vehicle_id = fields.Many2one(
        related="waybill_id.vehicle_id",
        readonly=True,
    )

    send_telegram = fields.Boolean(
        string="Telegram",
    )

    send_max = fields.Boolean(
        string="MAX",
    )

    send_email = fields.Boolean(
        string="Email",
    )

    def action_send(self):
        self.ensure_one()

        # TODO: генерация документа и отправка
        return {"type": "ir.actions.act_window_close"}

    @api.depends("waybill_id")
    def _compute_driver_vehicle(self):
        for wizard in self:
            wizard.driver_id = wizard.waybill_id.driver_id
            wizard.vehicle_id = wizard.waybill_id.vehicle_id