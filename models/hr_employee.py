from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    visitor_ids = fields.One2many(
        comodel_name='visitor.visitor',
        inverse_name='employees_ids',  # the Many2many field in visitor.visitor
        string='Visitors'
    )
