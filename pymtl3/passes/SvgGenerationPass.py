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

class SvgGenerationPass( BasePass ):

  def __call__( s, top ):
    # Make sure we have the pass's namespace
    if not hasattr(top, "_pass_svg_generation"):
      top._pass_svg_generation = PassMetadata()

    s.marked = []
    s.ports = []
    s.cells = []
    s.traverse_hierarchy( top )
    s.module = SvgGenerationPass.Module(s.ports, s.cells)
    print(s.module)
    # Write result to the pass's namespace
    top._pass_svg_generation.marked_components = \
        [c.__repr__() for c in s.marked]
    
    class Port:

        def __init__ (self, name, direction, bits):
            self.str = (f'"{name}": {{'"\n"
                   f'   "direction": "{direction}",'"\n"
                   f'   "bits":{bits}'"\n"
                   f'}}'"\n")

        def getString (self):
            return self.str


    class Cell:
        def __init__ (self, name, type, ports, connections):
            self.stringPorts = ', '.join(ports)
            self.stringConnections = ', '.join(connections)
            self.str = (f'"{name}": {{'"\n"
                    f'   "type": "{type}",'"\n"
                    f'   "port_directions": {{'"\n"
                    f'       {self.stringPorts}'"\n"
                    f'   }},'"\n"
                    f'   "connections": {{'"\n"
                    f'       {self.stringConnections}'"\n"
                    f'   }}'"\n"
                    f'  }}'"\n")
    
        def getString (self):
            return self.str

    class Module:

        def __init__ (self, ports, cells):
            self.stringPorts = ', '.join(ports)
            self.stringCells = ', '.join(cells)
            self.str = (f'{{'"\n"
                   f'   "top": {{'"\n"
                   f'       "<module>": {{'"\n"
                   f'           "ports": {{'"\n"
                   f'               {self.stringPorts}'"\n"
                   f'           }},'"\n"
                   f'           "cells": {{'"\n"
                   f'               {self.stringCells}'"\n"
                   f'           }},'"\n"
                   f'       }}'"\n"
                   f'    }}'"\n"
                   f'}}'"\n")
    
        def getString (self):
            return self.str

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
    # Get a list of all wires of `componentx`
    wires = component.get_wires()
    # Get a list of two connected signals in the order they are connected
    connect_order = component.get_connect_order()
    # Do something here...
    # print(f"name:{name} in_ports:{in_ports} out_ports:{out_ports} wires:{wires} connect_order:{connect_order}\n")
    in_port_list = []
    out_port_list = []

    for inPort in in_ports:
        in_port_list.append(f'"{inPort}": "input"')
    in_port_string = ', '.join(in_port_list)
    
    for outPort in out_ports:
        out_port_list.append(f'"{outPort}": "output"')
    out_port_string = ', '.join(out_port_list)
    port_string = in_port_string +", "+ out_port_string
    s.cells.append(SvgGenerationPass.Cell(name,'',port_string,'Not Implemented'))
