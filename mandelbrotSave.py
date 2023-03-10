import math
import numpy as np
import cv2
import random
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


pixels = []
def pixel(x,y,Pcolor):
    pixels.append([x,y,Pcolor])


resumeI = 0

centerRe = -0.75
centerIm = 0.1

lenIm = 1
lenRe = lenIm*(4/3)

minRe = centerRe - lenRe/2
maxRe = centerRe + lenRe/2
minIm = centerIm - lenIm/2
maxIm = centerIm + lenIm/2

def draw(width,height,maxIterations,zoom):


    re = minRe

    reStep = (maxRe-minRe)/width
    imStep = (maxIm-minIm)/height




    while(re < maxRe):
        
        im = minIm
        while(im < maxIm):
            result = belongs(re,im,maxIterations)
            x = math.ceil((re-minRe)/reStep)-1
            y = math.ceil((im-minIm)/imStep)-1
            if(len(pixels)%1000 == 0):
                print(math.floor(width*height),len(pixels),str(round(len(pixels)/math.floor(width*height)*100,2))+"%", zoom, lenIm)

            if(result == maxIterations):
                pixel(x,y,(0,0,0))
            else:
                h = 10 + round(360 * result * 1.0 / maxIterations)
                pColor = (h,150,240)
                pixel(x,y,pColor)
            im += imStep
        re += reStep


    if (len(pixels) >= math.floor(width*height)):

        # image of 100 x 100 pixels , with 3 channels 
        channels=3 
        color_bg=(0,0,0) 
        imgdim = (height, width, channels ) 
        blank_image = np.full(imgdim, color_bg, np.uint8)
        #Simple way to change the pixel(x=1,y=2) color to the (B=255,G=0,R=0) tuple color

        for i in pixels:
                blank_image[i[1],i[0]]= i[2]

        
        imgBRG = cv2.cvtColor(blank_image, cv2.COLOR_HLS2BGR)

        #cv2.imshow("mandelbrot", imgBRG)
        status = cv2.imwrite("C:\\Users\\deopw\\Desktop\\Carpetas Generales\\DiegoPascualPython\\mandelbrot\\mandelbrot_PNG\\MandelbrotVideo\\mandelbrot_" +str(height)+"p_"+str(zoom)+".png" , imgBRG)
        if(status):
            print("success")
        else:
            print("fail")
        cv2.waitKey(0)

size = 500
for i in range(1):
    pixels = []
    minRe = centerRe - lenRe/2
    maxRe = centerRe + lenRe/2
    minIm = centerIm - lenIm/2
    maxIm = centerIm + lenIm/2

    print(minRe,maxRe,":",minIm,maxIm)

    draw(math.floor(size*(4/3)),math.floor(size),500,i+resumeI)

    lenIm -= 1/((i+resumeI)*2+1)
    lenRe = lenIm*(4/3)

#0.572994842303518
    