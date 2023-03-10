from asyncio import events
import arcade
import math

def clamp(value, min_value, max_value):
	return max(min_value, min(max_value, value))

def saturate(value):
	return clamp(value, 0.0, 1.0)

def hue_to_rgb(h):
	r = abs(h * 6.0 - 3.0) - 1.0
	g = 2.0 - abs(h * 6.0 - 2.0)
	b = 2.0 - abs(h * 6.0 - 4.0)
	return saturate(r), saturate(g), saturate(b)

def hsl_to_rgb(h, s, l):
	r, g, b = hue_to_rgb(h)
	c = (1.0 - abs(2.0 * l - 1.0)) * s
	r = (r - 0.5) * c + l
	g = (g - 0.5) * c + l
	b = (b - 0.5) * c + l
	return r, g, b

def belongs(re,im,iterations):
    z = complex(0,0)
    c = complex(re,im)
    i = 0

    while(math.sqrt(z.real**2+z.imag**2)<2 and i < iterations):
        z = z*z+c
        i += 1
    
    return i



size = 1

pixels = []
def pixel(x,y,Pcolor):
    pixels.append([x,y,Pcolor])

minRe = -2
maxRe = 1
minIm = -1
maxIm = 1

re = minRe

arcade.open_window(round(size*1.5), round(size), "test")

arcade.set_background_color(arcade.color.WHITE)

reStep = (maxRe-minRe)/(size*1.5)
imStep = (maxIm-minIm)/size

im = minIm

def draw(deltaTime):



    global re
    global im

    maxIterations = 2500

    arcade.start_render()
    if(len(pixels)%10000 == 0):
        print(math.floor(size**2 * 1.5),len(pixels))

    if (len(pixels) >= math.floor(size**2 * 1.5 )):
        for i in pixels:
            arcade.draw_point(i[0],i[1],i[2],1)

    if(re < maxRe):
        if(im >= maxIm):
            im = minIm
            re += reStep
        if(im < maxIm):
            result = belongs(re,im,maxIterations)
            x = (re-minRe)/reStep 
            y = (im-minIm)/imStep

            if(result == maxIterations):
                pixel(x,y,arcade.color.BLACK)
            else:
                h = 30 + round(120 * result * 1.0 / maxIterations)
                pColor = hsl_to_rgb(h,100,50)
                pixel(x,y,pColor)
            print(pixels)

            im += imStep

    arcade.finish_render()

arcade.schedule(draw, 1/1000000)
arcade.run()
