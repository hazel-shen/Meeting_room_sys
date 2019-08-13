## you can fix the code with this comment.

from Adafruit_AMG88xx import Adafruit_AMG88xx
import pygame
import os
import math
import time
import redis
import numpy as np
import requests
import os
 
from scipy.interpolate import griddata

from colour import Color

conn = redis.Redis(
  host=os.environ['REDIS_HOST'],
  port=os.environ['REDIS_PORT'],
  password=os.environ['REDIS_AUTH'])

#low range of the sensor (this will be blue on the screen)
MINTEMP = 28

#high range of the sensor (this will be red on the screen)
MAXTEMP = 32

#how many color values we can have
COLORDEPTH = 2048

os.putenv('SDL_FBDEV', '/dev/fb1')
##pygame.init()

#initialize the sensor
sensor = Adafruit_AMG88xx()

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

#sensor is an 8x8 grid so lets do a square
height = 240
width = 240

#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))

#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

displayPixelWidth = width / 30
displayPixelHeight = height / 30

##lcd = pygame.display.set_mode((width, height))
##lcd.fill((255,0,0))
##pygame.display.update()
##pygame.mouse.set_visible(False)
##lcd.fill((0,0,0))
##pygame.display.update()

#some utility functions
def constrain(val, min_val, max_val):
  return min(max_val, max(min_val, val))

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#let the sensor initialize
time.sleep(.1)
	
while(1):
	#read the pixels
	pixels = sensor.readPixels()
  payload = {'pixels': " ".join(str(i) for i in pixels)}
  try:
    print 'Set Record:', conn.set("pixels-501", " ".join(str(i) for i in pixels))
  except Exception as ex:
    print 'Error:', ex
  ##  if(sum(1 for i in pixels if i > 29.5) > 6):
  ##      headers = {'Authorization':'Bearer ${LINE-Notify-token}}
  ##      form = {'message': 'There is someone!'}
  ##      response = requests.post('https://notify-api.line.me/api/notify', data=form, headers = headers)

	pixels = [map(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]	
	#perdorm interpolation
	bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
	
	#draw everything
  ##	for ix, row in enumerate(bicubic):
  ##		for jx, pixel in enumerate(row):
  ##			pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)], (displayPixelHeight * ix, displayPixelWidth * jx, displayPixelHeight, displayPixelWidth))
	time.sleep(1)
  ##	pygame.display.update()
