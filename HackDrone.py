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
	print "\tARROW UP : Move forward"
	print "\tARROW DOWN : Move backward"
	print "\tARROW RIGHT : Move to the right"
	print "\tARROW LEFT : Move to the left"
	print "\t--"
	print "\tZ : Increase vertical position"
	print "\tS : Decrease vertical position"
	print "\tQ : Turn left (without movement)"
	print "\tD : Turn right (without movement)"





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
                  help="Print all commands available",)
(options, args) = parser.parse_args()

if len(args) > 4:
    parser.error("wrong number of arguments")

# ip_drone = '192.168.1.1'
# MAC_drone = '90:03:b7:fd:22:49'
ip_src = options.ip_address
MAC_src = options.MAC_address
interface = options.interface
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
                print "takeoff"
            elif event.key == pygame.K_SPACE:
                print "land"
            # emergency
            # elif event.key == pygame.K_BACKSPACE:
            #     drone.reset()
            # Monte / Descend
            elif event.key == pygame.K_z:
                print "Monte"
            elif event.key == pygame.K_s:
                print "Descend"
            # Tourne a gauche / droite (pas de deplacement)
            elif event.key == pygame.K_q:
                print "Tourne a gauche"
            elif event.key == pygame.K_d:
                print "Tourne a droite"
            # Avance / Recule
            elif event.key == pygame.K_UP:
            	print "Avance"
            elif event.key == pygame.K_DOWN:
            	print "Recule"
            # Deplacement a gauche / roite
            elif event.key == pygame.K_LEFT:
            	print "Deplace a gauche"
            elif event.key == pygame.K_RIGHT:
            	print "Deplace a droite"
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