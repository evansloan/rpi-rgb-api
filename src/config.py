import board
import neopixel

class BaseConfig:
    # Server settings
    HOST = '0.0.0.0'
    PORT = 8000

    # RGBController settings
    AUTO_WRITE = False
    BRIGHTNESS = 0.2
    DEBUG = False
    PIN = board.D18
    PIXEL_COUNT = 150
    PIXEL_ORDER = neopixel.GRB


class DevConfig(BaseConfig):
    DEBUG = True