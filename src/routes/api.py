import asyncio

from sanic import response

from src import app, rgbc, utils


@app.post('/color')
async def color(request):
    data = utils.process_request(request.json, {'color': [tuple, int]})
    if not data:
        return response.text('Bad request body')

    rgbc.stop_effect()

    rgbc.color = data['color']
    rgbc.apply()

    return response.json(data)


@app.route('/effect', methods=['GET', 'POST'])
async def effect(request):
    if request.method == 'GET':
        return response.json([effect_name for effect_name in rgbc.effects])

    data = utils.process_request(request.json, {
        'effect': [str], 
        'color': [tuple, int],
        'speed': [float],
        'duration': [int]
    })
    if not data:
        return response.text('Bad request body')

    rgbc.stop_effect()
    rgbc.set_effect(data)

    return response.json(data)


@app.post('/clear')
async def clear(request):
    rgbc.clear()
    return response.json({'color', [0, 0, 0]})
