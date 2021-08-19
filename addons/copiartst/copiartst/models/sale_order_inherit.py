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
                'product_uom': self.company_id.sales_discount_product.uom_id.id,
                #'product_uom': self.company_id.sales_discount_product.uom_id,
                'product_uom_qty': 1,
                'price_unit': self.amount_discount * -1,
                'name': self.company_id.sales_discount_product.name,
                'order_id': self.id,
                'tax_id': [(6, 0, self.company_id.sales_discount_product.taxes_id.ids)],
            }
        sol = SaleOrderLine.sudo().create(vals)
        return sol