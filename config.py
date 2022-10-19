class Config:
  
  alarm = Pin(2, Pin.OUT)
  sensor = Pin(0, Pin.IN)
  control = None
  ssid = 'tatajewel'
  wifi_pass = 'mimosa2020'
  mqtt_domain = b'broker.hivemq.com'
  mqtt_host = '80db6d87c8a343e4985334eb98a49777.s1.eu.hivemq.cloud'
  mqtt_port = 8883
  mqtt_topic_sub = b'testtopic/1'
  mqtt_topic_pub = b'testtopic/1'
  mqtt_QoS = 0
  mqtt_client_id = ubinascii.hexlify(machine.unique_id())
  mqtt_user = 'mthing'
  mqtt_pass = '12345678'
  http_domain = 'http://microworking.somee.com/'    
  uid = Helper.get_uid()
  token = 'lLhnOasdfMjIafq24qqwefAoPTYqwgfNgWEE97t&F&%*R87'
  
  def __init__():
    print('')
  
  def get_alarm():
    from machine import Pin
    alarm = Pin(2, Pin.OUT)
    return(alarm)
  
  def sensor():
    return(self._sensor)
    
  def control():
    return(self._control)
    
  def ssid():
    return(self._ssid)
    
  def wifi_pass():
    return(self._wifi_pass)
    
  def mqtt_domain():
    return(self._mqtt_domain)
    
  def mqtt_host():
      return(self._mqtt_host)

  def mqtt_port():
      return(self._mqtt_port)

  def mqtt_topic_sub():
      return(self._mqtt_topic_sub)

  def mqtt_topic_pub():
      return(self._mqtt_topic_pub)

  def mqtt_QoS():
      return(self._mqtt_QoS)

  def mqtt_client_id():
      return(self._mqtt_client_id)

  def mqtt_user():
      return(self._mqtt_user)

  def mqtt_pass():
      return(self._mqtt_pass)

  def http_domain():
      return(self._http_domain)

  def http_domain():
      return(self._http_domain)

  def uid():
      return(self._uid)

  def token():
      return(self._token)



