#-*- coding: utf-8 -*-

import re
from odoo import models, fields, api

class Copiatst(models.Model):
	_name = 'copia.tst'
	_description = 'Captura los datos del TST. copia en un objeto'

	@api.depends('tst_amadeus') # Origen de la ruta
	def _orig(self):
		if self.tst_amadeus:
			self.orig=re.findall('\n (\w{3})\n', self.tst_amadeus)[0]

	@api.depends('tst_amadeus') # Ruta sin parcear
	def _route(self):
		if self.tst_amadeus:
			self.route=re.findall('\n \w{3}\v \w{3} \w{2}\n\w|\n([ |X]\w{3} ..)', self.tst_amadeus)
'''
    tramo=[]
    contador = len(route)
    for renglon in route:
        vuelo = renglon[5:12]
        fecha = renglon[14:20]
        orides = renglon[22:29]
        horarios = renglon[34:44]
        tramo.append(vuelo+fecha+orides+horarios)
        contador = contador-1 
    tramos="\n".join(tramo)
'''

    @api.depends('tst_amadeus') # Tarifa en Pesos
	def _fare_ars(self):
		if self.tst_amadeus:
			self.fare_ars=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', self.tst_amadeus)[0]

	@api.depends('tst_amadeus') # Total tarifa + tax en ARS
	def _ttl(self):
		if self.tst_amadeus:
			self.ttl=re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', self.tst_amadeus)[-1][-1]

	@api.depends('tst_amadeus') # Tarifa en USD
	def _fare_usd(self):
		if self.tst_amadeus:
			self.fare_usd=re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', self.tst_amadeus)[0]

	@api.depends('tst_amadeus') # No me acuerdo que carajo es esta variable
	def _date(self):
		if self.tst_amadeus:
			self.date=re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', self.tst_amadeus)

	@api.depends('tst_amadeus') # Retención AFIP por Pax Q1
	def _retenc(self):
		if self.tst_amadeus:
			self.retenc=re.findall('(\d{1,6}.\d{2})(Q1|-Q1)', self.tst_amadeus)[0]

	@api.depends('tst_amadeus') # Last Tkt Date con Hora máxima para emitir
	def _ltd(self):
		if self.tst_amadeus:
			self.ltd=re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', self.tst_amadeus)[0]

	@api.depends('tst_amadeus') # Equipaje despachado en Bodeba
	def _bagage(self):
		if self.tst_amadeus:
			self.bagage=re.findall('(0P|20|30|32|2B|PC|1P|2P|3P)\n', self.tst_amadeus)

	@api.depends('tst_amadeus') # Cía emisora del tkt
	def _cia(self):
		if self.tst_amadeus:
			#self.cia=re.findall('BG CXR: (..) |CARRIER (..)', self.tst_amadeus)[0]			
			self.cia=''.join(re.findall('BG CXR: (..) |CARRIER (..)', self.tst_amadeus)[0])

	@api.depends('tst_amadeus') # Tipo de Cambio
	def _rate(self):
		if self.tst_amadeus:
			self.rate=re.findall(r'1USD=(......)', self.tst_amadeus)[0]
		
	tst_amadeus = fields.Text('Copia del tst')
	orig = fields.Char('Origen', compute='_orig', store=True)
	route = fields.Char('Destinos', compute='tramos', store=True)
	date = fields.Char('Fechas ida/vuelta', compute='_date', store=True)
	fare_ars = fields.Char('Tarifas ARS', compute='_fare_ars', store=True)
	ttl = fields.Char('Total ARS', compute='_ttl', store=True)
	fare_usd = fields.Char('Tarifa USD', compute='_fare_usd', store=True)
	retenc = fields.Char('Retenc. AFIP 35%', compute='_retenc', store=True)
	ltd = fields.Char('Max dia/hora emisión', compute='_ltd', store=True)
	bagage = fields.Char('Equip. en bodega', compute='_bagage', store=True)
	cia = fields.Char('Cía Aérea', compute='_cia', store=True)
	rate = fields.Char('Cambio Amadeus', compute='_rate', store=True)
	line_air = fields.Many2many('sale.order','order_line', 'Agregar Vuelos')
