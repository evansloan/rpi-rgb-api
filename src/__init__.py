import board
import neopixel
from sanic import Sanic

from src import rgb

app = Sanic(name='rgb-api')
rgbc = rgb.RGBController(
    board.D18,
    150,
    brightness=0.2,
    pixel_order=neopixel.GRB,
    auto_write=False
)

from src import effects
from src.routes import api

