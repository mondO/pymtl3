#=========================================================================
# OpenLoopCLPass.py
#=========================================================================
# Generate a simple schedule (no Mamba techniques here) based on the
# DAG generated by some previous pass.
#
# Author : Shunning Jiang
# Date   : Apr 20, 2019

from BasePass     import BasePass, PassMetadata
from collections  import deque
from graphviz     import Digraph
from errors import PassOrderError
from pymtl.dsl.errors import UpblkCyclicError
from pymtl import *

class OpenLoopCLPass( BasePass ):
  def __call__( self, top ):
    if not hasattr( top._dag, "all_constraints" ):
      raise PassOrderError( "all_constraints" )

    top._sched = PassMetadata()

    self.schedule_with_top_level_callee( top )

  def schedule_with_top_level_callee( self, top ):

    # Construct the graph with top level callee port

    V   = top.get_all_update_blocks() | top._dag.genblks | top._dag.top_level_callee_ports
    E   = top._dag.all_constraints | top._dag.top_level_callee_constraints
    Es  = { v: [] for v in V }
    InD = { v: 0  for v in V }

    for (u, v) in E: # u -> v
      InD[v] += 1
      Es [u].append( v )

    # Perform topological sort for a serial schedule.

    schedule = []

    Q = deque( [ v for v in V if not InD[v] ] )

    while Q:
      import random
      random.shuffle(Q)
      u = Q.pop()
      schedule.append( u )
      for v in Es[u]:
        InD[v] -= 1
        if not InD[v]:
          Q.append( v )

    print schedule
    top._sched.schedule_execute_index = 0

    def wrap_method( top, idx, schedule, method ):

      def actual_method( *args, **kwargs ):
        i = top._sched.schedule_execute_index
        if i > idx:
          # This means we need to advance a full cycle
          # Skip all methods in between and get back to the beginning
          while i < len(schedule):
            if not isinstance( schedule[i], CalleePort ):
              print schedule[i]
              schedule[i]()
            i += 1
          if i == len(schedule):
            i = 0
            print top.line_trace()

        while i < idx:
          if not isinstance( schedule[i], CalleePort ):
            print schedule[i]
            schedule[i]()
          i += 1

        ret = method( *args, **kwargs )
        i += 1
        while i < len(schedule):
          if isinstance( schedule[i], CalleePort ):
            break
          schedule[i]()
          print schedule[i]
          i += 1
        if i == len(schedule):
          i = 0
          print top.line_trace()

        top._sched.schedule_execute_index = i
        return ret

      return actual_method

    for i, x in enumerate( schedule ):
      if isinstance( x, CalleePort ):
        x.original_method = x.method
        x.method = wrap_method( top, i, schedule, x.method )

    from graphviz import Digraph
    dot = Digraph()
    dot.graph_attr["rank"] = "same"
    dot.graph_attr["ratio"] = "compress"
    dot.graph_attr["margin"] = "0.1"

    for x in V:
      x_name = repr(x) if isinstance( x, CalleePort ) else x.__name__
      x_host = repr(x.get_parent_object() if isinstance( x, CalleePort )
                    else top.get_update_block_host_component(x))
      dot.node( x_name +"\\n@" + x_host, shape="box")

    for (x, y) in E:
      x_name = repr(x) if isinstance( x, CalleePort ) else x.__name__
      x_host = repr(x.get_parent_object() if isinstance( x, CalleePort )
                    else top.get_update_block_host_component(x))
      y_name = repr(y) if isinstance( y, CalleePort ) else y.__name__
      y_host = repr(y.get_parent_object() if isinstance( y, CalleePort )
                    else top.get_update_block_host_component(y))

      dot.edge( x_name+"\\n@"+x_host, y_name+"\\n@"+y_host )
    dot.render( "/tmp/upblk-dag.gv", view=True )

    return schedule

