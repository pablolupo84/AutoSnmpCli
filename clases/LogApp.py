"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def sleep(self): pass

    def breathe(self):
                 print ('Respirando aire')


class Dog(Animal):
    def eat(self):
                 print ('Come huesos')

    def sleep(self):
                 print ('perrera para dormir')


class Cat(Animal):
    def eat(self):
                 print ('Come pescado')

    def sleep(self):
                 print ('Casa del gato dormido')

                 from abc import ABCMeta, abstractmethod"""

#!/usr/bin/env python

import os
from datetime import datetime

"""
Descripcion: Modulo que permite manipular el Log de Errores de la APlicacion.
Si el archivo no existe lo crea y agrega el timestamp al loguear un mensaje.
Autor: Autotrol PL - Sistemas
Version: 0.1
"""

class logApp:
    """Modulo que permite manejar archivo de configuracion"""    
    def __init__(self,logFile):
        self.logFile = logFile
        self.logApp=open(self.logFile,'a+')
        self.logApp.close()

    def writeLog(self,msgError):
        self.msgError=str(datetime.now()) + ":" + msgError + "\n"
        self.logApp=open(self.logFile,'a+')
        self.logApp.write(self.msgError)
        self.logApp.close()

# TEST log_file.py
# mensajeError="ESte es un nuevo mensaje de error"
# fileError=logApp("log_file.txt")
# fileError.writeLog(mensajeError)
