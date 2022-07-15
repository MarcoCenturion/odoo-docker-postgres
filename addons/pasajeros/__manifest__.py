# -*- coding: utf-8 -*-
{
    'name': "pasajeros",

    'summary': """
        Datos necesarios para convertir los contactos en pasajeros
        Dni, pasaporte, vencimiento, pasajero frecuente, etc
    'description': """
        Long description of module's purpose
    """,

    'author': "Turismo y Hotelería Consultora",
    'website': "https://thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','res.partner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
