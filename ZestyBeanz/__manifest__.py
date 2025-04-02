
{
    'name': 'ZestyBeanz',
    'version': '1.0',
    'category': 'Learning',
    'sequence': 100,
    'summary': 'This is for Training Odoo',
    'description': """Learning The Odoo Framework""",
    'website': 'https://www.zbeanztech.com/',
    'depends': ['sale','sale_management','account','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/food_view.xml'
        
    ],
    
    'application': True,
    'license': 'LGPL-3',
}

