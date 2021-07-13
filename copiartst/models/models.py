#-*- coding: utf-8 -*-

import re
from odoo import models, fields, api

class Copiatst(models.Model):
	#_inherit = 'sale.order'
	_name = 'copia.tst'
	_description = 'Captura los datos del TST'
	

	@api.depends('tst_amadeus')
	def _route(self):
		if self.tst_amadeus:
			self.route=re.findall('\n[ |X]([A-Z]{3})', self.tst_amadeus)

	@api.depends('tst_amadeus')
	def _fare_ars(self):
		if self.tst_amadeus:
			self.fare_ars=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _ttl(self):
		if self.tst_amadeus:
			self.ttl=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', self.tst_amadeus)[-1]

	@api.depends('tst_amadeus')
	def _fare_usd(self):
		if self.tst_amadeus:
			self.fare_usd=re.findall('USD(\D{0,3}\d{1,6}.\d{2}) ', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _date(self):
		if self.tst_amadeus:
			self.date=re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _retenc(self):
		if self.tst_amadeus:
			self.retenc=re.findall('ARS (\D{0,3}\d{1,6}.\d{2})(-Q1|Q1)', self.tst_amadeus)[0][0]

	@api.depends('tst_amadeus')
	def _ltd(self):
		if self.tst_amadeus:
			self.ltd=str(re.findall('DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2}', self.tst_amadeus)[0]).split(' ',1)[1]

	@api.depends('tst_amadeus')
	def _bagage(self):
		if self.tst_amadeus:
			self.bagage=re.findall('(0P|20|30|32|2B|PC|1P)\n', self.tst_amadeus)

	@api.depends('tst_amadeus')
	def _cia(self):
		if self.tst_amadeus:
			self.cia=re.findall('BG CXR: (..)', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _rate(self):
		if self.tst_amadeus:
			self.rate=re.findall('RATE USED 1USD=(\d{1,4}.\d{2})', self.tst_amadeus)[0]

		
	tst_amadeus = fields.Text('Copia del tst')
	route = fields.Char('Ruta', compute='_route', store=True)
	date = fields.Char('Fecha ida y vuelta', compute='_date', store=True)
	fare_ars = fields.Float('Tarifas Pesos', compute='_fare_ars', store=True)
	ttl = fields.Float('Total en pesos', compute='_ttl', store=True)
	fare_usd = fields.Float('Tarifa USD', compute='_fare_usd', store=True)
	retenc = fields.Float('Retencion AFIP 35%', compute='_retenc', store=True)
	ltd = fields.Char('Ultimo día para emitir', compute=_ltd, store=True)
	bagage = fields.Char('Equipaje despachado', compute='_bagage', store=True)
	cia = fields.Char('Cía Aérea', compute='_cia', store=True)
	rate= fields.Float('Tipo de Cambio USD', compute='_rate', store=True)
	line_air = fields.Many2many('sale.order')


class SaleOrderInherit(models.Model):
	_inherit = 'sale.order.line'

	def _tstusd(self):
		
		pass

	def _tstars(self):
		pass
	