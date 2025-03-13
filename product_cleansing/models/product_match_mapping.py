from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductMatchMapping(models.Model):
    _name = 'product.match.mapping'
    _description = 'Product Match Mapping'

    product_id = fields.Many2one('product.product', required=True, ondelete='cascade')
    external_data_id = fields.Many2one('product.external.data', required=True, ondelete='cascade')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('matched', 'Matched'),
        ('unmatched', 'Unmatched')
    ], default='pending', required=True)
    matching_score = fields.Integer(string='Matching Score', default=0)
    match_validated_at = fields.Datetime(string='Validation Time', readonly=True)
    validated_by = fields.Many2one('res.users', string='Validated By', readonly=True)

    @api.constrains('matching_score')
    def _check_matching_score(self):
        for record in self:
            if not (0 <= record.matching_score <= 100):
                raise ValidationError('Matching score must be between 0 and 100')