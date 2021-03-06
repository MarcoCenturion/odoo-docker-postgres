# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaxData(models.Model):
	_name = 'pax.data'
	_description = 'Aditional Passanger Data'
	
	surname = fields.Char(String='Passanger Surname', required=True, size = 100, index=True)
	name = fields.Char(String='Passanger Name', required=True, size = 100, index=True)
	dob = fields.Date(String='Date of Birth')
	document = fields.Char(String='Número de DNI', size = 30, index=True)
	passport = fields.Char(String='Número de Pasaporte', size = 30)
	pass_tl = fields.Date(String='Vencimiento del Pasaporte')
	visa_us_tl = fields.Date(String='Vencimiento visa Usa')
	ff1 = fields.Char(String='Frequent Flier 1:', size = 30, index=True)
	ff2 = fields.Char(String='Frequent Flier 2:', size = 30, index=True)
	private_email = fields.Char(String='Frequent Flier 1:', size = 60, index=True)
	private_cel_phone = fields.Char(String='Frequent Flier 1:', size = 30, index=True)
	passanger_image = fields.Binary(string='Passport')
	doc_image = fields.Binary(string='DNI')
	visa_us_image = fields.Binary(string='VISA USA')
	contact_relation = fields.Many2many('res.partner', string='Pasajero')
	note = fields.Text(String="Detalles especiales")
