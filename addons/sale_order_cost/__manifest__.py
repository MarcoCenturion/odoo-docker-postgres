# -*- coding: utf-8 -*-
{
    'name': "sale_order_cost",

    'summary': """
        This module add an extra function on the form sale order with 
        the cost or cost of the file
        """,

    'description': """
    Details: 
      - Add lines with cost and taxes
      - Sum all of the producto an carry this to one line in sale_order front
      - This line will show to the user all the many products offered to the customare  
    """,

    'author': "Marco Centurion",
    'website': "https://www.thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel and leisure',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order_cost_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
