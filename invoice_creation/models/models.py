from odoo import models, fields, api


class InvoiceCreation(models.Model):
    _inherit = 'stock.picking'

    invoice_count = fields.Integer(compute='_compute_invoice_count', string='Invoices')

    def _compute_invoice_count(self):
        for picking in self:
            picking.invoice_count = self.env['account.move'].search_count([('invoice_origin', '=', picking.name)])

    def action_view_invoices(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'domain': [('invoice_origin', '=', self.name)]
        }

    def create_invoice(self):
        invoice_vals = {
            'move_type': 'out_invoice',
            'invoice_origin': self.name,
            'partner_id': self.partner_id.id,
            'invoice_date': self.scheduled_date,
            'delivery_date': self.scheduled_date,
            'ref': self.name,
            'invoice_line_ids': [],
        }
        for move in self.move_ids_without_package:
            invoice_line_vals = {
                'product_id': move.product_id.id,
                'quantity': move.product_uom_qty,
                'price_unit': move.product_id.lst_price,
                'name': move.product_id.name,
            }
            invoice_vals['invoice_line_ids'].append((0, 0, invoice_line_vals))

        invoice = self.env['account.move'].create(invoice_vals)


class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_count = fields.Integer(compute='_compute_delivery_count', string='Deliveries')

    @api.depends('invoice_origin')
    def _compute_delivery_count(self):
        for move in self:
            move.delivery_count = self.env['stock.picking'].search_count([('name', '=', move.invoice_origin)])

    def action_view_deliveries(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Deliveries',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('name', '=', self.invoice_origin)],
        }
