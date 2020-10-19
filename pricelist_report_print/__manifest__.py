# -*- coding: utf-8 -*-
{
    'name': 'Print Pricelist Report',
    'summary': "Add action print in Odoo 13 Pricelists with Eng and Ita localization",

    'author': "Roberto Zanardo",
    'website': "https://www.robertozanardo.com",

    'category': 'Pricelist',
    'version': '1.1',
    'depends': ['web', 'product'],
    "data": [
        'reports/report.xml',
        'reports/report_template.xml',
    ],

    'images': ['static/description/icon.png'],

    'license ': 'LGPL-3',

    'qweb': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'currency': 'EUR',
}
