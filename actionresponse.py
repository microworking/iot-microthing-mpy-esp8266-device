
class ActionResponse:
  
  def __init__(self):
    self.identity_token = None
    self.uid = None
    self.gpio = None
    self.action = None
    self.owner = None
    self.update_id = None
    self.chat_id = None
    self.message_id = None
    self.peripheral = None
    self.message = None
    self.date = None
  
  def to_payload(self):
    #response = dict({ 'identity_token':self.identity_token, 'uid':self.uid, 'gpio':self.gpio, 'action':self.action, 'owner':self.owner, 'update_id':self.update_id, 'chat_id':self.chat_id, 'message_id':self.message_id, 'peripheral':self.peripheral, 'message':self.message, 'date':self.date })
    response = '{ "identity_token": "' + self.identity_token + '", "uid": "' + self.uid + '", "gpio": ' + str(self.gpio) + ', "action": "' + self.action + '", "owner": "' + self.owner + '", "update_id": ' + str(self.update_id) + ', "chat_id": ' + str(self.chat_id) + ', "message_id": ' + str(self.message_id) + ', "peripheral": "' + self.peripheral + '", "message": "' + self.message + '", "date": "' + self.date + '"}'
    return response
  
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

