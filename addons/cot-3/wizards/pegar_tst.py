from odoo import models, fields, api

class TSTWizard(models.TransientModel):
    _name = 'tst.wizard'
    _description = 'Wizard para pegar TST'

    tst_content = fields.Text(string='Pegar TST')

    def pegar_tst(self):
        sale_order = self.env['sale.order'].browse(self._context.get('active_id'))
        sale_order.tst_content = self.tst_content
        sale_order.agregar_lineas_desde_tst()

