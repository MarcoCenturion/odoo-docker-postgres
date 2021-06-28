# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PaxData(models.Model):
	_name = 'pax.data'
	_description = 'Aditional Passanger Data'
	
	apellidos_pax = fields.Char(String='Apellidos', required=True, size = 100, select=True)
	nombres_pax = fields.Char(String='Nombres', required=True, size = 100, select=True)
	fecha_nacimiento = fields.Date(String='Fecha de Nacimiento')
	dni = fields.Char(String='Número de DNI', size = 30, select=True)
	pasaporte = fields.Char(String='Número de Pasaporte', size = 30)
	vto_pass = fields.Date(String='Vencimiento del Pasaporte')
	vto_visa_usa = fields.Date(String='Vencimiento visa Usa')
	imagen_pass = fields.Binary(string='Passport')
	imagen_dni = fields.Binary(string='DNI')
	imagen_visa_usa = fields.Binary(string='VISA USA')
	pasajero = fields.Many2many('res.partner', string='Pasajero')
	nota = fields.Text(String="Detalles especiales")
