# -*- coding: utf-8 -*-
{
    'name': "datos_pax",

    'summary': """
        Aditional data to make air reservations""",

    'description': """
        This module keep the data to make safe PNR's in the GDS's
        making secure and more eficient travel agencies
        We store the correct name os Passangers with documents, passport, 
        the expritation date, and an jpg
        In the version 2.0 will do a cron job to send alert when this time come
    """,

    'author': "TH Consultora",
    'website': "www.thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/pax_security.xml',
        'views/templates.xml',
        'views/data_view.xml',
        'wizard/campos_pnr.xml',
        #'report/export_pnr_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
