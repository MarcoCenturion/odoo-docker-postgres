#-*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    supplier = fields.Text(String='Travel Supplier')
    supplier_file = fields.Text(String='Travel Supplier file number')
    currency = fields.Selection([
        ('USD', 'Dollars'),
        ('ARS', 'Pesos Argentinos'),
        ('EUR', 'Euros')],
                                'currency',
                                default='ARS',
                                required=True)
    price = fields.Float(String='Supplier net price', digits=(10,2))
    bills = fields.Float(String='Supplier add bills', digits=(10,2))
    description = fields.Text(String='Tour short description')
    settlement = fields.Binary(String='Supplier Settlement')
    state = fields.Selection([
        ('RQ', 'Requested'),
        ('OK', 'Confirmed'),
        ('HL', 'Pending'),
        ('XX', 'Canceled')],
                             'state',
                             default='HL',
                             required=True)
