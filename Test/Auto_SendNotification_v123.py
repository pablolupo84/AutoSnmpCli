from pysnmp.hlapi import *
from pysnmp.hlapi.asyncore import *


#SEnd Notification v1y2
#Instancia dedicada a snmpEngine
snmpEngine = SnmpEngine()

#Primer MENSAJE A ENVIAR
sendNotification(
		snmpEngine,
		CommunityData('public'),
		UdpTransportTarget(('192.168.0.26', 162)),
		ContextData(),
		'trap',
		NotificationType(ObjectIdentity('SNMPv2-MIB', 'coldStart')),
	)

try:
    snmpEngine.transportDispatcher.runDispatcher()
    print("Primer Mensaje Enviado")
except:
	print("Primer Mensaje No Enviado")


#Instancia dedicada a snmpEngine
snmpEngine_2=SnmpEngine()

#Segundo MENSAJE A ENVIAR
sendNotification(
        snmpEngine_2,
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('127.0.0.1', 162)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity('1.3.6.1.6.3.1.1.5.2')
        ).addVarBinds(
            ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
            ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
        )
    )

try:
    snmpEngine_2.transportDispatcher.runDispatcher()
    print("Segundo Mensaje Enviado")
except:
    print("Segundo Mensaje No Enviado")



#Instancia dedicada a snmpEngine
snmpEngine_3=SnmpEngine(OctetString(hexValue='8000000004030201'))

#Tercer MENSAJE A ENVIAR
sendNotification(
        snmpEngine_3,
        UsmUserData(
            'user3',
            'user3password', 'user3encryption',
            authProtocol=usmHMACMD5AuthProtocol,
            privProtocol=usmDESPrivProtocol,
        ),
        UdpTransportTarget(("127.0.0.1", 162)),
        ContextData(),
        "trap",
        NotificationType(ObjectIdentity("SNMPv2-MIB", "authenticationFailure")),
    )

try:
    snmpEngine_3.transportDispatcher.runDispatcher()
    print("Tercer Mensaje Enviado")
except:
    print("Tercer Mensaje No Enviado")

#Instancia dedicada a snmpEngine
snmpEngine_4=SnmpEngine(OctetString(hexValue='8000000001020304'))

#Cuarto MENSAJE A ENVIAR
sendNotification(
        snmpEngine_4,
         UsmUserData(
             'usr-sha-aes128',
             'authkey1', 'privkey1',
             authProtocol=usmHMACSHAAuthProtocol,
             privProtocol=usmAesCfb128Protocol,
         ),
        UdpTransportTarget(("127.0.0.1", 162)),
        ContextData(),
        "inform",
        NotificationType(ObjectIdentity("SNMPv2-MIB", "authenticationFailure")),
    )

try:
    snmpEngine_4.transportDispatcher.runDispatcher()
    print("Cuarto Mensaje Enviado")
except:
    print("Cuarto Mensaje No Enviado")