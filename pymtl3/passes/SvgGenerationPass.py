#=========================================================================
# SvgGenerationPass.py
#=========================================================================
# 
#
# Author : Greg Nelson
# Date   : Sep 15, 2019

from pymtl3 import *
from pymtl3.passes.BasePass import BasePass, PassMetadata

# from netlistsvg import *

class SvgGenerationPass( BasePass ):

    def __call__( s, top ):
       
        if not hasattr(top, "_pass_svg_generation"):
            top._pass_svg_generation = PassMetadata()

        marked = s.find_marked(top)
        s.ports = []
        s.cells = []
        in_ports = marked.get_input_value_ports()
        out_ports = marked.get_output_value_ports()
        ndx = 2
        connect_order = marked.get_connect_order()
        order={}
        ndx = 2

        #assigns a unique id to each connection
        for (x,y) in connect_order:

            if(x in order.keys()):
                 order[x]=order[x]+[ndx]
            else:
                order[x]=[ndx]
            if(y in order.keys()):
                
                order[y]=order[y]+[ndx]
            else:
                order[y]=[ndx]
            ndx=ndx+1
        
        #iterates through all ports, creates its formatted json representation,
        #and adds this string to the list of all port strings, replaces . with _
        #becasue netlistsvg doesn't recognize port names with periods in them
        for inPort in in_ports:
            s.ports.append(SvgGenerationPass.Port(inPort.__repr__().replace('.','_'), "input",order[inPort]).getString())
           
        for outPort in out_ports:
            s.ports.append((SvgGenerationPass.Port(outPort.__repr__().replace('.','_'), "output", order[outPort]).getString()))
            
        #  iterates through all child components, creates its
        #  formatted json representation,
        #  and adds this string to the list of all cell strings
        for child_component in marked.get_child_components():
            type = ""
            if hasattr(child_component, "type"):
                type = child_component.type
            connectList = []
            in_port_list = []
            out_port_list = []
            for inPort in child_component.get_input_value_ports():
                inP =inPort.__repr__().replace('.','_')
                in_port_list.append(f'"{inP}": "input"')
                connectList.append(f'"{inP}": {order[inPort]}')

            for outPort in child_component.get_output_value_ports():
                outP =outPort.__repr__().replace('.','_')
                out_port_list.append(f'"{outP}": "output"')
                connectList.append(f'"{outP}": {order[outPort]}')
                      
            in_port_string = ', '.join(in_port_list)
            out_port_string = ', '.join(out_port_list)
            connect_string = ', '.join(connectList)
            port_string = in_port_string +", "+ out_port_string
            s.cells.append(SvgGenerationPass.Cell(child_component.__repr__(),type,port_string, connect_string).getString())
        
        s.module = SvgGenerationPass.Module(s.ports, s.cells)
        print(s.module.getString())
        
        name =marked.__repr__()+"-netlist"
        s.writeJSON(name,s.module.getString())
    
    

    #traverses the hiearchy until it finds the marked component and then returns it
    def find_marked( s, component ):
        if hasattr(component, "marked"):
            print ("tests")
            return component
        for child_component in component.get_child_components():
            s.find_marked( child_component )
    #creates a new json file 
    def writeJSON(s, fileName, str):
        path = './'+ fileName + '.json'
        f = open(path, 'w+')
        f.write(str)


    #JSON formatting
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
         
            self.str = (f'"{name}": {{'"\n"
                    f'   "type": "{type}",'"\n"
                    f'   "port_directions": {{'"\n"
                    f'       {ports}'"\n"
                    f'   }},'"\n"
                    f'   "connections": {{'"\n"
                    f'       {connections}'"\n"
                    f'   }}'"\n"
                    f'  }}'"\n")
    
        def getString (self):
            return self.str

    class Module:
        def __init__ (self, ports, cells):
            self.stringPorts = ', '.join(ports)
            self.stringCells = ', '.join(cells)
            self.str = (f'{{'"\n"
                   f'   "modules": {{'"\n"
                   f'       "module": {{'"\n"
                   f'           "ports": {{'"\n"
                   f'               {self.stringPorts}'"\n"
                   f'           }},'"\n"
                   f'           "cells": {{'"\n"
                   f'               {self.stringCells}'"\n"                  
                   f'       }},'"\n"        
                   f'            }}'"\n"
                   f'           }}'"\n"
                   f'}}'"\n"
                   
                   ) 

        def getString (self):
            return self.str

