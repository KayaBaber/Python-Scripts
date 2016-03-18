from __future__ import print_function
import PIL
import math
import numpy as np
from datetime import datetime
startTime = datetime.now()

def is_mandelbrot(real,imag):
    steps=100
    r,i=0,0
    for j in range(1,steps):
        r = r*r - i*i + real
        i = 2*r*i + imag
        magnitude=((r*r + i*i)**(0.5))
        if (np.isnan(magnitude)):
            return 200.0/j 
    return 'nope'


def color_wheel(angle):
    if angle=='nope':
        return (0,0,0)
    angle=angle*2*math.pi
    r=(0.5*math.cos(angle))+0.5
    g=(0.5*math.cos(angle+((2.0/3.0)*math.pi)))+0.5
    b=(0.5*math.cos(angle+((4.0/3.0)*math.pi)))+0.5
    return [int(r*255),int(g*255),int(b*255)]
    
    
def mandelPlot(center,zoom,res):
    baseZoom=3.0
    mandelImage=np.zeros((2*res,2*res,3))
    stepSize=baseZoom/(res*zoom)
    print(res*2)    
    for real in range(2*res):
        for imag in range(2*res):
            i=(imag*stepSize)+center[0]-(baseZoom/zoom)
            r=(real*stepSize)-center[1]-(baseZoom/zoom)
            mandelImage[real,imag]=color_wheel(is_mandelbrot(i,r))
        print(real,end="\r")
    print(real+1)
    return mandelImage


deepzoom=50
for i in range(deepzoom):
    multi=2**(i/4.0)
    center=(0.3,0)
    zoom=multi
    resolution=100*3
    mandelImage=mandelPlot(center, zoom, resolution)
    PIL.Image.fromarray(np.uint8(mandelImage)).save("mandel_zoom_"+str(resolution)+"_"+str(i)+".png")
    print('--------------\nLoop:'+str(i)+'\nExecution Duration: '+str(datetime.now() - startTime)+'\n----------------')