import asyncio
from datetime import datetime

import pigpio

from src import utils
from src.rgb import RGBController


@RGBController.effect('flash')
async def flash(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    on = data['color']
    off = (0, 0, 0)
    is_on = False
    
    while not rgbc.stop:
        if is_on:
            rgbc.fill(off)
        else:
            rgbc.fill(on)

        rgbc.show()
        is_on = not is_on

        rgbc.stop = utils.duration_check(target_time)
        await asyncio.sleep(data['speed'])
    
    rgbc.apply()


@RGBController.effect('glow')
async def glow(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    color_diffs = [c / 255 for c in data['color']]
    color = data['color'][:]
    direction = 0

    while not rgbc.stop:
        for new_val, og_val in zip(color, data['color']):
            if new_val >= og_val and og_val != 0:
                direction = 0
            if new_val <= 0 and og_val != 0:
                direction = 1

        if direction:
            color = [c + diff for (c, diff) in zip(color, color_diffs)]
        else:
            color = [c - diff for (c, diff) in zip(color, color_diffs)]

        rgbc.fill(tuple([int(c) for c in color]))
        rgbc.show()

        rgbc.stop = utils.duration_check(target_time)
        await asyncio.sleep(data['speed'])
    
    rgbc.apply()


@RGBController.effect('fade_in')
async def fade_in(rgbc, data):
    color_diffs = [i / 255 for i in data['color']]
    color = [0, 0, 0]

    while not rgbc.stop:
        color = [i + diff for (i, diff) in zip(color, color_diffs)]
        for new_val, og_val in zip(color, data['color']):
            if new_val >= og_val and og_val != 0:
                rgbc.stop = True

        rgbc.fill(tuple([int(c) for c in color]))
        rgbc.show()

        await asyncio.sleep(data['speed'])

    rgbc.apply()


@RGBController.effect('fade_out')
async def fade_out(rgbc, data):
    color_diffs = [i / 255 for i in data['color']]
    color = data['color']

    while not rgbc.stop:
        color = [i - diff for (i, diff) in zip(color, color_diffs)]
        for new_val, og_val in zip(color, data['color']):
            if new_val <= 0 and og_val != 0:
                rgbc.stop = True

        rgbc.fill(tuple([int(c) for c in color]))
        rgbc.show()

        await asyncio.sleep(data['speed'])

    rgbc.apply()


@RGBController.effect('race')
async def race(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    blank = (0, 0, 0)
    rgbc.fill(blank)
    rgbc.show()

    length = 20

    while not rgbc.stop:
        for i in range(rgbc.n):
            rgbc[i] = data['color']

            for j, k  in zip(range(1, length), range(length, 1, -1)):
                rgbc[i - j] = tuple([int(c * (k / 100)) for c in data['color']])
            
            rgbc[i - length] = blank
            rgbc.show()

            rgbc.stop = utils.duration_check(target_time)
            await asyncio.sleep(data['speed'])

    rgbc.apply()


@RGBController.effect('ants')
async def ants(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    blank = (0, 0, 0)
    rgbc.fill(blank)
    rgbc.show()


    active = 0
    while not rgbc.stop:

        if active:
            for i in range(0, rgbc.n, 2):
                rgbc[i] = data['color']
            for i in range(1, rgbc.n, 2):
                rgbc[i] = blank
        else:
            for i in range(0, rgbc.n, 2):
                rgbc[i] = blank
            for i in range(1, rgbc.n, 2):
                rgbc[i] = data['color']

        rgbc.show()

        active = not active
        rgbc.stop = utils.duration_check(target_time)
        await asyncio.sleep(data['speed'])

    rgbc.apply()


@RGBController.effect('zipper')
async def zipper(rgbc, data):
    target_time = utils.set_duration(data['duration'])

    blank = (0, 0, 0)
    rgbc.fill(blank)
    rgbc.show()

    active = 0
    while not rgbc.stop:
        if active:
            for i in range(0, rgbc.n, 2):
                rgbc[i] = data['color']
                rgbc.show()
            for i in range(1, rgbc.n, 2):
                rgbc[i] = blank
                rgbc.show()
        else:
            for i in range(0, rgbc.n, 2):
                rgbc[i] = blank
                rgbc.show()
            for i in range(1, rgbc.n, 2):
                rgbc[i] = data['color']
                rgbc.show()

        active = not active
        rgbc.stop = utils.duration_check(target_time)
        await asyncio.sleep(data['speed'])

    rgbc.apply()
