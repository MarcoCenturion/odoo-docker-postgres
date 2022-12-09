# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderCost(http.Controller):
#     @http.route('/sale_order_cost/sale_order_cost/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_cost/sale_order_cost/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_cost.listing', {
#             'root': '/sale_order_cost/sale_order_cost',
#             'objects': http.request.env['sale_order_cost.sale_order_cost'].search([]),
#         })

#     @http.route('/sale_order_cost/sale_order_cost/objects/<model("sale_order_cost.sale_order_cost"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_cost.object', {
#             'object': obj
#         })
