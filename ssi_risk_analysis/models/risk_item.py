# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class RiskItem(models.Model):
    _name = "risk_item"
    _inherit = ["mixin.master_data"]
    _description = "Risk Item"

    result_ids = fields.One2many(
        string="Results",
        comodel_name="risk_item.result",
        inverse_name="item_id",
    )
    method = fields.Selection(
        string="Method",
        selection=[
            ("manual", "Manual"),
            ("worksheet", "Worksheet"),
            ("custom", "Custom Worksheet"),
        ],
        default="manual",
        required=True,
    )
    worksheet_type_id = fields.Many2one(
        string="Worksheet Type",
        comodel_name="risk_analysis_worksheet_type",
    )

    @api.onchange(
        "method",
    )
    def onchange_worksheet_type_id(self):
        self.worksheet_type_id = False

    allowed_result_ids = fields.Many2many(
        string="Allowed Risk Analysis Results",
        comodel_name="risk_analysis_result",
        compute="_compute_allowed_result_ids",
        store=False,
    )

    def _compute_allowed_result_ids(self):
        for record in self:
            result = self.env["risk_analysis_result"]
            for ra_result in record.result_ids:
                result += ra_result.result_id
            record.allowed_result_ids = result
