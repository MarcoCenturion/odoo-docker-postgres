# -*- coding: utf-8 -*-
# from odoo import http


# class Datospax(http.Controller):
#     @http.route('/datospax/datospax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/datospax/datospax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('datospax.listing', {
#             'root': '/datospax/datospax',
#             'objects': http.request.env['datospax.datospax'].search([]),
#         })

#     @http.route('/datospax/datospax/objects/<model("datospax.datospax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('datospax.object', {
#             'object': obj
#         })
