from odoo import models, fields

class ProductProduct(models.Model):
    _inherit = 'product.product'

    external_match_ids = fields.One2many('product.match.mapping', 'product_id', string='External Matches')
    moombs_brand = fields.Char(string='Brand')
    moombs_category = fields.Char(string='Moombs Category')
    moombs_color = fields.Char(string='Color')
    moombs_size = fields.Char(string='Size')

    def action_view_matches(self):
        self.ensure_one()
        return {
            'name': 'Product Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'product.match.mapping',
            'view_mode': 'tree,form',
            'domain': [('product_id', '=', self.id)]
        }