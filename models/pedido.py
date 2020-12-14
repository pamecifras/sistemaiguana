# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pedido(models.Model):
    _name = 'pedido.boleta'

    name = fields.Char(string="Nombre Cliente", required=True)
    fecha = fields.Date()
    sub_total = fields.Float(default=0)
    descuento = fields.Float(default=0)
    total = fields.Float(default=0)
    
    detalle_boleta_ids = fields.One2many(
        'pedido.detalle_boleta', 'boleta_id', String ="Detalle de boleta")
    
class DetalleBoleta(models.Model):
    _name = 'pedido.detalle_boleta'
    boleta_id = fields.Many2one('pedido.boleta', String ="Boleta")
    cantidad = fields.Integer(default=1)
    precio = fields.Integer()
    sub_total = fields.Integer(string="Subtotal", compute ="_sub_total")
    total = fields.Integer(string="Total", compute ="total_")
    
    @api.one
    def _sub_total(self):
        self.sub_total= (self.cantidad * self.precio)
        
    @api.one
    def total_(self):
        self.total= (self.sub_total - ((self.descuento/100) * self.sub_total))
             
        
