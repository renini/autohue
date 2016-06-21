#!/usr/bin/python

# Set city
city_name = 'city'


# Import all needed modules.

import datetime
import pytz
import time
import logging
from astral import Astral
from phue import Bridge



# Philips Hue Setup.

b = Bridge('ip_of_your_bridge')
b.connect()
b.get_api()
logging.basicConfig()
lights = 'off'


# Astral Setup

a = Astral()
a.solar_depression = 'civil'
city = a[city_name]



# Check Sunset and Sunrise and turn lights on

while True:
        sun = city.sun(date=datetime.datetime.today(), local=True)
        if datetime.datetime.now(pytz.timezone('US/Mountain')) > sun['sunset'] and datetime.datetime.now(pytz.utc) > sun['sunrise']:
                if lights == 'off':
                        b.set_light([4,5,6], 'on', True)
                        b.set_light([4,5,6], 'bri', 254)
                        lights = 'on'
        elif datetime.datetime.now(pytz.timezone('US/Mountain')) > sun['sunrise'] and datetime.datetime.now(pytz.utc) < sun['sunset']:
                if lights == 'on':
                        lights_list = b.get_light_objects('list')
                        for light in lights_list:
                                light.on = False
                        lights = 'off'
        time.sleep(60)
