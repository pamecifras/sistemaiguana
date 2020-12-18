# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoPago(models.Model):
    _name = 'pedido.tipo_pago'
    
    name = fields.Char(string="Tipo de Pago")

class Pedido(models.Model):
    _name = 'pedido.boleta'

    name = fields.Char(string="Nombre Cliente", required=True)
    orden = fields.Char(string="Orden", required=True)
    fecha = fields.Date("Fecha de venta")
    sub_total = fields.Float(default=0)
    descuento = fields.Float(default=0)
    total = fields.Float(default=0)
    
    tipo_pago_id = fields.Many2one(
        'pedido.tipo_pago', string = "Tipo de Pago")
    

    
    
    

    
