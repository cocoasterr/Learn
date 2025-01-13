# -*- coding: utf-8 -*-
# from odoo import http


# class OmBank(http.Controller):
#     @http.route('/om_bank/om_bank', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_bank/om_bank/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_bank.listing', {
#             'root': '/om_bank/om_bank',
#             'objects': http.request.env['om_bank.om_bank'].search([]),
#         })

#     @http.route('/om_bank/om_bank/objects/<model("om_bank.om_bank"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_bank.object', {
#             'object': obj
#         })

