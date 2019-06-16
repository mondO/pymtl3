#=========================================================================
# YosysTranslator_L3_cases_test.py
#=========================================================================
"""Test the yosys-SystemVerilog translator."""

from __future__ import absolute_import, division, print_function

import pytest

from pymtl3.passes.rtlir.util.test_utility import do_test
from pymtl3.passes.sverilog.translation.test.SVTranslator_L3_cases_test import (
    test_ifc_decls,
    test_interface,
    test_interface_index,
    test_multi_ifc_decls,
)
from pymtl3.passes.yosys.translation.YosysTranslator import YosysTranslator


def trim( src ):
  lines = src.split( "\n" )
  ret = []
  for line in lines:
    if not line.startswith( "//" ):
      ret.append( line )
  return "\n".join( ret )

def local_do_test( m ):
  m.elaborate()
  tr = YosysTranslator( m )
  tr.translate( m )
  src = trim( tr.hierarchy.src )
  assert src == m._ref_src_yosys
