# -*- coding: utf-8 -*-
# from odoo import http


# class Pasajeros(http.Controller):
#     @http.route('/pasajeros/pasajeros/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pasajeros/pasajeros/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pasajeros.listing', {
#             'root': '/pasajeros/pasajeros',
#             'objects': http.request.env['pasajeros.pasajeros'].search([]),
#         })

#     @http.route('/pasajeros/pasajeros/objects/<model("pasajeros.pasajeros"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pasajeros.object', {
#             'object': obj
#         })
