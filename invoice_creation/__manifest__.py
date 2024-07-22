# -*- coding: utf-8 -*-
{
    'name': "Invoice from Picking",

    'summary': "Invoice from Picking",

    'description': """
     This module adds a functionality to create invoices directly from stock picking. 
     Create invoice from Picking
     Create invoice from stock view

    Features:
    - Adds a 'Create Invoice' button on the stock picking form view.
    - Automatically populates the invoice with details from the stock picking.


    Usage:
    - Navigate to Inventory > Operations > Transfers.
    - Open a stock picking record.
    - Click on the 'Create Invoice' button to create an invoice.
    - Review the created invoice in the Invoicing app.

    This module streamlines the workflow by reducing the manual effort required to create invoices from delivery orders, 
    ensuring accuracy and efficiency in the invoicing process.
    """,
    'author': "HAK Technologies",
    'website': "https://www.HAKTechnologies.com",
    'version': '0.1',
    'license': 'OPL-1',
    'images': ['description/icon.png'],

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'stock'],

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
