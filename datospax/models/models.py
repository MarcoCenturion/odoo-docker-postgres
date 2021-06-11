# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaxData(models.Model):
	_name = 'pax.data'
	_description = 'Aditional Passanger Data'
	#_inherit = 'res.partner'
	apellidos_pax = fields.Char(String='Apellidos', required=True, size = 100)
	nombres_pax = fields.Char(String='Nombres', required=True, size = 100)
	dni = fields.Char(String='Número de DNI', size = 30)
	pasaporte = fields.Char(String='Número de Pasaporte', size = 30)
	vto_pass = fields.Date(String='Vencimiento del Pasaporte')
	imagen_pass = fields.Binary(string='JPG de pasaporte no mayor a 2M')
	imagen_dni = fields.Binary(string='JPG de DNI no mayor a 2M')
	pasajero = fields.Many2many('res.partner', string='Pasajero')