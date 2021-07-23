# -*- coding: utf-8 -*-
# from odoo import http


# class Copiartst(http.Controller):
#     @http.route('/copiartst/copiartst/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copiartst/copiartst/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('copiartst.listing', {
#             'root': '/copiartst/copiartst',
#             'objects': http.request.env['copiartst.copiartst'].search([]),
#         })

#     @http.route('/copiartst/copiartst/objects/<model("copiartst.copiartst"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copiartst.object', {
#             'object': obj
#         })
