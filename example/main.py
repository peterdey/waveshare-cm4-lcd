'''
Select images as required
True for image1  
False for image2
'''
Select = True
import time
import image 

Img = image.image()

while(1):
    if(Img.flgh):
        Img.HMI1() 
    else:
        Img.HMI2()


