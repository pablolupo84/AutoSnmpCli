#!/usr/bin/env python

import configparser,os

"""
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Autotrol PL - Sistemas
Version: 0.1
"""

class config:
    """Modulo que permite manejar archivo de configuracion"""    
    def __init__(self,config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)  
        
    def ShowItemSection(self,section):
        return self.config.items(section)
    
    def ShowValueItem(self,section,key_word):
        return self.config.get(section,key_word)
    
    def change(self,section,key_word,value):
        self.config.set(section,key_word,value)

    def write(self):
        self.config.write(open(self.config_file,'w'))

# TEST clase_config.py
# configuracion=config('../config.ini')
# items=configuracion.ShowItemSection('TRANSPORT_SETUP')
# print (items)
# print (configuracion.ShowValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
# configuracion.change('TRANSPORT_SETUP','TrapAgentAddress','Peloncho')
# print (configuracion.ShowValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
# configuracion.write()