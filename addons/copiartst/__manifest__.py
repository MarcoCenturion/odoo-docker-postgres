# -*- coding: utf-8 -*-
{
    'name': "copiar_tst",

    'summary': """
    Previous to this process, the user must cut and paste the content of the TST from Amadeus Selling Platform
    and then paste in this module.
    Then, the app will take the data and paste it into the sale.order.
    """,

    'description': """ 
        This Module will take the variables of the clipboard and paste into the sales.form 
        to do quality tasks, closing forms to the final user.
        Taking LAST TICKET DAY, fare, taxs, baggage allowance, rate. etc.
        Like this Example:
            ---
            Cía Emisora ('', 'IB')
            Ruta IGU ['XSAO IB', ' BCN IB', 'XSAO IB', ' IGU LA'] 
            Ultimo día para emitir DTE 16SEP22 
            Equipaje ['1P', '1P', '1P', '1P'] 
            A recuperar en AFIP ARS ('65038.50', 'Q1') por pasajero
            Total c/tax 292300.5
            ---
        """,

    'author': "TH Consultora",
    'website': "www.thconsultora.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Travel','Process Automation'
    'version': '1.0',

    # any module necessary for this one to work correctly
    #'depends': ['base','sale','sale_management'], 
    'depends': ['base'], 
    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/copiartst_security.xml',
        'views/views.xml',
        'views/templates.xml',
        #'views/view_line.xml',
        'report/export_tst.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
       'demo/demo.xml',
    ],
}
