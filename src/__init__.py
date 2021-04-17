import os

from sanic import Sanic

from src import rgb

app = Sanic(name='rgb-api')
app.update_config(os.getenv('RGB_API_CONFIG', 'src.config.BaseConfig'))

rgbc = rgb.RGBController(
    app.config['PIN'],
    app.config['PIXEL_COUNT'],
    brightness=app.config['BRIGHTNESS'],
    pixel_order=app.config['PIXEL_ORDER'],
    auto_write=app.config['AUTO_WRITE']
)

from src import effects
from src.routes import api

@app.listener('before_server_stop')
async def before_server_stop(app, loop):
    rgbc.color = (0, 0, 0)
    rgbc.apply()
