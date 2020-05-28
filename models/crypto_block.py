from odoo import fields, models

class Block(models.Model):
    _name = 'crypto.block'
    _description = 'Block'

    keypair_name = fields.Char('Name', required=True)
    keypair_path = fields.Char()
    active = fields.Boolean('Active?', default=True)
    date_generated = fields.Date()
    #chosen_file = fields.Many2one('crypto.block', 'keypair_name', string="Choose file for sign")
