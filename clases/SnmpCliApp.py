from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import FileConfigIni
import LogApp


class SnmpCliApp():
    #Define path log localmente.
    #pathLogApp="snmtp_log.txt"
    #logApp=LogApp.LogAppFile("snmtp_log.txt")
    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher
    # snmpEngine= engine.SnmpEngine()
    
    dic_configuracion={}
    #datosConfigIni=FileConfigIni.FileConfigIni()
    
    #Ver si sacarlo luego de aqui dentro
    OID_reference = {
    '1.3.6.1.6.3.1.1.5.0':'hwLoadAndBackupTrapsOID',
    '1.3.6.1.6.3.1.1.5.1':'coldStart',
    '1.3.6.1.6.3.1.1.5.2':'warmStart',
    '1.3.6.1.6.3.1.1.5.3':'linkDown',
    '1.3.6.1.6.3.1.1.5.4':'linkUp',
    '1.3.6.1.6.3.1.1.5.5':'authenticationFailure',
    '1.3.6.1.6.3.1.1.5.6':'egpNeighborLoss',
    '1.3.6.1.2.1.1.3.0': 'sysUpTimeInstance',
    '1.3.6.1.6.3.1.1.4.1.0':'snmpTrapOID',
    '1.3.6.1.6.3.18.1.3.0':'snmpTrapAddress',
    '1.3.6.1.6.3.18.1.4.0':'snmpTrapCommunity',
    '1.3.6.1.6.3.1.1.4.3.0':'snmpTrapEnterprise',
    '1.3.6.1.2.1.1.1.0':'sysDescr'
    }

    def __init__(self):
        logApp=LogApp.LogAppFile("snmtp_log.txt")
        snmpEngine= engine.SnmpEngine()
        datosConfigIni=FileConfigIni.FileConfigIni()

        self.InicializarDatos(logApp,datosConfigIni)

        

    def InicializarDatos(self,logApp,datosConfigIni):
        logApp.writeLog('Inicializando Datos - Config.ini')
        self.dic_configuracion.setdefault('TrapAgentAddress',datosConfigIni.showValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
        logApp.writeLog('TrapAgentAddress: {}'.format(self.dic_configuracion.get('TrapAgentAddress')))
        self.dic_configuracion.setdefault('Port',int(datosConfigIni.showValueItem('TRANSPORT_SETUP','Port')))
        logApp.writeLog('Port: {}'.format(self.dic_configuracion.get('Port')))
        self.dic_configuracion.setdefault('CommunityName',datosConfigIni.showValueItem('SNMP_V12_SETUP','CommunityName'))
        logApp.writeLog('CommunityName: {}'.format(self.dic_configuracion.get('CommunityName')))
        self.dic_configuracion.setdefault('ModeCommunity',datosConfigIni.showValueItem('SNMP_V12_SETUP','ModeCommunity'))
        logApp.writeLog('ModeCommunity: {}'.format(self.dic_configuracion.get('ModeCommunity')))


# test=SnmpCliApp()
# print(len(test.dic_configuracion))