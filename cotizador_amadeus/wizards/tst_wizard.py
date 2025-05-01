from odoo import models, fields, api
import re, datarime

class TSTWizard(models.TransientModel):
    _name = 'tst.wizard'
    _description = 'Wizard para procesar contenido TST'

    tst_content = fields.Text(string='Contenido TST')

    @api.model
    def default_get(self, fields):
        res = super(TSTWizard, self).default_get(fields)
        sale_order_id = self.env.context.get('active_id')
        res['sale_order_id'] = sale_order_id
        return res

    sale_order_id = fields.Many2one('sale.order', string='Orden de Venta', readonly=True)

    def procesar_tst_y_agregar_lineas(self):
        sale_order = self.env['sale.order'].browse(self.sale_order_id.id)
        sale_order.write({'tst_content': self.tst_content})
        sale_order.agregar_lineas_desde_tst()

    def process_tst_content(self):
        sale_order = self.env['sale.order'].browse(self.env.context.get('active_id'))
        if sale_order:
            sale_order.write({'tst_content': self.tst_content})
            sale_order.agregar_lineas_desde_tst()
