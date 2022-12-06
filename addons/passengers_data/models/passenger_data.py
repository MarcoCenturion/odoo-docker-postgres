# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = "res.partner" 
    dob = fields.Date(String='Date of Birth')
    document = fields.Char(String='Número de DNI', size = 30, index=True)
    passport = fields.Char(String='Número de Pasaporte', size = 30, index=True)
    pass_tl = fields.Date(String='Vencimiento del Pasaporte')
    visa_us_tl = fields.Date(String='Vencimiento visa Usa')
    ff1 = fields.Char(String='Frequent Flier 1:', size = 30, index=True)
    ff2 = fields.Char(String='Frequent Flier 2:', size = 30, index=True)
    passanger_image = fields.Binary(string='Passport')
    doc_image = fields.Binary(string='DNI')
    visa_us_image = fields.Binary(string='VISA USA')
    note = fields.Text(String="Detalles especiales")
