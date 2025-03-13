{
    'name': 'Product Data Cleansing and Enrichment',
    'version': '18.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Product data cleansing, matching, and enrichment module',
    'description': '''
Product Data Cleansing and Enrichment Module
==========================================

This module provides functionality for:
- External product data management
- Product matching and validation
- Data enrichment from external sources
- Match scoring and validation workflow
''',
    'author': 'Arul',
    'website': 'https://github.com/ArulWeb3',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/product_matching_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}