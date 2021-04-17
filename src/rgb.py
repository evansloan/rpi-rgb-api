import neopixel


class RGBController(neopixel.NeoPixel):
    
    effects = {}
    
    def __init__(self, pwm_pin, pixel_count, **kwargs):
        super().__init__(pwm_pin, pixel_count, **kwargs)
        
        self.color = (0, 0, 0)
        self.stop = False

    @classmethod
    def effect(cls, name):
        def wrapper(func): 
            cls.effects[name] = func
            return func
        return wrapper

    def clear(self):
        self.stop = True
        self.color = (0, 0, 0)
        self.apply()

    def apply(self):
        self.fill(self.color)
        self.show()
