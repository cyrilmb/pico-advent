# DAY 1 ~ blinking the onboard LED

# from machine import Pin
# from time import sleep

# onboardLED = Pin(25, Pin.OUT)

# print("LED starts flashing...")
# while True:
#     try:
#         onboardLED.toggle()
#         sleep(1) # sleep 1sec
#     except KeyboardInterrupt:
#         break
# onboardLED.off()
# print("Finished.")


# DAY 2 ~ colored LEDs, resistors and jumper cables

# from machine import Pin
# import time

# onboardLED = Pin(25, Pin.OUT)

# red = Pin(18, Pin.OUT)
# yellow = Pin(19, Pin.OUT)
# green = Pin(20, Pin.OUT)

# red.value(1)
# yellow.value(1)
# green.value(1)

# time.sleep(5)

# red.value(0)
# yellow.value(0)
# green.value(0)

# counter = 1 #Setting the counter

# while counter < 11:
#     print(counter)
#     #LEDS on
#     red.value(1)
#     yellow.value(1)
#     green.value(1)

#     time.sleep(0.5)

#     #LEDs off
#     red.value(0)
#     yellow.value(0)
#     green.value(0)

#     time.sleep(0.5)

#     counter += 1


# # Cycle through each LED color
# counter = 1

# while counter < 15:
#     onboardLED.value(1)
#     print(counter)

#     red.value(1)
#     yellow.value(0)
#     green.value(0)
#     time.sleep(0.2)

#     red.value(0)
#     yellow.value(1)
#     green.value(0)
#     time.sleep(0.2)

#     red.value(0)
#     yellow.value(0)
#     green.value(1)
#     time.sleep(0.2)

#     onboardLED.value(0)
#     green.value(0)

#     counter += 1


# Day 3 ~ adding buttons to activate responses on the PICO

# Imports
# from machine import Pin
# import time

# # Set button name with GPIO pin number, set the pin as INPUT and use pull down
#     #Pull down is a builtin funcionality on the controller to lower the voltage in the GPIO pin so that it 
#     #registers the 3.3V signal sent by the button. Pins can float between 0V-3.3V, so it can't detect the signal.
# button1 = Pin(13, Pin.IN, Pin.PULL_DOWN) 
# button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
# button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# # LED names and GPIO pin numbers
# red = Pin(18, Pin.OUT)
# yellow = Pin(19, Pin.OUT)
# green = Pin(20, Pin.OUT)

# onboardLED = Pin(25, Pin.OUT)

# while True: # forever and ever loop
#     time.sleep(0.2) # quick nap

#     if button1.value() == 1:
#         print('NOOO YOU PUSHED THE WRONG BUTTON')
#         green.value(1)

#     elif button2.value() == 1:
#         print('WHY WOULD YOU PUSH THAT ONE')
#         yellow.value(1)

#     elif button3.value() == 1:
#         print('THANK GOD YOU DIDNT PUSH THE LAST BUTTON WAIT NOOOO')
#         red.value(1)
    
#     else:
#         green.value(0)
#         yellow.value(0)
#         red.value(0)
#         onboardLED.toggle()
