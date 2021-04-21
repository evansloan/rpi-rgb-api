import asyncio

import neopixel

from src import utils


class RGBController(neopixel.NeoPixel):
    
    effects = {}
    
    def __init__(self, pwm_pin, pixel_count, **kwargs):
        super().__init__(pwm_pin, pixel_count, **kwargs)
        self.color = (0, 0, 0)
        self.running_effect = None

    @classmethod
    def effect(cls, name):
        def wrapper(func): 
            cls.effects[name] = func
            return func
        return wrapper

    def clear(self):
        self.stop_effect()
        self.color = (0, 0, 0)
        self.apply()

    def apply(self):
        self.fill(self.color)
        self.show()

    def set_effect(self, data):
        self.running_effect = asyncio.ensure_future(self.effects[data['effect']](self, data))

    def stop_effect(self):
        if self.running_effect is not None:
            self.running_effect.cancel()
            self.running_effect = None
            self.apply()
