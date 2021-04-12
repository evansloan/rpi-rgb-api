# RGB API

A simple asynchronous RESTful API used to control an LED strip connected to a Raspberry Pi

Written in Python using [Sanic](https://github.com/sanic-org/sanic) async web framework

LEDs are wired in the below configuration

![](https://i.imgur.com/qEZ0Fu7.png)

## Starting the API

Requires Python >= 3.7

1. Install PiGPIO

`wget http://abyz.me.uk/rpi/pigpio/pigpio.zip && unzip pigpio.zip && cd PIGPIO && sudo make install`

2. Clone rpi-rgb-api

`git clone https://github.com/evansloan/rpi-rgb-api && cd rpi-rgb-api`

3. Install requirements

`pip install -r requirements.txt`

4. Run PiGPIO

`sudo pigpiod`

5. Run web server

`python app.py`

## Using the API

Now that the server is running, endpoints can be accessed at `<RASPBERRY_PI_IP>:8000/`

Available endpoints are located in `src/routes/api.py`

### To set the LEDs to a static color:

```
curl -H "Content-Type: application/json" -d '{"color": [0,255,0]}' http://192.168.10.164:8000/update
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
