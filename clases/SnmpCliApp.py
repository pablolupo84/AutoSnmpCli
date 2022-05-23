from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import FileConfigIni
import LogApp


class SnmpCliApp():
 
    dic_configuracion={}

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
        self.logApp=LogApp.LogAppFile("snmtp_log.txt")
        self.snmpEngine= engine.SnmpEngine()
        self.datosConfigIni=FileConfigIni.FileConfigIni()

        self.InicializarDatos()

    def InicializarDatos(self):
        self.logApp.writeLog('Inicializando Datos - Config.ini')
        self.dic_configuracion.setdefault('TrapAgentAddress',self.datosConfigIni.showValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
        self.logApp.writeLog('TrapAgentAddress: {}'.format(self.dic_configuracion.get('TrapAgentAddress')))
        self.dic_configuracion.setdefault('Port',int(self.datosConfigIni.showValueItem('TRANSPORT_SETUP','Port')))
        self.logApp.writeLog('Port: {}'.format(self.dic_configuracion.get('Port')))
        self.dic_configuracion.setdefault('CommunityName',self.datosConfigIni.showValueItem('SNMP_V12_SETUP','CommunityName'))
        self.logApp.writeLog('CommunityName: {}'.format(self.dic_configuracion.get('CommunityName')))
        self.dic_configuracion.setdefault('ModeCommunity',self.datosConfigIni.showValueItem('SNMP_V12_SETUP','ModeCommunity'))
        self.logApp.writeLog('ModeCommunity: {}'.format(self.dic_configuracion.get('ModeCommunity')))

    def cbFun(self,snmpEngine, stateReference, contextEngineId, contextName,varBinds, cbCtx):
        self.logApp.writeLog('Received new Trap message')
        self.logApp.writeLog('Notification from ContextEngineId: {}'.format(contextEngineId.prettyPrint()))

        for name, val in varBinds:
            name_OID=name.prettyPrint()
            value_OID=val.prettyPrint()    
            if (self.OID_reference.get(name.prettyPrint())!=None):
                name_OID=self.OID_reference.get(name.prettyPrint())
            if (self.OID_reference.get(val.prettyPrint())!=None):
                value_OID=self.OID_reference.get(val.prettyPrint())

            self.logApp.writeLog('Name: {} | Val: {}'.format(name_OID,value_OID))


test=SnmpCliApp()
print(len(test.dic_configuracion))