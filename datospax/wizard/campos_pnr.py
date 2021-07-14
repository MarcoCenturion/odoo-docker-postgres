from odoo import models, fields, api
from odoo.exceptions import UserError


class CamposPnr(models.TransientModel):
	_name='datospax.pnr.wizard'
	_description='Exportar datos de Odoo a Amadeus'

	row_1a = fields.Char(string="Renglon a pegar en 1A", )
	paxs = fields.Many2many("pax.data", 
		string="Seleccionar Pasajeros", 
		help="Click sobre los pasajeros a importar")

	def export_data(self):
'''
		export=self.env['pax.data']

		if self.surname:
			row_1a = fields.Char('NM1'+surname+'/'+name)

		return row_1a'''