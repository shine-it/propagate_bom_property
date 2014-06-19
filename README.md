Propagate BOM property
======================

OpenERP custom module to provide extra functionality on BOM property

The orginal BOM property can only work with the product BOM itself or another
word, first level of a BOM.

This module will allow the BOM property propagate through the BOM structure
in the process of BOM exploading. Thus, the BOM property set on the
componenent BOM can also be checked to decide which BOM to use for a componenent.

*Known Issue:*
This module will not propage BOM property if BOM type is "phantom", this is due to a bug in Odoo/OpenERP.

Eventually, this moudle shouldn't have been existed. The bug fix for the above issue and this module should merge into the core.

*TODO:* show examples


