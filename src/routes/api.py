import asyncio

from sanic import response

from src import app, rgbc, utils


@app.post('/color')
async def update(request):
    data = utils.process_request(request.json, {'color': [tuple, int]})
    if not data:
        return response.text('Bad request body')

    rgbc.stop = True
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

    rgbc.stop = False
    asyncio.ensure_future(rgbc.effects[data['effect']](rgbc, data))

    return response.json(data)


@app.post('/clear')
async def clear(request):
    rgbc.clear()
