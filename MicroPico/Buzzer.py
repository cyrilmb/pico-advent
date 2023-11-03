from machine import Pin, PWM, ADC
import time

buzzer = PWM(Pin(13))
potentiometer = ADC(Pin(27))
red = Pin(18, Pin.OUT)
green = Pin(20, Pin.OUT)

count = 0
volume = 0

c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 515
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880

def BeepIt(note, duration):
    global count
    volume = potentiometer.read_u16()
    buzzer.duty_u16(volume)
    buzzer.freq(note)

    if count % 2 == 0 : 
        red.value(1) 
        time.sleep(duration) 
        red.value(0) 
    else: 
        green.value(1) 
        time.sleep(duration) 
        green.value(0) 
        buzzer.duty_u16(0) 
        time.sleep(0.050) 
        count += 1

def Part1():
    BeepIt(a, 0.5)
    BeepIt(a, 0.5)
    BeepIt(a, 0.5)
    BeepIt(f, 0.35)
    BeepIt(cH, 0.15)
    BeepIt(a, 0.5)
    BeepIt(f, 0.35)
    BeepIt(cH, 0.15)
    BeepIt(a, 0.65)
    time.sleep(0.5)
    BeepIt(eH, 0.5)
    BeepIt(eH, 0.5)
    BeepIt(eH, 0.5)
    BeepIt(fH, 0.35)
    BeepIt(cH, 0.15)
    BeepIt(gS, 0.5)
    BeepIt(f, 0.35)
    BeepIt(cH, 0.15)
    BeepIt(a, 0.65)
    time.sleep(0.5)

def Part2():
    BeepIt(aH, 0.5)
    BeepIt(a, 0.3)
    BeepIt(a, 0.15)
    BeepIt(aH, 0.5)
    BeepIt(gSH, 0.325)
    BeepIt(gH, 0.175)
    BeepIt(fSH, 0.125)
    BeepIt(fH, 0.125)
    BeepIt(fSH, 0.25)
    time.sleep(0.325)
    BeepIt(aS, 0.25)
    BeepIt(dSH, 0.5)
    BeepIt(dH, 0.325)
    BeepIt(cSH, 0.175)
    BeepIt(cH, 0.125)
    BeepIt(b, 0.125)
    BeepIt(cH, 0.25)
    time.sleep(0.35)

def Part3():
    BeepIt(f, 0.25)
    BeepIt(gS, 0.5)
    BeepIt(f, 0.35)
    BeepIt(a, 0.125)
    BeepIt(cH, 0.5)
    BeepIt(a, 0.375)
    BeepIt(cH, 0.125)
    BeepIt(eH, 0.65)
    time.sleep(0.5)

def Part4():
    BeepIt(f, 0.25)
    BeepIt(gS, 0.5)
    BeepIt(f, 0.375)
    BeepIt(cH, 0.125)
    BeepIt(a, 0.5)
    BeepIt(f, 0.375)
    BeepIt(cH, 0.125)
    BeepIt(a, 0.65)
    time.sleep(0.65)

Part1()
Part2()
Part3()
Part2()
Part4()

buzzer.duty_u16(0)