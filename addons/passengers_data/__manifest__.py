# -*- coding: utf-8 -*-
{
    'name': "Passenger data for travel agencies and tour operators",

    'summary': """
    Aditional data for normal flows, admin, sales, marketing, etc.
    """,

    'description': """
        Save passenger data to the travel industry
    """,

    'author': "Marco Centurion",
    'website': "https://www.thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/passengers.xml',
    ],
}
