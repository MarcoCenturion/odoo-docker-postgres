# -*- coding: utf-8 -*-
# from odoo import http


# class CotizadorAmadeus(http.Controller):
#     @http.route('/cotizador_amadeus/cotizador_amadeus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cotizador_amadeus/cotizador_amadeus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cotizador_amadeus.listing', {
#             'root': '/cotizador_amadeus/cotizador_amadeus',
#             'objects': http.request.env['cotizador_amadeus.cotizador_amadeus'].search([]),
#         })

#     @http.route('/cotizador_amadeus/cotizador_amadeus/objects/<model("cotizador_amadeus.cotizador_amadeus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cotizador_amadeus.object', {
#             'object': obj
#         })

