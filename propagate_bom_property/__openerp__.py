# -*- encoding: utf-8 -*-
##############################################################################
#
#    propagate_bom_property module for OpenERP, Propagate BOM Property
#    Copyright (C) 2014 Shine IT (<http://www.openerp.cn>) contact@openerp.cn
#
#    This file is a part of propagate_bom_property
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

{
    'name': 'Propagate BOM Property',
    'version': '1.0',
    'category': 'MRP',
    'description': """
    The orginal BOM property can only work with the product BOM itself or another
    word, first level of a BOM.

    This module will allow the BOM property propagate through the BOM structure
    in the process of BOM exploading. Thus, the BOM property set on the
    componenent BOM can also be checked to decide which BOM to use for a componenent.

    TODO: show examples
    """,
    'author': 'Shine IT',
    'depends': ['sale_mrp'],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
