from odoo import models, fields, api


class om_kota(models.Model):
    _name = 'vit.om_kota'
    _description = 'kota management'

    name = fields.Char(string='Name')
    state_id = fields.Many2one('res.country.state', string='State')

class Partner(models.Model):
    _inherit = 'res.partner'

    kota_id = fields.Many2one('vit.om_kota', string='Kota')