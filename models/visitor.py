from odoo import models,fields,api

class visitor(models.Model):
    _name="visitor.visitor"
    _description="Visitor"

    name=fields.Char(string="Name",required=True)
    phone =fields.Char(string="Phone")
    address =fields.Char(string="Address")
    purpose =fields.Char(string="Purpose")
    check_in = fields.Datetime(string="Check-In Time")
    check_out = fields.Datetime(string="Check-Out Time")
    status=fields.Selection(
        [
            ('draft', 'Draft'),
            ('checked_in', 'Checked In'),
            ('checked_out', 'Checked Out'),
        ],
        string="Status",
        default='draft'

    )
    # stay_duration =fields.Float(
    #     string='Stay Duration (Hours)',
    #     compute="_compute_stay_duration",
    #     store=True
    # )
    stay_duration = fields.Char(
        string="Stay Duration (H:M:S)",
        compute="_compute_stay_duration",
        store=True
    )
    late_checkout = fields.Boolean(
        string="Late Checkout",
        compute="_compute_late_checkout"
    )
    employees_ids = fields.Many2many(
    'hr.employee',
    'visitor_employee_rel',
    'visitor_id',
    'employee_id',
    string="Visited Employees"
)

    def action_check_in(self):
        for rec in self:
            rec.check_in=fields.Datetime.now()
            rec.status='checked_in'

    def action_check_out(self):
        for rec in self:
            rec.check_out=fields.Datetime.now()
            rec.status='checked_out'
    
    @api.depends('check_in','check_out')
    def _compute_stay_duration(self):
        for rec in self:
            if rec.check_in and rec.check_out:
                delta = rec.check_out - rec.check_in
       
                total_seconds = int(delta.total_seconds())
     
                hours = total_seconds // 3600
                minutes = (total_seconds % 3600) // 60
                seconds = total_seconds % 60
                rec.stay_duration = f"{hours}h:{minutes}m:{seconds}s"
            else:
           
                rec.stay_duration = "0h:0m:0s"

    def action_print_visitor_card(self):
        return self.env.ref('visitor_management.action_print_visitor_card').report_action(self)

    @api.depends('check_in', 'check_out')
    def _compute_late_checkout(self):
        today = fields.Date.context_today(self)
        for rec in self:
            if rec.check_in and not rec.check_out:
                checkin_date = rec.check_in.date()
                rec.late_checkout = checkin_date < today
            else:
                rec.late_checkout = False
