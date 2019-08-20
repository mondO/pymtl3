from itertools import product
from pymtl3 import *
from pymtl3.passes.SvgGenerationPass import SvgGenerationPass

class C( Component ):
  def construct( s, marked = True ):
    if marked:
      s.marked = True

class B( Component ):
  def construct( s, marked = True, marked_c = True ):
    if marked:
      s.marked = True
    s.all_cs = [ C(marked_c) for _ in range(5) ]

class A( Component ):
  def construct( s, marked = True, marked_b = True, marked_c = True ):
    if marked:
      s.marked = True
    s.all_bs = [ B(marked_b, marked_c) for _ in range(2) ]

def test_all_marked():
  a = A()
  a.elaborate()
  a.apply( SvgGenerationPass() )

def test_not_marked():
  a = A()
  a.elaborate()
  a.apply( SvgGenerationPass() )
