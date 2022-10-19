class ActionHandler:
  
    def select_action(msg_obj):
      action = ActionResponse()
      action.identity_token = msg_obj.identity_token
      action.uid = msg_obj.uid
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
      if msg_obj.action == 'sys': ActionHandler.get_sys_info_action(action)
      if msg_obj.action == 'network': ActionHandler.get_network_info_action(action)
      if msg_obj.action == 'version': ActionHandler.get_version_info_action(action)
      if msg_obj.action == 'test': ActionHandler.test_action(action)

    def start_action(action):
      #actionResponse.gpio
      #actionResponse.action
      action.message = 'Ola ' + action.owner + ', este dispositivo nao possui perifericos para controlar'
      publish_handler(action)

    def stop_action(action):
      #actionResponse.gpio
      #actionResponse.action
      action.message = 'Ola ' + action.owner + ', este dispositivo nao possui perifericos para controlar'
      publish_handler(action)
 
    def read_action(action):
      wsensor = Pin(action.gpio, Pin.IN, Pin.PULL_UP)
      if(wsensor.value() == 0):
        action.message = 'O ' + action.peripheral + ' esta detectando agua'
      else:
        action.message = 'O ' + action.peripheral + ' nao esta detectando agua'
      publish_handler(action)

    def restart_action(action):
      action.message = 'O dispositivo controlador dp periferico ' + action.peripheral + ' sera reiniciado pelo usuario ' + action.owner + '...por favor aguarde'
      publish_handler(action)

    def get_sys_info_action(action):
      action.message = Helper.get_sys_info()
      publish_handler(action)
          
    def get_network_info_action(action):
      action.message = Helper.get_network_info()
      publish_handler(action)
      
    def get_version_info_action(action):
      action.message = Helper.get_version_info()
      publish_handler(action)
  
    def test_action(action):
      action.message = 'Beeeep! ;-)'
      publish_handler(action)
      Beep.init()

