from odoo import models, fields, api
from odoo.exceptions import UserError


class CamposPnr(models.TransientModel):
	_name='datospax.pnr.wizard'
	_description='Exportar datos de Odoo a Amadeus'

	buscar = fields.Char(string="indicar el apellido del pasajero", )
	paxs = fields.Many2many("pax.data", 
		string="Seleccionar Pasajeros", 
		help="Click sobre los pasajeros a importar")

	def exporta_data(self):
		print('Todo bien')
		return True