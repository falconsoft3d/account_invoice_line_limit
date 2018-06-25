# coding: utf-8
from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    invoice_line_count = fields.Integer('Cantidad de líneas', compute='_compute_lines_count')

    @api.multi
    @api.depends('invoice_line_ids')
    def _compute_lines_count(self):
        for record in self:
            record.invoice_line_count = len(record.invoice_line_ids)

    @api.onchange('invoice_line_ids')
    def onchange_invoice_lines(self):
        if self.type == 'out_invoice' and self.env.user.company_id.sale_invoice_line_limit and self.invoice_line_count > self.env.user.company_id.sale_invoice_line_limit:
            return {
                'warning': {
                    'title': u'Aviso',
                    'message': u'Ha excedido de %d líneas para ésta factura.' % self.env.user.company_id.sale_invoice_line_limit
                }
            }
        elif self.type == 'in_invoice' and self.env.user.company_id.purchase_invoice_line_limit and self.invoice_line_count > self.env.user.company_id.purchase_invoice_line_limit:
            return {
                'warning': {
                    'title': u'Aviso',
                    'message': u'Ha excedido de %d líneas para ésta factura.' % self.env.user.company_id.purchase_invoice_line_limit
                }
            }
