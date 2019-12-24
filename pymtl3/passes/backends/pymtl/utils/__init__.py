#=========================================================================
# utility.py
#=========================================================================
# Author : Peitian Pan
# Date   : Dec 23, 2019
"""Provide helper methods that might be useful to pymtl backend passes."""

from keyword import kwlist

pymtl_keyword = kwlist + [
    # PyMTL3 DSL keywords?
    # 'InPort', 'OutPort', 'Wire', 'Interface', 'Component',
    # 'connect',
    # 'Bits1', 'Bits2', 'Bits8', 'Bits16', 'Bits32',
]

pymtl_reserved = set( pymtl_keyword )
