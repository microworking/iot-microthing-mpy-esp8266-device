class HttpHandler:
  
  def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('TimRouter','12345678')
    #sta_if.connect('VIVOFIBRA-307E','57601b307e')
    #sta_if.connect('tatajewel', 'mimosa2020')
    while not sta_if.isconnected():
      if sta_if.isconnected():
        print('network config:', sta_if.ifconfig()) #debug
        break
      else:
        sta_if.active(False)
        sta_if.active(True)
        sta_if.connect('TimRouter','12345678')
        #sta_if.connect('tatajewel','mimosa2020')
        #sta_if.connect('VIVOFIBRA-307E','57601b307e')
        time.sleep(10)

  def http_get(url, port):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.connect(addr)    
    for i in range(10):
      try:
        s.write(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        break
      except:
        pass #TODO: tratar o erro para dar by pass por umas 20x ai reinicia o modulo
    while True:
        data = s.recv(100)
        if data:
            pass #print(str(data, 'utf8'), end='') #tratar 404, 500, etc
        else:
            break
    s.close()




