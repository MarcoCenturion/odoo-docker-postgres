# -*- coding: utf-8 -*-
{
    'name': "pasajeros",

    'summary': """
        Datos necesarios para convertir los contactos en pasajeros
        Dni, pasaporte, vencimiento, pasajero frecuente, etc
    'description': """
        This module was created to add pax data to the res.partner  
        - Personal data like passports, documents, vacinations, etc. 
        - Seat preferencies, meal pref. frequent flyer clubs, etc. 
        - Time limit of passports, visas, vac, etc.
        - Automatic taking this data from ODOO to the PNR in Amadeus or Sabre.I
        """,

    'author': "Turismo y Hotelería Consultora",
    'website': "https://thconsultora.com.ar",

    'category': 'Travel',
    'version': '1.0',

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
