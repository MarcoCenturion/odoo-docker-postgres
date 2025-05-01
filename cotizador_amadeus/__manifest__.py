# -*- coding: utf-8 -*-
{
    'name': "Custom Air Pricer Model",
    'license': 'LGPL-3',

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Custom module created for parsing a TST and PNR to paste in the sale.order line readable for customares.


""",

    'author': "TH Consultora",
    'website': "https://www.thconsultora.com.ar/blog",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel Industry',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/wizard_views.xml', 
        'views/sale_order_views.xml',
   ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
}

