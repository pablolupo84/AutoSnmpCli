import FileConfigIni,LogApp
import unittest
import os
from datetime import datetime

class Test(unittest.TestCase):
        
    def test_Port_162(self):
        self.configuracion=FileConfigIni.FileConfigIni("../config.ini")
        self.assertEqual(self.configuracion.showValueItem('TRANSPORT_SETUP','port'),"162","test_Port_162")

    def test_cantidad_items_transport_setup_igual_3(self):
        self.configuracion=FileConfigIni.FileConfigIni("../config.ini")
        self.assertEqual(len(self.configuracion.showItemSection('TRANSPORT_SETUP')),3,"test_cantidad_items_transport_setup_igual_3")
    
    def test_mensaje_output_hola_mundo(self):
        msg="HolaMundo"
        self.fileError=LogApp.LogAppOutput()
        self.assertIn(msg,self.fileError.writeLog(msg))


if __name__ == '__main__':
    unittest.main() 
 