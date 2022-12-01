process_timer = Timer(-1)

def main_process_start():
  global process_timer, process_verify_cycle
  process_timer = Timer(-1)
  process_timer.init(period=process_verify_cycle, mode=Timer.PERIODIC, callback=lambda t:main_process())

def main_process_stop():
  global process_timer
  process_timer.deinit()

def main_process():
  global mqtt, mqtt_client, action, flow_control, sensor, debug_mode
  print("")
