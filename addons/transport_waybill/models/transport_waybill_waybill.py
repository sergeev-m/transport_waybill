from odoo import models, fields


class Waybill(models.Model):
    _name = "transport_waybill.waybill"
    _description = "Waybill"
    _order = "id desc, name"

    name = fields.Char(
        string="Number",
        required=True,
        readonly=True,
        copy=False,
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "transport_waybill.waybill"
        ),
    )

    driver_id = fields.Many2one("transport_waybill.driver", required=True)
    vehicle_id = fields.Many2one("transport_waybill.vehicle", required=True)
    date = fields.Date(default=fields.Date.today)
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent')])

    document = fields.Binary(
        string="Document",
        attachment=True,
    )

    document_filename = fields.Char(
        string="Filename",
    )

    def action_open_send_wizard(self):
        pass 

    def action_open_send_wizard(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": "Send Waybill",
            "res_model": "transport_waybill.send.wizard",
            "view_mode": "form",
            "view_id": self.env.ref(
                "transport_waybill.view_transport_waybill_send_wizard_form"
            ).id,
            "target": "new",
            "context": {
                "default_waybill_id": self.id,
            },
        }

    def action_preview_report(self):
        self.ensure_one()

        # return self.env.ref(
        #     "transport_waybill.action_report_waybill"
        # ).report_action(self)

        report = self.env.ref(
            "transport_waybill.action_report_waybill"
        )

        return {
            "type": "ir.actions.act_url",
            "url": f"/report/pdf/{report.report_name}/{self.id}",
            "target": "new",
        }
