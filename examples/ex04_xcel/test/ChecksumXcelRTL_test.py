"""
==========================================================================
 ChecksumXcelRTL_test.py
==========================================================================
Test cases for RTL checksum accelerator.

Author : Yanghui Ou
  Date : June 14, 2019
"""
from __future__ import absolute_import, division, print_function

from pymtl3 import *

from .ChecksumXcelCL_test import mk_xcel_transaction
from ..ChecksumXcelRTL import ChecksumXcelRTL

#-------------------------------------------------------------------------
# Wrap Xcel into a function
#-------------------------------------------------------------------------
# [checksum_xcel_rtl] creates an RTL checksum accelerator, feeds in the
# input, ticks it, gets the response, and returns the result.

def checksum_rtl( words ):
  assert len(words) == 8

  # Create a simulator using RTL accelerator
  dut = ChecksumXcelRTL()
  dut.elaborate()
  dut.apply( SimulationPass )
  dut.sim_reset()
  
  reqs, _ = mk_xcel_transaction( words )

  for req in reqs:

    # Wait until xcel is ready to accept a request
    dut.xcel.resp.rdy = b1(1)
    while not dut.req.rdy:
      dut.xcel.req.en   = b1(0)
      dut.tick()
    
    # Send a request
    dut.xcel.req.en  = b1(1)
    dut.xcel.req.msg = req
    dut.tick()
   
    # Wait for response
    while not dut.resp.en:
      dut.xcel.req.en   = b1(0)
      dut.tick()
    
    # Get the response message
    resp_msg = dut.resp.msg
    dut.tick()

  return resp_msg.datas

#-------------------------------------------------------------------------
# Src/sink based tests
#-------------------------------------------------------------------------
# Here we directly reuse all test cases in ChecksumXcelCL_test. We only
# need to provide a different DutType in the setup_class.

from .ChecksumXcelCL_test import ChecksumXcelCLSrcSink_Tests as BaseTests

class ChecksumXcelRTLSrcSink_Tests( BaseTests ):

  @classmethod
  def setup_class( cls ):
    cls.DutType = ChecksumXcelRTL
