from RPi import GPIO
from time import sleep

class Encoder:

    def __init__(self, clk, dt, btn=None, steps=2, debug=False):
        self.clk = clk
        self.dt = dt
        self.btn = btn
        self.steps = steps
        self.delta = 0
        self.debug = debug

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        self._last_clk_state = GPIO.input(clk)

        GPIO.add_event_detect(self.clk, GPIO.FALLING, callback=self._int_callback, bouncetime=5)
        
        if btn is not None:
            if self.debug:
                print('setting up button on pin {}'.format(btn))
            GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(self.btn, GPIO.FALLING, callback=self._click_int_callback, bouncetime=300)

    def _int_callback(self, channel):
        current_clk_state = GPIO.input(self.clk)
        if self.debug:
            print('interrupt called, new clock state={}'.format(current_clk_state))

        if current_clk_state != self._last_clk_state:
            dt_state = GPIO.input(self.dt)
            if dt_state != current_clk_state and self._click_callback is not None:
                # Clockwise Step
                self.delta +=1

                if self.debug:
                    print('clockwise turn detected')
                
                if self.delta >= self.steps:
                    self._turn_callback(True)
                    self.delta = 0
            else:
                # Counter-Clockwise Step
                self.delta -= 1

                if self.debug:
                    print('counter clockwise turn detected')
                
                if -self.delta >= self.steps: 
                    self._turn_callback(False)
                    self.delta = 0

            self._last_clk_state = current_clk_state

    def _click_int_callback(self, channel):
        if self._click_callback is not None:
            self._click_callback()

    def on_turn(self, callback):
        self._turn_callback = callback
    
    def on_click(self, callback):
        self._click_callback = callback


