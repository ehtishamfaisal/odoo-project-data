# -*- coding: utf-8 -*-
{
    'name': "Order Conformation Invoice",

    'summary': "Order Conformation Invoice",

    'description': "Order Conformation Invoice",

    'author': "Muhammmad Kamran",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report','account'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
