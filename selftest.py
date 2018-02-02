# -*- coding: latin-1 -*-
#!/usr/bin/env python

import mynimbus
import time
import sys

print("Nimbus master start!!")
nm = mynimbus.NimbusMaster()
print("initialisation...")
nm.nimbus_init()
print("initialisation completed!")
print("Set all Gauge to 0")
nm.setGaugeValue(0,0)
time.sleep(0.5)	
nm.setGaugeValue(1,0)
time.sleep(0.5)
nm.setGaugeValue(2,0)
time.sleep(0.5)
nm.setGaugeValue(3,0)
time.sleep(4)
print("Set first gauge to 40, 60, 30 0 and 100")
nm.setGaugeValue(0,40)
time.sleep(2)
nm.setGaugeValue(0,60)
time.sleep(2)
nm.setGaugeValue(0,30)
time.sleep(2)
nm.setGaugeValue(0,0)
time.sleep(2)
nm.setGaugeValue(0,100)
print("Write text on all display")
nm.printText(0,"Test")
nm.printText(1,"Jeedom")
nm.printText(2,"Zelda")
nm.printText(3,"Working")
print("play with gauges")
nm.setGaugeValue(0,25)
time.sleep(0.5)
nm.setGaugeValue(1,50)
time.sleep(0.5)
nm.setGaugeValue(2,75)
time.sleep(0.5)
nm.setGaugeValue(3,100)
time.sleep(3)
print("return to 0 all")
nm.setGaugeValue(0,0)
time.sleep(0.5)
nm.setGaugeValue(1,0)
time.sleep(0.5)
nm.setGaugeValue(2,0)
time.sleep(0.5)
nm.setGaugeValue(3,0)