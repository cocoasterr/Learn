from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta  # Import library untuk manipulasi tanggal


class om_invoices(models.Model):
    _inherit = 'res.partner'

    def action_create_invoices(self):
        for partner in self:
            # Cari produk berdasarkan nama
            product = self.env['product.product'].search([('name', '=', 'Storage Box')], limit=1)
            
            if not product:
                raise ValueError("Produk 'Storage Box' tidak ditemukan.")
            
            # date = 01 in nexh month
            next_month_date = (datetime.now() + relativedelta(months=1)).replace(day=1)
            
            # Buat invoice untuk partner
            invoice = self.env['account.move'].create({
                'partner_id': partner.id,
                'invoice_date': next_month_date,  # Format tanggal
                'move_type': 'out_invoice',  # Ganti 'type' dengan 'move_type'
                'invoice_line_ids': [(0, 0, {
                    'name': 'Monthly Subscription',
                    'product_id': product.id,
                    'quantity': 1,
                    'price_unit': product.lst_price,
                    'account_id': product.categ_id.property_account_income_categ_id.id,
                })]
            })
            # Posting invoice
            invoice.action_post()