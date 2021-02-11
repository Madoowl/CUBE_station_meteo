from machine import I2C, Pin 
from lcpi2c import LCDI2C
from time import sleep
import network, utime, si7021, time, json, urequests as requests

def init_screen():
    i2c = I2C(-1, Pin(2), Pin(0))
    lcd = LCDI2C( i2c, cols=16, rows=2 )
    lcd.backlight()
    lcd.clear()
    return lcd

def do_connect(lcd = None):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        try:
            if lcd != None :
                lcd = init_screen()
                lcd.set_cursor( (0,0) )
                lcd.print('Connexion en')
                lcd.set_cursor( (0,1) )
                lcd.print('cours ...')
                time.sleep(2)
            else :
                lcd = init_screen()
        except OSError :
            lcd.set_cursor( (0,0) )
            lcd.print('Erreur réseau')
        wlan.connect('Iphone de Yuki', 'blablack') 
        while not wlan.isconnected():
            pass
    print('Config Wifi :', wlan.ifconfig())
    try:
        lcd.clear()
        lcd.set_cursor( (0,0) )
        lcd.print('Connecte !')
        time.sleep(2)
    except OSError :
        lcd.set_cursor( (0,0) )
        lcd.print('Erreur réseau')
        
# init_screen()
do_connect(lcd = init_screen())

i2c = I2C(-1, Pin(2), Pin(0))
s = si7021.SI7021(i2c)
delay = 5 #En secondes
lcd = init_screen()
while True:
    superdata = []
    wlan = network.WLAN(network.STA_IF)
    i = 1
    print('T° : ' , s.temperature())
    print('Humidité : ' ,s.humidity(), '%')
    try:
        lcd.clear
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
        
    while i % 5 != 0 :
        datas = {
            "serial": 1,
            "temp": s.temperature(),
            "hum": s.humidity(),
            "delay": delay,
            "ip": wlan.ifconfig()
                    
            }
        superdata.append(datas)
        i = i + 1
        time.sleep(delay)
        
    print(json.dumps(superdata))
    url = "http://172.20.10.14:5000/api/tempRel/"
    data = superdata
    try :
        r = requests.post(url, json=data)
        try: 
            lcd.clear()
            lcd.set_cursor( (0,0) )
            lcd.print('Donnees')
            lcd.set_cursor( (0,1) )
            lcd.print('envoyees !')
            time.sleep(2)
        except OSError :
            print('Pas d\'écran')
    except:
        try:
            lcd.clear()
            lcd.set_cursor( (0,0) )
            lcd.print('Erreur')
            lcd.set_cursor( (0,1) )
            lcd.print('reseau !')
            time.sleep(2)
        except OSError :
            print('Pas d\'écran')

