# -*- coding: utf-8 -*-
# from odoo import http


# class OmKota(http.Controller):
#     @http.route('/om_kota/om_kota', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_kota/om_kota/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_kota.listing', {
#             'root': '/om_kota/om_kota',
#             'objects': http.request.env['om_kota.om_kota'].search([]),
#         })

#     @http.route('/om_kota/om_kota/objects/<model("om_kota.om_kota"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_kota.object', {
#             'object': obj
#         })
