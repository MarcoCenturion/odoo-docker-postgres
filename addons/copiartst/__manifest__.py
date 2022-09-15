# -*- coding: utf-8 -*-
{
    'name': "copiar_tst",

    'summary': """
    app to paste the TST into the FILE.
    """

    'description': """ 
        This Module will take the variables of the clipboard and paste into the sales.form 
        to do quality tasks, closing forms to the final user.
        Taking LAST TICKET DAY, fare, taxs, baggage allowance, rate. etc.

    """,

    'author': "TH Consultora",
    'website': "thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tarvel','Automatización de procesos'
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sale_management'], 

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/copiartst_security.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/view_line.xml',
        'report/export_tst.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
       'demo/demo.xml',
    ],
    }
