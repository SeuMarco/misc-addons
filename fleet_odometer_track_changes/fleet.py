# -*- coding: utf-8 -*-
from odoo import fields, models


class FleetVehicle(models.Model):

    _inherit = 'fleet.vehicle'

    def _get_odometer(self, cr, uid, ids, odometer_id, arg, context):
        res = super(FleetVehicle, self)._get_odometer(cr, uid, ids, odometer_id, arg, context)
        return res

    def _set_odometer(self, cr, uid, id, name, value, args=None, context=None):
        res = super(FleetVehicle, self)._set_odometer(cr, uid, id, name, value, args, context)
        return res


    odometer = fields.Float(compute="_get_odometer", fnct_inv=_set_odometer, string='Last Odometer'
                                    help='Odometer measure of the vehicle at the moment of this log',
                                    track_visibility='onchange'),

