# coding: utf-8
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'

    sale_invoice_line_limit = fields.Integer('Líneas por factura de venta', default=0, help='Define el límite deseado de líneas por factura, arrojará un aviso al pasar el límite pero no evitará que se creen mas líneas.')
    purchase_invoice_line_limit = fields.Integer('Líneas por factura de compra', default=0, help='Define el límite deseado de líneas por factura, arrojará un aviso al pasar el límite pero no evitará que se creen mas líneas.')

    @api.constrains('sale_invoice_line_limit')
    def check_sale_invoice_line_limit(self):
        if self.sale_invoice_line_limit < 0:
            raise ValidationError(u'Límite por factura de venta no puede ser menor a 0')

    @api.constrains('purchase_invoice_line_limit')
    def check_purchase_invoice_line_limit(self):
        if self.purchase_invoice_line_limit < 0:
            raise ValidationError(u'Límite por factura de compra no puede ser menor a 0')
