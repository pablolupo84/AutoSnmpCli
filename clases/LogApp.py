import os
from datetime import datetime
from abc import ABCMeta, abstractmethod

"""
Descripcion: Modulo que permite manipular el Log de Errores de la APlicacion.
Si el archivo no existe lo crea y agrega el timestamp al loguear un mensaje.
Autor: Autotrol PL - Sistemas
Version: 0.1
"""

class LogApp(metaclass=ABCMeta):
         
    @abstractmethod
    def __init__(self,logFile):
        pass

    @abstractmethod
    def writeLog(self,msgError):
        pass

class LogAppFile(LogApp):
    """Clase que permite manejar un log en un archivo"""
    
    def __init__(self,logFile="log_file.txt"):
        self.logFile = logFile
        self.logApp=open(self.logFile,'a+')
        self.logApp.close()
    
    def writeLog(self,msgError):
        
        self.msgError=str(datetime.now()) + ":" + msgError + "\n"
        self.logApp=open(self.logFile,'a+')
        self.logApp.write(self.msgError)
        self.logApp.close()

class LogAppOutput(LogApp):
    """Clase que permite manejar un log por Standar Output"""
    
    def __init__(self):
        print("Iniciando salida por Standar Output")
    
    def writeLog(self,msgError):
        self.msgError=str(datetime.now()) + ":" + msgError + "\n"
        print(self.msgError)
        
    def writeLog(self,msgError):
        self.msgError=str(datetime.now()) + ":" + msgError + "\n"
        return self.msgError

# TEST log_file.py
# mensajeError="ESte es un nuevo mensaje de error"
# fileError=LogAppFile()
# fileError.writeLog(mensajeError)
# fileError=LogAppOutput()
# fileError.writeLog(mensajeError)