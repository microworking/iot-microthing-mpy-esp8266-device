class HttpService:
    
    POST_HEADER = {"content-type": "application/json; charset=utf-8"}

    def get_actions():
      endpoint = Config.http_domain + '/api/telegram/iot/notify'

    def get_token():
      request_url = 'http://microworking.somee.com/api/telegram/iot/notify'
      print('')

    def get_day_of_week(): #colocar o verbo na web api
      request_url = 'http://microworking.somee.com/api/telegram/iot/notify'
      print('')

    def get_time(): #colocar o verbo na web api
      request_url = 'http://microworking.somee.com/api/telegram/iot/notify'
      print('')

    def send_call_back(msg):
      request_url = 'http://microworking.somee.com/api/telegram/iot/notify'
      msg.token = 0
      msg.uid = 0
      msg.update_id = 0
      msg.message_id = 0
      msg.result = 0
      msg.message = 0
      postdata = ujson.dumps(msg)
      res = urequests.post(request_url, headers = post_header, data = postdata)
      text = res.text

    def send_message(msg):
      request_url = 'http://microworking.somee.com/api/telegram/iot/notify'
      post_data = ujson.dumps({"text": msg, "chat_id": "","uid": "bx8bxcax15x00"})
      res = urequests.post(request_url, headers = POST_HEADER, data = post_data)
      text = res.text

    #token, uid, update_id, message_id, result, message
