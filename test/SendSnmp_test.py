from pysnmp.hlapi import *
from pysnmp.hlapi.asyncore import *


#SEnd Notification v1y2
#Instancia dedicada a snmpEngine
snmpEngine = SnmpEngine()

#Primer MENSAJE A ENVIAR
sendNotification(
		snmpEngine,
		CommunityData('public'),
		UdpTransportTarget(('10.0.2.15', 162)),
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
        UdpTransportTarget(('10.0.2.15', 162)),
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