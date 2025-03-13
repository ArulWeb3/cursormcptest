import uuid
from odoo import models, fields, api

class ProductExternalData(models.Model):
    _name = 'product.external.data'
    _description = 'External Product Data'
    _order = 'timestamp DESC'

    custom_id = fields.Char(string='Custom ID', required=True, readonly=True, index=True, default=lambda self: str(uuid.uuid4()))
    source = fields.Char(string='Source', required=True, help='Source of the external data')
    data = fields.Json(string='Data', required=True, help='Raw external product data')
    version = fields.Integer(string='Version', default=1)
    timestamp = fields.Datetime(string='Timestamp', default=fields.Datetime.now)
    previous_version_id = fields.Char(string='Previous Version ID', readonly=True)

    _sql_constraints = [('unique_custom_id', 'unique(custom_id)', 'Custom ID must be unique!')]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('custom_id'):
                vals['custom_id'] = str(uuid.uuid4())
        return super().create(vals_list)