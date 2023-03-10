import math
import numpy as np
import cv2
import time

def belongs(re,im,iterations,c):
    z = complex(re,im)
    con = c
    i = 0

    while(math.sqrt(z.real**2+z.imag**2)<2 and i < iterations):
        z = z*z+con
        i += 1
    
    return i


pixels = []
def pixel(x,y,Pcolor):
    pixels.append([x,y,Pcolor])




resumeI = 0

centerRe = 0
centerIm = 0

lenIm = 1
lenRe = lenIm*(4/3)

minRe = centerRe - lenRe/2
maxRe = centerRe + lenRe/2
minIm = centerIm - lenIm/2
maxIm = centerIm + lenIm/2

def draw(width,height,maxIterations,zoom,com,num):


    re = minRe

    reStep = (maxRe-minRe)/width
    imStep = (maxIm-minIm)/height




    while(re < maxRe):
        
        im = minIm
        while(im < maxIm):
            result = belongs(re,im,maxIterations,com)
            x = math.ceil((re-minRe)/reStep)-1
            y = math.ceil((im-minIm)/imStep)-1
            #if(len(pixels)%5000 == 0):
                #print(math.floor(width*height),len(pixels),str(round(len(pixels)/math.floor(width*height)*100,2))+"%", zoom, lenIm)

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
        status = cv2.imwrite("C:\\Users\\deopw\\Desktop\\Carpetas Generales\\DiegoPascualPython\\mandelbrot\\julia_collection_PNG\\julia_" +str(height)+"p_"+str(num)+".png" , imgBRG)
        if(status):
            print("success " + str(com.real) + "_" + str(com.imag) + "i")
        else:
            print("fail")
        cv2.waitKey(0)

c = complex(0.3413,0.3413)
iterations = 300
size = 2048

pixels = []
minRe = centerRe - lenRe/2
maxRe = centerRe + lenRe/2
minIm = centerIm - lenIm/2
maxIm = centerIm + lenIm/2

num = 0
start = time.time()
for i in range(125):
    start2 = time.time()
    num += 1
    pixels = []
    print(num)
    draw(math.floor(size*(4/3)),math.floor(size),iterations,i+resumeI,c+complex(i*0.0002656,i*0.0002656),num)
    print(round(time.time()-start2,2))
print("Done in " + str(round(time.time()-start,2)) + " seconds")
lenIm -= 1/((i+resumeI)*2+1)
lenRe = lenIm*(4/3)

#0.572994842303518
    