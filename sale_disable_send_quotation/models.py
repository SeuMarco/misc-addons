# -*- coding: utf-8 -*-
from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_quotation_send(self, cr, uid, ids, context=None):
        super(SaleOrder, self).action_quotation_send(cr, uid, ids, context=context)
        return None
