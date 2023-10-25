#imports
from machine import ADC, Pin
import time

# LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Pot goes on ADC pin 27
pot = ADC(Pin(27))

# Variable for delay
LEDdelay = 0

while True:
    print(pot.read_u16())
    #delay gets longer as pot turns up
    LEDdelay = pot.read_u16()/65000

    red.value(1)
    time.sleep(LEDdelay)
    red.value(0)

    yellow.value(1)
    time.sleep(LEDdelay)
    yellow.value(0)

    green.value(1)
    time.sleep(LEDdelay)
    green.value(0)



