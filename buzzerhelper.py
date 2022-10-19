class Beep:
  #from config import Config
  #_alarm = Config.alarm
  #_alarm = Pin(2, Pin.OUT)
  #_alarm.value(1)
  
  def __init__():
    _alarm = Pin(2, Pin.OUT)
    _alarm.value(1)
    
  def very_short():
    _alarm.value(0)
    time.sleep_ms(50)
    _alarm.value(1)
    time.sleep_ms(200)

  def short():
    _alarm.value(0)
    time.sleep_ms(100)
    _alarm.value(1)
    time.sleep_ms(200)

  def long():
    _alarm.value(0)
    time.sleep_ms(400)
    _alarm.value(1)
    time.sleep_ms(200)

  def very_long():
    _alarm.value(0)
    time.sleep_ms(1000)
    _alarm.value(1)
    time.sleep_ms(200)

  def init():
    _alarm = Pin(2, Pin.OUT)
    _alarm.value(0)
    time.sleep_ms(100)
    _alarm.value(1)
    time.sleep_ms(200)

  def conected():
    _alarm = Pin(2, Pin.OUT)
    _alarm.value(0)
    time.sleep_ms(100)
    _alarm.value(1)
    time.sleep_ms(200)
    _alarm.value(0)
    time.sleep_ms(400)
    _alarm.value(1)
    time.sleep_ms(200)

  def request():
    _alarm.value(0)
    time.sleep_ms(50)
    _alarm.value(1)
    time.sleep_ms(200)

  def error():
    _alarm.value(0)
    time.sleep_ms(1000)
    _alarm.value(1)
    time.sleep_ms(200)
    _alarm.value(0)
    time.sleep_ms(1000)
    _alarm.value(1)
    time.sleep_ms(200)
    _alarm.value(0)
    time.sleep_ms(1000)
    _alarm.value(1)
    time.sleep_ms(200)
    


