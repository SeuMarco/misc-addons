# -*- coding: utf-8 -*-
from odoo import models


class CrmPhonecall(models.Model):
    _name = 'crm.phonecall'
    _inherit = ['crm.phonecall', 'reminder']
