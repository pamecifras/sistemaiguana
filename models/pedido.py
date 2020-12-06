# -*- coding: utf-8 -*-

from odoo import models, fields, api 

class Pedido(models.Model):
     _name = 'pedido.boleta'
     
     name = fields.Char(string = "Nombre", required = True)
     
     total = fields.Integer(string = "Total", required = True)
     subtotal = fields.Integer(string = "Subtotal")
     