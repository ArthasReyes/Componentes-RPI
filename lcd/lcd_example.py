from time import sleep
from machine import Pin
from lcd_new import Lcd

led = Pin('LED', Pin.OUT)
lcd = Lcd(16,2,0,1)    

led.off()
lcd.putstr("Hola mundo!")
sleep(2)
lcd.clear()
lcd.putstr("Encendiendo LED...")
led.on()
sleep(2)
lcd.putstr("Apagando LED...")
led.off()
sleep(2)
lcd.clear()
lcd.putstr("Adiós...")
