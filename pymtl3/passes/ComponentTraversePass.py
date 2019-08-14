#=========================================================================
# ComponentTraversePass.py
#=========================================================================
# Traverse the component hierarchy and generates a list of names of
# components that have the `marked` attribute.
#
# Author : Peitian Pan
# Date   : Aug 1, 2019

from pymtl3 import *
from pymtl3.passes.BasePass import BasePass, PassMetadata

class ComponentTraversePass( BasePass ):

  def __call__( s, top ):
    # Make sure we have the pass's namespace
    if not hasattr(top, "_pass_component_traverse"):
      top._pass_component_traverse = PassMetadata()

    s.marked = []
    s.traverse_hierarchy( top )

    # Write result to the pass's namespace
    top._pass_component_traverse.marked_components = \
        [c.__repr__() for c in s.marked]

  def traverse_hierarchy( s, component ):
    """Traverse the component hierarchy and call `s.process` for all components
    that have `marked` attribute."""
    if hasattr(component, "marked"):
      s.process( component )

    for child_component in component.get_child_components():
      s.traverse_hierarchy( child_component )

  def process( s, component ):
    """Customized process method to be called for each marked component."""
    name = component.__repr__()
    # Get a list of all input/output ports of `component`
    in_ports = component.get_input_value_ports()
    out_ports = component.get_output_value_ports()
    # Get a list of all wires of `component`
    wires = component.get_wires()
    # Get a list of two connected signals in the order they are connected
    connect_order = component.get_connect_order()
    # Do something here...
    print(f"name:{name} in_ports:{in_ports} out_ports:{out_ports} wires:{wires} connect_order:{connect_order}\n")
