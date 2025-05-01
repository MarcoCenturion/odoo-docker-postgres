# cotizador_amadeus/models/sale_order.py
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tst_content = fields.Text(string="TST Content")
    
    def pegar_tst(self):
        return {
            'name': 'Pegar TST',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.pegar.tst',
            'view_mode': 'form',
            'target': 'new'
        }
    
    def agregar_lineas_desde_tst(self):
        lineas, franquicia = self.procesar_tst(self.tst_content)
        # Código para agregar las líneas en sale.order.line

    def procesar_tst(self, tst_content):
        # Procesar el contenido de tst_content y devolver las líneas y franquicias
        pass

