# -*- coding: utf-8 -*-
from odoo import http

# class Pedido(http.Controller):
#     @http.route('/pedido/pedido/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pedido/pedido/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pedido.listing', {
#             'root': '/pedido/pedido',
#             'objects': http.request.env['pedido.pedido'].search([]),
#         })

#     @http.route('/pedido/pedido/objects/<model("pedido.pedido"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pedido.object', {
#             'object': obj
#         })