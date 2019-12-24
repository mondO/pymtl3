#=========================================================================
# PyMTLBehavioralTranslatorL5.py
#=========================================================================
# Author : Peitian Pan
# Date   : Dec 23, 2019
"""Provide the level 5 PyMTL translator implementation."""

from pymtl3.passes.backends.generic.behavioral.BehavioralTranslatorL5 import (
    BehavioralTranslatorL5,
)
from pymtl3.passes.rtlir import BehavioralRTLIR as bir
from pymtl3.passes.rtlir import RTLIRType as rt

from ...errors import PyMTLerilogTranslationError
from .PyMTLBehavioralTranslatorL4 import (
    BehavioralRTLIRToPyMTLVisitorL4,
    PyMTLBehavioralTranslatorL4,
)


class PyMTLBehavioralTranslatorL5(
    PyMTLBehavioralTranslatorL4, BehavioralTranslatorL5):

  def _get_rtlir2sv_visitor( s ):
    return BehavioralRTLIRToPyMTLVisitorL5

#-------------------------------------------------------------------------
# BehavioralRTLIRToPyMTLVisitorL5
#-------------------------------------------------------------------------

class BehavioralRTLIRToPyMTLVisitorL5( BehavioralRTLIRToPyMTLVisitorL4 ):
  """Visitor that translates RTLIR to PyMTL for a single upblk."""

  #-----------------------------------------------------------------------
  # visit_Attribute
  #-----------------------------------------------------------------------

  def visit_Attribute( s, node ):
    """Return the PyMTL representation of an attribute.

    Add support for subcomponent attributes in L5.
    """
    # Generate subcomponent attribute
    if isinstance( node.value.Type, rt.Component ) and\
       not isinstance( node.value, bir.Base ):

      value = s.visit( node.value )
      attr = node.attr
      s.check_res( node, attr )
      return f'{value}__{attr}'

    return super().visit_Attribute( node )

  #-----------------------------------------------------------------------
  # visit_Index
  #-----------------------------------------------------------------------

  def visit_Index( s, node ):
    if isinstance( node.value.Type, rt.Array ) and \
       isinstance( node.value.Type.get_sub_type(), rt.Component ):
      try:
        idx = node.idx._value
      except AttributeError:
        raise SVerilogTranslationError( s.blk, node,
          'index of component array must be a static constant expression!' )
      idx = int( idx )
      value = s.visit( node.value )
      return f"{value}__{idx}"

    else:
      return super().visit_Index( node )
