#print(wlan.scan())             # scan for access points
Beep.init()
HttpHandler.do_connect()
Beep.conected()

try:
  mqttclient = connect_and_subscribe()
except OSError as e:
  print(e)
  restart_and_reconnect()
  mqttclient = connect_and_subscribe()

flowc = 0
mqttclient.set_callback(new_message_handler)

sensor = Pin(0, Pin.IN, Pin.PULL_UP)
while True:
  try:
    mqttclient.check_msg()
    #schedule.check_time()
    #sensors.check_state()
    
    if sensor.value() == 0 and flowc == 1:
      print('sensor == 0 and flowc == 1')
      flowc = 0
      #time.sleep_ms(500)
    
    if sensor.value() == 1 and flowc == 0:
      print('sensor == 1 and flowc == 0')
      flowc = 1
      #time.sleep_ms(500)
    
  except OSError as e:
    restart_and_reconnect()

# TODO: tratar o erro no http_get OSError -2 e ECCONABORTED
# TODO: descobrir como encriptografar o token e o chatid
# TODO: criar rotinas de startup (colocar ssid, pass, token, chatid, nome, local e servidor http 80 em modo AP)
# from machine import WDT #TODO: nao da para passar um valor de timeout para o watch dog (implementar?)
# wdt = WDT()
# wdt.feed()
