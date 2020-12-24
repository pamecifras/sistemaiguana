# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoPago(models.Model):
    _name = 'pedido.tipo_pago'

    name = fields.Char(string = "Tipo de Pago")


class Pedido(models.Model):
    _name = 'pedido.boleta'

    name = fields.Char(string = "Nombre Cliente", required = True)
    fecha = fields.Date("Fecha Venta", required = True)

    tipo_pago_id = fields.Many2one(
        'pedido.tipo_pago', string = "Tipo de Pago", required = True)

    detalle_boleta_ids = fields.One2many(
        'pedido.detalle_boleta', 'boleta_id')


class DetallePedido(models.Model):
    _name = 'pedido.detalle_boleta'

    producto_id = fields.Many2one('catastro.producto', string = "Orden", required = True)
    cantidad = fields.Integer(default = 1, required = True)
    precio = fields.Integer(required = True)
    subtotal = fields.Integer(string = "Subtotal", compute = "_sub_total")
    boleta_id = fields.Many2one('pedido.boleta', string = "Boleta ID")
    
    @api.one
    def _sub_total(self):
        self.subtotal = (self.cantidad * self.precio)

        