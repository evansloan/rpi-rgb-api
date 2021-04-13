import pigpio


class RGBController(pigpio.pi):
    
    effects = {}
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.pins = {
            'red': {
                'pin': 17,
                'value': 0
            },
            'green': {
                'pin': 24,
                'value': 0
            },
            'blue': {
                'pin': 22,
                'value': 0
            }
        }
        self.stop = False

    @classmethod
    def effect(cls, name):
        def wrapper(func): 
            cls.effects[name] = func
            return func
        return wrapper

    def update(self, data):
        self.stop = True

        for i, k in enumerate(self.pins):
            self.pins[k]['value'] = data['color'][i]

    def clear(self):
        for k in self.pins:
            self.pins[k]['value'] = 0
        
        self.stop = True
        self.apply()

    def apply(self):
        for _, color in self.pins.items():
            self.set_PWM_dutycycle(color['pin'], color['value'])

