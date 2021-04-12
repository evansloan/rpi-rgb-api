from sanic import Sanic

from src import rgb

app = Sanic(name='rgb-api')
rgbc = rgb.RGBController()

from src import effects
from src.routes import api

