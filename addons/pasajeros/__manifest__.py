# -*- coding: utf-8 -*-
{
    'name': "pasajeros",

    'summary': """
        Datos necesarios para convertir los contactos en pasajeros
        Dni, pasaporte, vencimiento, pasajero frecuente, etc
    'description': """
        Este módulo está diseñado para agregar datos que serán imprescindibles para la gestión personal de los pasajeros
        - Datos personales para viajes -pasaportes, documentos, carnets, vacunas-
        - Datos comerciales preferencias, club de millaje, 
        - Vencimientos de pasaportes, visas, tarjetas de crédito, vacunaciones
        - Contactos para agregar automaticamente en los PNRS y files
    """,

    'author': "Turismo y Hotelería Consultora",
    'website': "https://thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel',
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
