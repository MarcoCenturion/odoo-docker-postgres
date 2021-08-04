#-*- coding: utf-8 -*-

import re
from odoo import models, fields, api

class Copiatst(models.Model):
	_name = 'copia.tst'
	_description = 'Captura los datos del TST'
	

	@api.depends('tst_amadeus')
	def _orig(self):
		if self.tst_amadeus:
			self.orig=re.findall('\n (\w{3})\n', self.tst_amadeus)[0]


	@api.depends('tst_amadeus')
	def _route(self):
		if self.tst_amadeus:
			self.route=re.findall('\n \w{3}\v \w{3} \w{2}\n\w|\n([ |X]\w{3} ..)', self.tst_amadeus)


	@api.depends('tst_amadeus')
	def _fare_ars(self):
		if self.tst_amadeus:
			self.fare_ars=re.findall('\nARS(\D{0,3}\d{1,6}.\d{2})', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _ttl(self):
		if self.tst_amadeus:
			self.ttl=re.findall('\n(ARS|AR|ARS )(\d{1,7}.\d{2})', self.tst_amadeus)[-1][-1]

	@api.depends('tst_amadeus')
	def _fare_usd(self):
		if self.tst_amadeus:
			self.fare_usd=re.findall('USD(\D{0,6}\d{1,6}.\d{2}) ', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _date(self):
		if self.tst_amadeus:
			self.date=re.findall(r'(?:[ |*][A-Z]{1}.)((?:\d{2}\D{3} ))', self.tst_amadeus)

	@api.depends('tst_amadeus')
	def _retenc(self):
		if self.tst_amadeus:
			self.retenc=re.findall('(\d{1,6}.\d{2})-Q1', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _ltd(self):
		if self.tst_amadeus:
			self.ltd=re.findall('(DTE \d{2}\D{3}\d{2}/\d{2}:\d{2}|DTE \d{2}\D{3}\d{2})', self.tst_amadeus)[0]

	@api.depends('tst_amadeus')
	def _bagage(self):
		if self.tst_amadeus:
			self.bagage=re.findall('(0P|20|30|32|2B|PC|1P|2P)\n', self.tst_amadeus)

	@api.depends('tst_amadeus')
	def _cia(self):
		if self.tst_amadeus:
			#self.cia=re.findall('BG CXR: (..) |CARRIER (..)', self.tst_amadeus)[0]			
			self.cia=''.join(re.findall('BG CXR: (..) |CARRIER (..)', self.tst_amadeus)[0])

	@api.depends('tst_amadeus')
	def _rate(self):
		if self.tst_amadeus:
			self.rate=re.findall(r'1USD=(......)', self.tst_amadeus)[0]
		
	tst_amadeus = fields.Text('Copia del tst')
	orig = fields.Char('Origen', compute='_orig', store=True)
	route = fields.Char('Destinos', compute='_route', store=True)
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



class SaleOrderInherit(models.Model):
	_inherit = 'sale.order'
	def _copytst(self):

		sale_order = self.env['sale.order'].search([('name', '=', '')])
		sale_order_new.write({'order_line': [(0,0, {'order_id': sale_order.id,'product_id': 1,
			'price_unit': 3000.0,'product_uom_qty': 1.0 ,'name': 'Ahora'})]})


	def _pastetst(self):
		self.ensure_one()
		vals={}
		SaleOrderLine = self.env['sale.order.line']
		disc = int(self.env['ir.config_parameter'].sudo().get_param('global.discount'))
		amount = (self.amount_untaxed + self.amount_tax) * disc / 100 
		super(ButtonDiscount, self).write({
			'global_discount_rate': disc,
			'amount_discount': amount
		})
		if self.amount_discount > 0:
			vals = {
				'sequence': 10000,
				'product_id': self.company_id.sales_discount_product.id,
				'product_uom': self.company_id.sales_discount_product.uom_id.id,
				'product_uom_qty': 1,
				'price_unit': self.amount_discount * -1,
				'name': self.company_id.sales_discount_product.name,
				'order_id': self.id,
				'tax_id': [(6, 0, self.company_id.sales_discount_product.taxes_id.ids)],
			}
		sol = SaleOrderLine.sudo().create(vals)
		return sol

	def _newtst(self):
		pass