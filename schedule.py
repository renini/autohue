#!/usr/bin/python

# Set city
city_name = 'Denver'


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



# Astral Setup

a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
sun = city.sun(date=datetime.datetime.today(), local=True)



# Check Sunset and Sunrise and turn lights on

while True:
        if datetime.datetime.now(pytz.timezone('US/Mountain')) > sun['sunset'] a                                                                nd datetime.datetime.now(pytz.utc) > sun['sunrise']:
                b.set_light([4,5,6], 'on', True)
                b.set_light([4,5,6], 'bri', 254)
        elif datetime.datetime.now(pytz.timezone('US/Mountain')) > sun['sunrise'                                                                ] and datetime.datetime.now(pytz.utc) < sun['sunset']:
                lights_list = b.get_light_objects('list')
                for light in lights_list:
                  light.on = True
        time.sleep(60)
