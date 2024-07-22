# -*- coding: utf-8 -*-
# from odoo import http


# class InvoiceCreation(http.Controller):
#     @http.route('/invoice_creation/invoice_creation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/invoice_creation/invoice_creation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('invoice_creation.listing', {
#             'root': '/invoice_creation/invoice_creation',
#             'objects': http.request.env['invoice_creation.invoice_creation'].search([]),
#         })

#     @http.route('/invoice_creation/invoice_creation/objects/<model("invoice_creation.invoice_creation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('invoice_creation.object', {
#             'object': obj
#         })

