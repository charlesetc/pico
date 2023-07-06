from machine import Pin, Timer
import time
from random import randint, random


led = Pin('LED', Pin.OUT)
out1 = Pin(0, Pin.OUT)
in1 = Pin(1, Pin.IN, Pin.PULL_DOWN)

out2 = Pin(2, Pin.OUT)
in2 = Pin(3, Pin.IN, Pin.PULL_DOWN)

out3 = Pin(4, Pin.OUT)
in3 = Pin(5, Pin.IN, Pin.PULL_DOWN)

out4 = Pin(6, Pin.OUT)
in4 = Pin(7, Pin.IN, Pin.PULL_DOWN)

led.value(1)
time.sleep(0.2)
led.value(0)

out1.value(0)
out2.value(0)
out3.value(0)
out4.value(0)

state = 'off'
direction = 'incr'

timer = Timer()
period = 100

def delayTimer(by):
    timer.deinit()
    Timer().init(mode=Timer.ONE_SHOT, period=by, callback=lambda t: timer.init(period=period, mode=Timer.PERIODIC, callback=nextLight))

def nextLight(timer):
    global state, direction
    if state == 0:
        if random() > 0.5:
            direction = 'decr'
            state = 4
        else:
            direction = 'incr'
            state = 1

    elif state == 1 and direction == 'incr':
        state = 2
    elif state == 2 and direction == 'incr':
        state = 3
    elif state == 3 and direction == 'incr':
        state = 4
    elif state == 4 and direction == 'incr':
        state = 0
        delayTimer(randint(100, 3000))

    elif state == 4 and direction == 'decr':
        state = 3
    elif state == 3 and direction == 'decr':
        state = 2
    elif state == 2 and direction == 'decr':
        state = 1
    elif state == 1 and direction == 'decr':
        state = 0
        delayTimer(randint(100, 3000))


while True:

    if state == 'off' and (
        in1.value() == 1 \
        or in2.value() == 1 \
        or in3.value() == 1 \
        or in4.value() == 1):
        state = 0
        delayTimer(300)

    if (state == 1 and in1.value() == 1 \
        or state == 2 and in2.value() == 1 \
        or state == 3 and in3.value() == 1 \
        or state == 4 and in4.value() == 1):
        state = 'win'
        timer.deinit()

    if state == 1:
        out1.value(1)
    else:
        out1.value(0)

    if state == 2:
        out2.value(1)
    else:
        out2.value(0)

    if state == 3:
        out3.value(1)
    else:
        out3.value(0)

    if state == 4:
        out4.value(1)
    else:
        out4.value(0)

    if state == 'win':
        out1.value(0)
        out2.value(0)
        out3.value(0)
        out4.value(0)
        out1.value(0)
        time.sleep(0.1)
        out1.value(1)
        out2.value(1)
        out3.value(1)
        out4.value(1)
        time.sleep(0.1)
        out1.value(0)
        out2.value(0)
        out3.value(0)
        out4.value(0)
        time.sleep(0.1)
        out1.value(1)
        out2.value(1)
        out3.value(1)
        out4.value(1)
        time.sleep(0.1)
        out1.value(0)
        out2.value(0)
        out3.value(0)
        out4.value(0)
        time.sleep(0.1)
        out1.value(1)
        out2.value(1)
        out3.value(1)
        out4.value(1)
        time.sleep(0.1)
        out1.value(0)
        out2.value(0)
        out3.value(0)
        out4.value(0)
        time.sleep(0.1)
        out1.value(1)
        out2.value(1)
        out3.value(1)
        out4.value(1)
        time.sleep(1.8)
        out1.value(0)
        out2.value(0)
        out3.value(0)
        out4.value(0)

        state = 'off'
        timer.deinit()

#
# buttonPressed = False
#
# while True: 
#     if in1.value() == 1 and buttonPressed == False:
#         buttonPressed = True
#         led.toggle()
#         out1.value(1)
#
#     if in1.value() == 0 and buttonPressed == True:
#         buttonPressed = False
#         out1.value(0)
#
#     time.sleep(0.01)
