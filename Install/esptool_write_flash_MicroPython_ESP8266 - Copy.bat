python -m esptool --chip esp8266 erase_flash

python -m esptool --chip esp8266 --port COM3 write_flash --flash_mode dio --flash_size detect 0x0 C:\microworking\ESP8266\MicroPython\Firmware_MicroPython\esp8266-1m-20220618-v1.19.1.bin