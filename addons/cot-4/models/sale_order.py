from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    tst_content = fields.Text(string='TST Content')

    def agregar_lineas_desde_tst(self):
        lineas, franquicia = self.procesar_tst(self.tst_content)

        # Ejemplo de cómo agregar los renglones
        for cia, datos in lineas.items():
            # Renglón contable
            self.order_line.create({
                'order_id': self.id,
                'product_id': self.env['product.product'].search([('name', '=', "Cia" + cia)]).id,
                'purchase_price': datos['costo'],
                'price_unit': datos['venta'],
            })
            
            # Renglón no contable
            tramos = "Tramos Placeholder"  # Ajusta según sea necesario
            self.order_line.create({
                'order_id': self.id,
                'product_id': self.env['product.product'].search([('name', '=', "Cia" + cia + "Ruta" + tramos + "Franquicia" + franquicia[cia])]).id,
                'name': "Cía" + cia + " Ruta " + tramos + " Franquicia " + franquicia[cia],
            })

    def procesar_tst(self, tst_content):
        # Aquí va la lógica para procesar el contenido TST y devolver un diccionario
        lineas = {}  # Implementar la lógica para extraer datos contables
        franquicia = {}  # Implementar la lógica para extraer datos no contables
        # Lógica para procesar tst_content y llenar `lineas` y `franquicia`
        return lineas, franquicia

