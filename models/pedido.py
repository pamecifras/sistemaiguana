# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TipoPago(models.Model):
    _name = 'pedido.tipo_pago'

    name = fields.Char(string = "Tipo de Pago")


class Pedido(models.Model):
    _name = 'pedido.boleta'

    name = fields.Char(string = "Nombre Cliente", required = True)
    fecha = fields.Date("Fecha Venta")
    total = fields.Float(default = 0)

    tipo_pago_id = fields.Many2one(
        'pedido.tipo_pago', string = "Tipo de Pago")

    detalle_boleta_ids = fields.One2many(
        'pedido.detalle_boleta', 'boleta_id')


class DetallePedido(models.Model):
    _name = 'pedido.detalle_boleta'

    producto_id = fields.Many2one('catastro.producto', string = "Orden")
    cantidad = fields.Integer()
    precio = fields.Integer()
    total = fields.Integer(string = "Total", compute = "_total")
    boleta_id = fields.Many2one('pedido.boleta')
    
    @api.one
    def _total(self):
        self.total = (self.cantidad * self.precio)
        
        