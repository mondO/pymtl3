from itertools import product
from pymtl3 import *
from SvgGenerationPass import SvgGenerationPass



class And ( Component ):
    def construct ( s ):
        s.a1 = InPort (Bits(1))
        s.b1 = InPort (Bits(1))
        s.out1 = OutPort (Bits(1))
        connect(s.a1,s.out1)
        
     

class Or ( Component ):
    def construct ( s ):
        s.a2 = InPort (Bits(1))
        s.b2 = InPort (Bits(1))
        s.out2 = OutPort (Bits(1))
        connect(s.a2,s.out2)

class Xor ( Component ):
    def construct ( s ):
        s.a3 = InPort (Bits(1))
        s.b3 = InPort (Bits(1))
        s.out3 = OutPort (Bits(1))
        connect(s.a3,s.out3)
   

class FullAdder( Component ):
    def construct( s ):
        s.marked =True
        s.a = InPort  (Bits(1))
        s.b = InPort  (Bits(1))
        s.ci = InPort (Bits(1))
        s.co = OutPort (Bits(1))
        s.sum = OutPort (Bits(1)) 
        
        s.a_xor_b = Xor()
        s.a_and_b = And()
        s.ab_and_ci = And()
        s.ab_xor_ci = Xor()
        s. abxor_or_aband = Or()

        connect(s.a,  s.a_xor_b.a3)
        connect(s.b,  s.a_xor_b.b3)
        connect(s.a,  s.a_and_b.a1)
        connect(s.b,  s.a_and_b.b1)
        connect( s.a_xor_b.out3, s.ab_and_ci.a1)
        connect( s.ci, s.ab_and_ci.b1)
        connect( s.a_xor_b.out3, s.ab_xor_ci.a3)
        connect( s.ci, s.ab_xor_ci.b3)
        connect( s.ab_and_ci.out1, s.abxor_or_aband.a2)
        connect( s.a_and_b.out1, s.abxor_or_aband.b2)
        connect(s.abxor_or_aband.out2, s.co)
        connect ( s.ab_xor_ci.out3, s.sum)

  
def test_adder():
  adder = FullAdder()
  adder.elaborate()
  adder.apply( SvgGenerationPass() )
