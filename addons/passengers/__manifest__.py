# -*- coding: utf-8 -*-
{
    'name': "passengers",

    'summary': """
        Datos necesarios para convertir los contactos en pasajeros
        Dni, pasaporte, vencimiento, pasajero frecuente, etc
    'description': """
        """,

    'author': "Turismo y Hotelería Consultora",
    'website': "https://thconsultora.com.ar",

    'category': 'Travel Agencies and Tour Operator',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','res.partner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/passengers.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        ],
}
