# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    _order = 'sequence,id'

    sequence = fields.Integer('Sequence', default=0)
