import asyncio
from datetime import datetime

import pigpio

from src import utils
from src.rgb import RGBController


@RGBController.effect('flash')
async def flash(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    on = data['color']
    off = [0, 0, 0]
    brightness = off
    
    while not rgbc.stop:
        for i, (k, v) in enumerate(rgbc.pins.items()):
            rgbc.set_PWM_dutycycle(v['pin'], brightness[i])
        
        rgbc.stop = utils.duration_check(target_time)

        brightness = on if brightness == off else off
        await asyncio.sleep(data['speed'])
    
    rgbc.apply()

@RGBController.effect('glow')
async def glow(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    color_diffs = [color / 255 for color in data['color']]
    color_mod = data['color'][:]
    direction = 0

    while not rgbc.stop:
        for i, (_, v) in enumerate(rgbc.pins.items()):
            if color_mod[i] >= data['color'][i] and data['color'][i] != 0:
                direction = 0
            if color_mod[i] <= 0 and data['color'][i] != 0:
                direction = 1

            if direction:
                color_mod[i] += color_diffs[i]
            else:
                color_mod[i] -= color_diffs[i]

            rgbc.set_PWM_dutycycle(v['pin'], color_mod[i])

        rgbc.stop = utils.duration_check(target_time)
        await asyncio.sleep(data['speed'])
    
    rgbc.apply()


@RGBController.effect('fade_in')
async def fade_in(rgbc, data):
    color_diffs = [color / 255 for color in data['color']]
    color = [0, 0, 0]

    while not rgbc.stop:
        for i, (_, v) in enumerate(rgbc.pins.items()):
            color[i] += color_diffs[i]
            if color[i] >= data['color'][i] and data['color'][i] != 0:
                rgbc.stop = True

            rgbc.set_PWM_dutycycle(v['pin'], color[i])

        await asyncio.sleep(data['speed'])

    rgbc.apply()


@RGBController.effect('fade_out')
async def fade_out(rgbc, data):
    color_diffs = [color / 255 for color in data['color']]
    color = data['color'][:]

    while not rgbc.stop:
        for i, (_, v) in enumerate(rgbc.pins.items()):
            color[i] -= color_diffs[i]
            if color[i] <= 0 and data['color'][i] != 0:
                rgbc.stop = True

            rgbc.set_PWM_dutycycle(v['pin'], color[i])

        await asyncio.sleep(data['speed'])

    rgbc.apply()