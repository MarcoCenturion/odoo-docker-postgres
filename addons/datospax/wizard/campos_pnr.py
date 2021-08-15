from odoo import models, fields, api
from odoo.exceptions import UserError


class CamposPnr(models.TransientModel):
	_name='pnr.wizard'
	_description='Exportar datos de Odoo a Amadeus'


	buscar = fields.Char(string="indicar el apellido del pasajero", )
	paxs = fields.Many2many("pax.data", 
		string="Seleccionar Pasajeros", 
		help="Click sobre los pasajeros a importar")

	def export_data(self):
		data = {"ids": self.ids,"model": "datos.pax","form": self.read()[0],}
		return self.env.ref("datospax.view_pax_export_amadeus")