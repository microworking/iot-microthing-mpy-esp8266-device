
class ActionRequest:
  
  def __init__(self, message):
    self.identity_token = message["identity_token"]
    self.uid = message["uid"]
    self.gpio = message["gpio"]
    self.action = message["action"]
    self.owner = message["owner"]
    self.update_id = message["update_id"]
    self.chat_id = message["chat_id"]
    self.message_id = message["message_id"]
    self.peripheral = message["peripheral"]
    self.message = message["message"]
    self.date = message["date"]

  def identity_token(self):
    return(self.identity_token)
  
  def uid(self):
    return(self.uid)
    
  def gpio(self):
    return(self.gpio)
    
  def action(self):
    return(self.action)

  def owner(self):
    return(self.owner)

  def update_id(self):
    return(self.update_id)

  def chat_id(self):
    return(self.chat_id)
    
  def message_id(self):
    return(self.message_id)
    
  def peripheral(self):
    return(self.peripheral)
    
  def message(self):
    return(self.message)

  def date(self):
    return(self.date)
    