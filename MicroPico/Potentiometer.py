#imports
from machine import ADC, Pin, PWM
import time

# LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
yellow = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

# Pot goes on ADC pin 27
potentiometer = ADC(Pin(27))

# ## CYCLING LEDS
# # Variable for delay
# LEDdelay = 0

# while True:
#     print(potentiometer.read_u16())
#     #delay gets longer as pot turns up
#     LEDdelay = potentiometer.read_u16()/65000

#     red.value(1)
#     time.sleep(LEDdelay)
#     red.value(0)

#     yellow.value(1)
#     time.sleep(LEDdelay)
#     yellow.value(0)

#     green.value(1)
#     time.sleep(LEDdelay)
#     green.value(0)


## PULSE WIDTH MODULATION

# Set LED pin with PWM
led = PWM(Pin(18))

# Set the PWM frequency (of switching on and off)
led.freq(1000)

reading = 0

while True:
    reading = potentiometer.read_u16()
    print(reading)

    # Set PWM duty cycle to pot reading
    led.duty_u16(reading)

    time.sleep(0.1)
