# RGB API

A simple asynchronous RESTful API used to control a ws2812b LED strip connected to a Raspberry Pi

Written in Python using [Sanic](https://github.com/sanic-org/sanic) async web framework

LEDs are wired in the below configuration

![](https://i.imgur.com/s5mho2P.png)

## Starting the API

Requires Python >= 3.7

1. Clone rpi-rgb-api

`git clone https://github.com/evansloan/rpi-rgb-api && cd rpi-rgb-api`

2. Install requirements

`pip install -r requirements.txt`

3. Run web server

`sudo python app.py`

## Using the API

Now that the server is running, endpoints can be accessed at `<RASPBERRY_PI_IP>:8000/`

Available endpoints are located in `src/routes/api.py`

### To set the LEDs to a static color:

```
curl -H "Content-Type: application/json" -d '{"color": [0,255,0]}' http://192.168.10.164:8000/color
```

Request body params:

`color`: Array containing RGB values for the desired color

### Apply an effect to the LEDs:

Available effects are located in `src/effects.py`

```
curl -H "Content-Type: application/json" \
-d '{"effect": "flash", "color": [0,255,0]}, "duration": 10, "speed": 0.3}' \
http://192.168.10.164:8000/effect
```

Request body params:

`effect`: The name of the effect

`color`: Array containing RGB values for the desired color

`duration`: The duration of the effect in seconds (set to 0 for infinite duration)

`speed`: The speed of the effect in seconds
