#mqtt_server = b'broker.hivemq.com'
#mqtt_server = b'80db6d87c8a343e4985334eb98a49777.s1.eu.hivemq.cloud'
mqtt_server = b'mqtt.flespi.io'
topic_sub = b'microworking/telegram-iot/microthingv1/broker'
topic_pub = b'microworking/telegram-iot/microthingv1/cloud'
last_message = 0
message_interval = 5
counter = 0
client_id = ubinascii.hexlify(machine.unique_id())

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

def connect_and_subscribe():
  import ssl
  global client_id, mqtt_server, topic_sub
   
  client = MQTTClient(client_id, mqtt_server, port=1883, user=b"8o1nx9zfTFUiAkYdgWR3GUlX9fxpREFOQw1dtoidR0jfa5ihR0alIj9GmuV4YrIE", password='', keepalive=4000, ssl=False) 
  #client = MQTTClient(client_id, mqtt_server, port=8883, user=b"mthing", password=b"12345678", keepalive=4000, ssl=True, ssl_params={ "ca_certs":server, "ca_file":cert, "keyfile":key, "certfile": cert})
  #client = MQTTClient(client_id, mqtt_server, port=8883, user=b"mthing", password=b"12345678", keepalive=4000, ssl=True, ssl_params={ "certfile":b"/mqtt-client-cert.pem", "cert_reqs":b"CERT_REQUIRED" }) #"certfile":b"/mqtt-client-cert.pem" "ca_certs":b"/isrgrootx1.pem", "keyfile":b"/mqtt-client-key.pem",
  #client = MQTTClient(client_id, mqtt_server, port=8883, user=b"mthing", password=b"12345678", keepalive=4000, ssl=True, ssl_params={ 'server_side':True, 'cert_reqs': 'CERT_REQUIRED', 'ca_certs':'/isrgrootx1.pem', 'certfile':'/mqtt-client-cert.pem', 'keyfile':'/mqtt-client-key.pem', 'do_handshake':True }) 
  #client = MQTTClient(client_id, mqtt_server, port=8883, user=b"mthing", password=b"12345678", keepalive=4000, ssl=True, ssl_params={ "cert_reqs": "CERT_REQUIRED", "ca_certs":"/isrgrootx1.pem", "keyfile":"/mqtt-client-key.pem", "certfile":"/mqtt-client-cert.pem" }) 
  #client = MQTTClient(client_id, mqtt_server, port=8883, user=b"mthing", password=b"12345678", keepalive=4000, ssl=True, ssl_params={ "server_hostname": mqtt_server, 'ca_certs':'/hivemq.pem', 'keyfile':None, 'certfile':None }) 
  #client = MQTTClient(client_id, mqtt_server, user="mthing", password="12345678") .encode("utf-8")
  #client = MQTTClient(client_id, mqtt_server, 8883, 'mthing', '12345678')
  #client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(2)
  machine.reset()
  
def new_message_handler(topic, msg):
  try:
    msg_str = ujson.loads(msg.decode())
    msg_obj = ActionRequest(msg_str)
    if msg_obj.uid == Helper.get_uid():
      ActionHandler.select_action(msg_obj)
  except Exception as ex:
    print('New message handler exception: ' + str(ex))
    pass

def publish_handler(payload_obj):
  global topic_pub
  try:
    mqttclient.publish(topic_pub, payload_obj.to_payload(), retain=False, qos=0)
  except Exception as ex:
    print('Publish message handler exception: ' + str(ex))
    pass


