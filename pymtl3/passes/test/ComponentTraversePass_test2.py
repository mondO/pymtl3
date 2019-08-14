from itertools import product
from pymtl import *
from pymtl3.passes.ComponentTraversePass import ComponentTraversePass
class Circuit( Model ):

  def __init__( s ):
    s.a = InPort  (Bits(1))
    s.b = InPort  (Bits(1))
    s.ci = InPort (Bits(1))
    s.co = OutPort (Bits(1))
    s.sum = OutPort (Bits(1)) 
    s.ABxor = Wire (Bits(1)) 
    s.ABand = Wire (Bits(1))
    s.ABCand = Wire (Bits(1))
    s.marked=True

    @s.combinational
    def A_XOR_B():
        if (s.a.value and ( 1 != s.b.value))or((1!=s.a.value) and s.b.value):
             s.ABxor.value = 1
            
        else:
             s.ABxor.value = 0     
    
    @s.combinational
    def A_AND_B():
         s.ABand.value = (s.a and s.b)
  
    @s.combinational
    def AB_AND_Ci():
         s.ABCand.value = (s.ABxor.value and s.ci.value)

    @s.combinational
    def AB_XOR_Ci():
        if ((s.ABxor.value and (1!=s.ci.value))or((1!=s.ABxor.value) and s.ci.value)):
             s.sum.value = 1
        else:
             s.sum.value = 0

    @s.combinational
    def ABxor_OR_ABand():
         if (s.ABand.value or s.ABCand.value):
             s.co.value = 1
         else:
            s.co.value = 0
    

def test_all_marked():
  a = Circuit()
  a.elaborate()
  a.apply( ComponentTraversePass() )