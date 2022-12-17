# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Component Creator',
    'version': '1.0.0',
    'category': 'Component',
    'summary': 'A simple component creator',
    'description': """Component Creator is a simple Master Component creator that
                   helps user to create components and define the desired processing
                   time from scratch. 
                   """,
    'depends': [],
    'sequence': -100,
    'data': [
        'views/menu.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}
