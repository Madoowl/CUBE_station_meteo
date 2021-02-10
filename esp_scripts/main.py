from machine import I2C, Pin
from lcpi2c import LCDI2C
import network, urequests, utime, si7021, time
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
delay = 2 #En secondes
lcd = LCDI2C( i2c, cols=16, rows=2 )
lcd.backlight()
while True:
    print('T° : ' , s.temperature())
    print('Humidité : ' ,s.humidity(), '%')
    #response = urequests.post("http://jsonplaceholder.typicode.com/posts", data = str(s.temperature))
    #print(response.text)
    #print(response.json())
    # Affiche un messagee (sans retour à la ligne automatique)
    lcd.set_cursor( (0,0) )
    lcd.print('T: ')
    lcd.print(str(s.temperature()))
    lcd.print('C ')
    lcd.set_cursor( (0,1) )
    lcd.print('H: ')
    lcd.print(str(s.humidity()))
    lcd.print('%')   
    time.sleep(delay)
