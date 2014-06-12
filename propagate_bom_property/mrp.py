# -*- coding:utf-8 -*-
##############################################################################
#
#    propagate_bom_property module for OpenERP, Propagate BOM Property
#    Copyright (C) 2010 Shine IT (<http://www.openerp.cn>) contact@openerp.cn
#
#    This file is a part of multi_level_bom_property
#
#    propagate_bom_property is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    propagate_bom_property is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import osv

class MRP_Production(osv.Model):
    _inherit = 'mrp.production'

    def _hook_create_post_procurement(self, cr, uid, production, procurement_id, context=None):
        context = context or {}
        super(MRP_Production, self)._hook_create_post_procurement(cr, uid,
                production, procurement_id, context)
        procurement_obj = self.pool.get('procurement.order')
        proc_id = procurement_obj.search(cr, uid,
                [('production_id','=',production.id)], context=context)
        if proc_id:
            procurement = procurement_obj.browse(cr, uid, proc_id[0])
            if procurement.property_ids:
                property_ids = [property.id for property in procurement.property_ids]
                procurement_obj.write(cr, uid, procurement_id, {'property_ids':
                    [(6,0,property_ids)]}, context=context)

