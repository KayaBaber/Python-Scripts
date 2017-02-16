from PIL import Image
import os
import math
from datetime import datetime as dt


def color_wheel(angle):
    if angle=='nope':
        return (0,0,0)
    angle=angle*2*math.pi
    r=(0.5*math.cos(angle))+0.5
    g=(0.5*math.cos(angle+((2.0/3.0)*math.pi)))+0.5
    b=(0.5*math.cos(angle+((4.0/3.0)*math.pi)))+0.5
    return (int(r*255),int(g*255),int(b*255))


def mandel_color(r, i, iter):
    z = 0
    for n in range(iter):
            if abs(z) > 2:
                return color_wheel(2/abs(z))
            z = z**2 + (xSc + ySc*(1j))
    return (0, 0, 0)


start = dt.now()
dir_path = os.path.dirname(os.path.realpath(__file__))
yPixels = 4000
xPixels = yPixels
mandelImage = Image.new("RGB", (xPixels, yPixels), "black")
mandelData = mandelImage.load()
scaleFactor = yPixels / 4.0
iterations = 50
for x in range(yPixels):
        for y in range(xPixels):
            xSc = x/scaleFactor - 2
            ySc = y/scaleFactor - 2
            mandelData[x, y] = mandel_color(xSc, ySc, iterations)
mandelImage.save(dir_path + "/mandel_" + str(yPixels) + "_" + str(iterations) + ".png")
    
print(dir_path + "/mandel_" + str(yPixels) + "_" + str(iterations) + ".png")
print("Total runtime:")
print(dt.now() - start)