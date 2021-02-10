from machine import I2C, Pin
import json
import urequests as requests
from lcpi2c import LCDI2C
import network, utime, si7021, time
from time import sleep
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Iphone de Yuki', 'blablack') 
        while not wlan.isconnected():
            pass
    print('Config Wifi :', wlan.ifconfig())
do_connect()
i2c = I2C(-1, Pin(2), Pin(0))
s = si7021.SI7021(i2c)
delay = 5 #En secondes
try:
    lcd = LCDI2C( i2c, cols=16, rows=2 )
    lcd.backlight()
except OSError:
    print('Pas d\'ecran')
while True:
    superdata = []
    i = 1
    while i % 5 != 0 :
        print('T° : ' , s.temperature())
        print('Humidité : ' ,s.humidity(), '%')
        datas = {
            "temp": s.temperature(),
            "hum": s.humidity(),
            "delay": delay,           
            }
        superdata.append(datas)
        i = i + 1
        try:
            lcd = LCDI2C( i2c, cols=16, rows=2 )
            lcd.backlight()
            lcd.set_cursor( (0,0) )
            lcd.print('T: ')
            lcd.print(str(s.temperature()))
            lcd.print('C ')
            lcd.set_cursor( (0,1) )
            lcd.print('H: ')
            lcd.print(str(s.humidity()))
            lcd.print('%')
        except OSError :
            print('Pas d\'écran')
        time.sleep(delay)   
    print(json.dumps(superdata))
    
    url = "http://172.20.10.14:5000/api/tempRel/"
    data = superdata
    r = requests.post(url, json=data)
