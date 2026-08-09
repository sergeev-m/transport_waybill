{
    "name": "Transport",
    "version": "19.0.0.1",
    "summary": "Накладные",
    "category": "Fleet",
    "author": "https://t.me/sergeev_mikhail",
    # "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence.xml",
        "views/transport_waybill_driver.xml",
        "views/transport_waybill_vehicle.xml",
        "views/transport_waybill_waybill.xml",
        "views/transport_waybill_send_wizard.xml",
        "views/menu.xml",
        "report/transport_waybill_report.xml",
        "data/demo_data.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
