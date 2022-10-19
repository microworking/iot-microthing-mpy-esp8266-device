# This file is executed on every boot (including wake-boot from deepsleep)
#import webrepl
#webrepl.start()
import os
#uos.dupterm(None, 1) # disable REPL on UART(0)
import sys
import gc
import esp
import machine
import micropython
import time
import ubinascii
import network
import socket
import urequests
import ujson
import ussl
from machine import Pin, Signal
from simple import MQTTClient

esp.osdebug(None)
gc.collect()
gc.threshold(gc.mem_free() // 4 + gc.mem_alloc())

exec(open('commonhelper.py').read(),globals())
exec(open('config.py').read(),globals())
exec(open('buzzerhelper.py').read(),globals())
exec(open('httphandler.py').read(),globals())
exec(open('mqttservice.py').read(),globals())
exec(open('actionrequest.py').read(),globals())
exec(open('actionresponse.py').read(),globals())
exec(open('actionhandler.py').read(),globals())
exec(open('main.py').read(),globals())
