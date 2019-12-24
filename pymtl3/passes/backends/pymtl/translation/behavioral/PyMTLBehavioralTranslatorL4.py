#=========================================================================
# PyMTLBehavioralTranslatorL4.py
#=========================================================================
# Author : Peitian Pan
# Date   : Dec 23, 2019
"""Provide the level 4 PyMTL translator implementation."""

from pymtl3.passes.backends.generic.behavioral.BehavioralTranslatorL4 import (
    BehavioralTranslatorL4,
)
from pymtl3.passes.rtlir import RTLIRType as rt

from ...errors import PyMTLerilogTranslationError
from .PyMTLBehavioralTranslatorL3 import (
    BehavioralRTLIRToPyMTLVisitorL3,
    PyMTLBehavioralTranslatorL3,
)


class PyMTLBehavioralTranslatorL4(
    PyMTLBehavioralTranslatorL3, BehavioralTranslatorL4):

  def _get_rtlir2sv_visitor( s ):
    return BehavioralRTLIRToPyMTLVisitorL4

#-------------------------------------------------------------------------
# BehavioralRTLIRToPyMTLVisitorL4
#-------------------------------------------------------------------------

class BehavioralRTLIRToPyMTLVisitorL4( BehavioralRTLIRToPyMTLVisitorL3 ):
  """Visitor that translates RTLIR to PyMTL for a single upblk."""

  #-----------------------------------------------------------------------
  # visit_Attribute
  #-----------------------------------------------------------------------

  def visit_Attribute( s, node ):
    """Return the PyMTL representation of an attribute.

    Add support for interface attributes in L4. We just name mangle every
    signal in an interface instead of constructing a PyMTL interface
    and instantiating new interfaces from it.
    """
    if isinstance( node.value.Type, rt.InterfaceView ):
      value = s.visit( node.value )
      attr = node.attr
      s.check_res( node, attr )
      return f'{value}__{attr}'
    else:
      return super().visit_Attribute( node )

  #-----------------------------------------------------------------------
  # visit_Index
  #-----------------------------------------------------------------------

  def visit_Index( s, node ):
    if isinstance( node.value.Type, rt.Array ) and \
        isinstance( node.value.Type.get_sub_type(), rt.InterfaceView ):
      try:
        nbits = node.idx._value
      except AttributeError:
        raise SVerilogTranslationError( s.blk, node,
          f'index of interface array {node.idx} must be a static constant expression!' )
      idx = int( nbits )
      value = s.visit( node.value )
      return f'{value}__{idx}'

    else:
      return super().visit_Index( node )
