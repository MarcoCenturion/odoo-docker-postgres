# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/passengersData(http.Controller):
#     @http.route('//mnt/extra-addons/passengers_data//mnt/extra-addons/passengers_data/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/passengers_data//mnt/extra-addons/passengers_data/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/passengers_data.listing', {
#             'root': '//mnt/extra-addons/passengers_data//mnt/extra-addons/passengers_data',
#             'objects': http.request.env['/mnt/extra-addons/passengers_data./mnt/extra-addons/passengers_data'].search([]),
#         })

#     @http.route('//mnt/extra-addons/passengers_data//mnt/extra-addons/passengers_data/objects/<model("/mnt/extra-addons/passengers_data./mnt/extra-addons/passengers_data"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/passengers_data.object', {
#             'object': obj
#         })
