# cotizador_amadeus/wizards/pegar_tst.py
from odoo import models, fields, api

class WizardPegarTST(models.TransientModel):
    _name = 'wizard.pegar.tst'
    _description = 'Wizard para Pegar TST'

    tst_content = fields.Text(string="TST Content", required=True)

    def action_procesar(self):
        sale_order_id = self.env.context.get('active_id')
        sale_order = self.env['sale.order'].browse(sale_order_id)
        sale_order.tst_content = self.tst_content
        sale_order.agregar_lineas_desde_tst()

