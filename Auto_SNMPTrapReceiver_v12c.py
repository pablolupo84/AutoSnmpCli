
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import os,sys
from datetime import datetime
from clases import clase_config
from clases import clase_logFile

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


"""
Descripcion: Modulo que retorna un diccionario armado en base al archivo de configuracion
En caso de que un parametro este vacio, retorna un diccionario vacio.
Recibe por parametro el path donde se encuentra el archivo de configuracion.
Autor: Autotrol PL - Sistemas
Version: 0.1
"""
def InicializarDatos(path_config):
    dic_configuracion={}

    config_ini=clase_config.config(path_config)
    ErrorLog.writeLog('Inicializando Datos')
    dic_configuracion.setdefault('TrapAgentAddress',config_ini.ShowValueItem('TRANSPORT_SETUP','TrapAgentAddress'))
    ErrorLog.writeLog('TrapAgentAddress: {}'.format(dic_configuracion.get('TrapAgentAddress')))
    dic_configuracion.setdefault('Port',int(config_ini.ShowValueItem('TRANSPORT_SETUP','Port')))
    ErrorLog.writeLog('Port: {}'.format(dic_configuracion.get('Port')))
    dic_configuracion.setdefault('CommunityName',config_ini.ShowValueItem('SNMP_V12_SETUP','CommunityName'))
    ErrorLog.writeLog('CommunityName: {}'.format(dic_configuracion.get('CommunityName')))
    dic_configuracion.setdefault('ModeCommunity',config_ini.ShowValueItem('SNMP_V12_SETUP','ModeCommunity'))
    ErrorLog.writeLog('ModeCommunity: {}'.format(dic_configuracion.get('ModeCommunity')))

    for keys in dic_configuracion:
        if dic_configuracion[keys]=="":
            dic_configuracion.clear()
            break

    return dic_configuracion



# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName,varBinds, cbCtx):
    print('{} : Received new Trap message'.format(datetime.now()));
    print('{} : Notification from ContextEngineId: {}, ContextName: {}'.format(datetime.now(),contextEngineId.prettyPrint(),
                                                                        contextName.prettyPrint()))
    ErrorLog.writeLog('Received new Trap message')
    ErrorLog.writeLog('Notification from ContextEngineId: {}, ContextName: {}'.format(contextEngineId.prettyPrint(),contextName.prettyPrint()))

    for name, val in varBinds:
        name_OID=name.prettyPrint()
        value_OID=val.prettyPrint()    
        if (OID_reference.get(name.prettyPrint())!=None):
            name_OID=OID_reference.get(name.prettyPrint())
        if (OID_reference.get(val.prettyPrint())!=None):
            value_OID=OID_reference.get(val.prettyPrint())
        
        print('{} : Name: {} | Val: {}'.format(datetime.now(),name_OID,value_OID))
        print('--------------------------------------------------------------------------')
        ErrorLog.writeLog('Name: {} | Val: {}'.format(name_OID,value_OID))
        ErrorLog.writeLog('--------------------------------------------------------------------------')
        

if __name__ == '__main__':
    
    #Define path log localmente.
    PATH_LOG="snmtp_log.txt"

    # Create SNMP engine with autogenernated engineID and pre-bound
    # to socket transport dispatcher
    snmpEngine = engine.SnmpEngine()

    #Se crea la instancia logApp con el path de archivo de logs
    ErrorLog=clase_logFile.logApp(PATH_LOG)

    print('\n{} Iniciando Auto_SNMPTrapReceiver'.format(datetime.now()));
    ErrorLog.writeLog('Iniciando Auto_SNMPTrapReceiver')


    try:
        dic_configuracion=InicializarDatos('config.ini')
        if dic_configuracion:
            
            # UDP over IPv4, first listening interface/port
            ErrorLog.writeLog('UDP over IPv4, first listening interface/port')
            config.addTransport(
                snmpEngine,
                udp.domainName + (1,),
                udp.UdpTransport().openServerMode((dic_configuracion.get('TrapAgentAddress'),
                                                    dic_configuracion.get('Port')))
            )

            # SNMPv1/2c setup
            ErrorLog.writeLog('SNMPv1/2c setup')
            config.addV1System(snmpEngine,  dic_configuracion.get('CommunityName'), 
                                            dic_configuracion.get('ModeCommunity'))
            
        else:
            ErrorLog.writeLog('Inicializar Datos - Vacio por datos sin configurar')
    except Exception as err:
        print("Error: {}".format(err))
        ErrorLog.writeLog("Error: {}".format(err))
    else: 
        print('--------------------------------------------------------------------------')
        print('Start SNMPTrapReceiver -> {}'.format(datetime.now()))
        print("Agent is listening SNMP Trap on {} Port : {}".format(dic_configuracion.get('TrapAgentAddress'),dic_configuracion.get('Port')))
        print('--------------------------------------------------------------------------')
        
        ErrorLog.writeLog('--------------------------------------------------------------------------')
        ErrorLog.writeLog('Start SNMPTrapReceiver')
        ErrorLog.writeLog("Agent is listening SNMP Trap on {} Port : {}".format(dic_configuracion.get('TrapAgentAddress'),dic_configuracion.get('Port')))
        ErrorLog.writeLog('--------------------------------------------------------------------------')


        # Register SNMP Application at the SNMP engine
        ntfrcv.NotificationReceiver(snmpEngine, cbFun)
        ErrorLog.writeLog('Register SNMP Application at the SNMP engine')

        # this job would never finish
        snmpEngine.transportDispatcher.jobStarted(1)  
        ErrorLog.writeLog('snmpEngine.transportDispatcher.jobStarted()')

        # Run I/O dispatcher which would receive queries and send confirmations
        try:
            snmpEngine.transportDispatcher.runDispatcher()
            ErrorLog.writeLog('snmpEngine.transportDispatcher.runDispatcher()')
        except:
            snmpEngine.transportDispatcher.closeDispatcher()
            ErrorLog.writeLog('snmpEngine.transportDispatcher.closeDispatcher()')

    finally:
        print('{} : Finaliza app Auto_SNMPTrapReceiver'.format(datetime.now()))
        ErrorLog.writeLog('Finaliza app Auto_SNMPTrapReceiver')
