from odoo import models, fields, api


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    bank_acc_ids = fields.One2many(
        'res.partner.bank',
        'partner_id',
        string='Bank Accounts',
    )

# class Partner(models.Model):
#     _name = 'res.partner.bank'
#     _inherit = 'res.partner.bank'

#     partner_id = fields.Many2one(
#         'res.partner',
#         string='Related Partner',
#     )