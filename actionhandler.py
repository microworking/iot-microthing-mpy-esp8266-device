
class ActionHandler:
  
    def select_action(msg_obj):      
      action = ActionResponse()
      action.identity_token = msg_obj.identity_token
      action.uid = Helper.get_uid()
      action.gpio = msg_obj.gpio
      action.action = msg_obj.action
      action.owner = msg_obj.owner
      action.update_id = msg_obj.update_id
      action.chat_id = msg_obj.chat_id
      action.message_id = msg_obj.message_id
      action.peripheral = msg_obj.peripheral
      action.message = msg_obj.message
      action.date = msg_obj.date
      if msg_obj.action == 'start': ActionHandler.start_action(action)
      if msg_obj.action == 'stop': ActionHandler.stop_action(action)
      if msg_obj.action == 'read': ActionHandler.read_action(action)
      if msg_obj.action == 'restart': ActionHandler.restart_action(action)
      if msg_obj.action == 'debug': ActionHandler.debug_action(action)
      if msg_obj.action == 'sound': ActionHandler.sound_action(action)
      if msg_obj.action == 'broadcast': ActionHandler.broadcast_action(action)
      if msg_obj.action == 'sys': ActionHandler.get_sys_info_action(action)
      if msg_obj.action == 'network': ActionHandler.get_network_info_action(action)
      if msg_obj.action == 'version': ActionHandler.get_version_info_action(action)
      if msg_obj.action == 'test': ActionHandler.test_action(action)

    def start_action(action):
      global sensor, mqtt, gpio2_state_1_message, sound_enanble
      action.message = gpio2_state_1_message % (action.owner)
      if sound_enanble: Beep.request()
      sensor.value(1)
      mqtt.publish_handler(action)

    def stop_action(action):
      global sensor, mqtt, gpio2_state_0_message, sound_enanble
      action.message = gpio2_state_0_message % (action.owner)
      if sound_enanble: Beep.request()
      sensor.value(0)
      mqtt.publish_handler(action)
 
    def read_action(action):
      global mqtt, sensor, gpio0_state_0_message, gpio0_state_1_message, sound_enanble
      if(sensor.value() == 0):
        action.message = gpio0_state_0_message % (action.peripheral)
      else:
        action.message = gpio0_state_1_message % (action.peripheral)
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)

    def restart_action(action):
      global mqtt, restart_message, sound_enanble
      action.message = restart_message % (action.peripheral, action.owner)
      mqtt.publish_handler(action)
      if sound_enanble: Beep.request()
      machine.reset()
      
    def debug_action(action):
      global mqtt, debug_mode, sound_enanble
      msg = None
      if debug_mode == True:
        debug_mode = False
        msg = 'desabilitado'
      else:
        debug_mode = True
        msg = 'habilitado'
      action.message = debug_mode_message % (msg, action.peripheral, action.owner)
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)
      
    def sound_action(action):
      global sensor, mqtt, sound_enanble, sound_enanble_message
      msg = None
      if sound_enanble == True:
        sound_enanble = False
        msg = 'desabilitado'
        sensor.value(1)
      else:
        sound_enanble = True
        msg = 'habilitado'
        sensor.value(0)
      action.message = sound_enanble_message % (msg, action.peripheral, action.owner)
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)
    
    def broadcast_action(action):
      global mqtt, broadcast_enable, broadcast_enable_message, sound_enanble
      msg = None
      if broadcast_enable == True:
        broadcast_enable = False
        msg = 'desabilitado'
      else:
        broadcast_enable = True
        msg = 'habilitado'
      action.message = broadcast_enable_message % (msg, action.peripheral, action.owner)
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)

    def get_sys_info_action(action):
      global mqtt, sound_enanble
      action.message = Helper.get_sys_info()
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)
          
    def get_network_info_action(action):
      global mqtt, sound_enanble
      action.message = Helper.get_network_info()
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)
      
    def get_version_info_action(action):
      global mqtt, sound_enanble
      action.message = Helper.get_version_info()
      if sound_enanble: Beep.request()
      mqtt.publish_handler(action)
  
    def test_action(action):
      global mqtt
      action.message = 'Beeeep! ;-)'
      mqtt.publish_handler(action)
      Beep.init()

