from PyEcoder.PyEcoder import Encoder
import RPi.GPIO as GPIO
import time

enc = Encoder(14, 15, 3, debug=False)

val = 0
def turn(direction):
    global val
    val += 1 if direction else -1
    print(val)

enc.on_click(lambda: print('click'))
enc.on_turn(turn)

try:  
    print('waiting forever')
    while True:
          time.sleep(1)
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
