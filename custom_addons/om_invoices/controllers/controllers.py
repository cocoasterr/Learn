# -*- coding: utf-8 -*-
# from odoo import http


# class OmInvoices(http.Controller):
#     @http.route('/om_invoices/om_invoices', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_invoices/om_invoices/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_invoices.listing', {
#             'root': '/om_invoices/om_invoices',
#             'objects': http.request.env['om_invoices.om_invoices'].search([]),
#         })

#     @http.route('/om_invoices/om_invoices/objects/<model("om_invoices.om_invoices"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_invoices.object', {
#             'object': obj
#         })
