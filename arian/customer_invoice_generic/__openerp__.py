# -*- coding: utf-8 -*-
{
    'name': "Customer Invoice Generic",

    'summary': "Customer Invoice Generic",

    'description': "Customer Invoice Generic",

    'author': "Nayyab",
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
