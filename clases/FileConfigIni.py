import configparser,os

"""
Descripcion: Modulo que permite manipular archivos de configuracion con formato : .ini
Autor: Autotrol PL - Sistemas
Version: 0.1
"""

class config():
    
    """Constructor: Recibe un path valido y retorna un diccionario parseado"""    
    
    def __init__(self,path = "../config.ini"):
        self.path = path
        self.fileParser = configparser.ConfigParser()
        self.fileParser.read(self.path)  

    def showItemSection(self,section):
        return self.fileParser.items(section)
    
    def showValueItem(self,section,key_word):
        return self.fileParser.get(section,key_word)
    
    def changeValueItem(self,section,key_word,value):
        self.fileParser.set(section,key_word,value)

    def writeFile(self):
        self.fileParser.write(open(self.path,'w'))

# TEST clase_config.py
# configuracion=config()
# items=configuracion.showItemSection('TRANSPORT_SETUP')
# print (items)
# print (configuracion.showValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
# configuracion.changeValueItem('TRANSPORT_SETUP','TrapAgentAddress','Peloncho')
# print (configuracion.showValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
# configuracion.writeFile()