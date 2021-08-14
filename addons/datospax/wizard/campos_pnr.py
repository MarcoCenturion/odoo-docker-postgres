from odoo import models, fields, api
from odoo.exceptions import UserError


class CamposPnr(models.TransientModel):
	_name='datospax.pnr.wizard'
	_description='Exportar datos de Odoo a Amadeus'


	buscar = fields.Char(string="indicar el apellido del pasajero", )
	paxs = fields.Many2many("pax.data", 
		string="Seleccionar Pasajeros", 
		help="Click sobre los pasajeros a importar")

	def export_data(self):
		domain=['surname', '!=', self.pax.data(surname(' ')) ]

		pax=self.env['pax.data']
		
		if self.pax.data:
			domain.append(())
			pasajero=[
			'surname',
			'name',
			'passport',
			'private_email',
			'private_cel_phone',
			]
		pax_records=pax.data.search_read(domain.pasajero)
		data={
		'pax_records':pax_records,
		}
		return self.env.ref('data.pax_renglon_a_amadeus').report_action(self, data=data)
