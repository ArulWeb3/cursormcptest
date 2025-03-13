from odoo import http
from odoo.http import request

class ProductCleansingController(http.Controller):

    @http.route('/api/v1/product_cleansing/external_data', type='json', auth='user')
    def get_external_data(self, **kwargs):
        domain = []
        if kwargs.get('source'):
            domain.append(('source', '=', kwargs['source']))
        
        records = request.env['product.external.data'].search(domain)
        return {
            'status': 'success',
            'data': [{
                'id': r.id,
                'custom_id': r.custom_id,
                'source': r.source,
                'data': r.data,
                'version': r.version
            } for r in records]
        }

    @http.route('/api/v1/product_cleansing/match', type='json', auth='user')
    def create_match(self, **kwargs):
        required = ['product_id', 'external_data_id', 'matching_score']
        if not all(kwargs.get(field) for field in required):
            return {'status': 'error', 'message': 'Missing required fields'}

        try:
            match = request.env['product.match.mapping'].create({
                'product_id': kwargs['product_id'],
                'external_data_id': kwargs['external_data_id'],
                'matching_score': kwargs['matching_score'],
                'status': 'pending'
            })
            return {
                'status': 'success',
                'data': {
                    'id': match.id,
                    'status': match.status
                }
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}