import cv2
import numpy	

from time import sleep
from matplotlib import pyplot as plt

import zeep
from onvif import ONVIFCamera, ONVIFService
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue
zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

from onvif import ONVIFCamera
mycam1 = ONVIFCamera('192.168.15.42',80,'boshandi7','GtN0aXIBL9is','C:/Python27/wsdl/')
mycam2 = ONVIFCamera('192.168.15.43',80,'boshandi7','GtN0aXIBL9is','C:/Python27/wsdl/')

#catching streams
str42=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
str43=cv2.VideoCapture('rtsp://192.168.15.43:554/2')  

#creating histogram
#42
fig=plt.figure(figsize=(2, 4))
color = ('b','g','r')
ret,frame42=str42.read()
#cv2.imshow('qwerty',frame42)
hsv = cv2.cvtColor(frame42,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 4, 1)
plt.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 4, 2)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
    histr = cv2.calcHist([frame42],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    
#creating histogram
#43
ret,frame43=str43.read()
hsv = cv2.cvtColor(frame43,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 4, 3)
plt.imshow(hist,interpolation = 'nearest')
    
fig.add_subplot(2, 4, 4)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
    histr = cv2.calcHist([frame43],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])    

media42 = mycam1.create_media_service()
media_profile42 = media42.GetProfiles()[0]
image42 = mycam1.create_imaging_service()
token42 = media_profile42.VideoSourceConfiguration.SourceToken
SY42 = image42.create_type('GetImagingSettings')
SY42.VideoSourceToken = token42
request42 = image42.GetImagingSettings(SY42)
print(request42)

media43 = mycam2.create_media_service()
media_profile43 = media43.GetProfiles()[0]
image43 = mycam2.create_imaging_service()
token43 = media_profile43.VideoSourceConfiguration.SourceToken
SY43 = image43.create_type('GetImagingSettings')
SY43.VideoSourceToken = token43
request43 = image43.GetImagingSettings(SY43)
print(request43)

#Changing parameters into correct
b42=request42.Brightness
if b42 <48.0:
    print("Camera 42 Brightness")
    while b42 < 48.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness + 2.0
        print(request42.Brightness)
        b42 = b42+2.0
if b42 > 50.0:
    print("Camera 42 Brightness")
    while b42 > 50.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Brightness = request42.Brightness - 2.0
        print(request42.Brightness)
        b42 = b42 - 2.0
b43=request43.Brightness
if b43 <48.0:
    print("Camera 43 Brightness")
    while b43 < 48.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Brightness = request43.Brightness + 2.0
        print(request43.Brightness)
        b43 = b43+2.0
if b43 > 50.0:
    print("Camera 43 Brightness")
    while b43 > 50.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Brightness = request43.Brightness - 2.0
        print(request43.Brightness)
        b43 = b43 - 2.0      
       
s42=request42.ColorSaturation
if s42 <59.0:
    print("Camera 42 Saturation")
    while s42 <59.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation + 2.0
        print(request42.ColorSaturation)
        s42 = s42+2.0
if s42 > 61.0:
    print("Camera 42 Saturation")
    while s42 > 61.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.ColorSaturation = request42.ColorSaturation - 2.0
        print(request42.ColorSaturation)
        s42 = s42 - 2.0
s43=request43.ColorSaturation
if s43 <59.0:
    print("Camera 43 Saturation")
    while s43 <59.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.ColorSaturation = request43.ColorSaturation + 2.0
        print(request43.ColorSaturation)
        s43 = s43+2.0
if s43 > 61.0:
    print("Camera 43 Saturation")
    while s43 > 61.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.ColorSaturation = request43.ColorSaturation - 2.0
        print(request43.ColorSaturation)
        s43 = s43 - 2.0       
        
c42=request42.Contrast
if c42 <49.0:
    print("Camera 42 Contrast")
    while c42 <49.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast + 2.0
        print(request42.Contrast)
        c42 = c42+2.0
if c42 > 51.0:
    print("Camera 42 Contrast")
    while c42 > 51.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.Contrast = request42.Contrast - 2.0
        print(request42.Contrast)
        c42 = c42 - 2.0
c43=request43.Contrast
if c43 <49.0:
    print("Camera 43 Contrast")
    while s43 <49.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Contrast = request43.Contrast + 2.0
        print(request43.Contrast)
        c43 = c43+2.0
if c43 > 51.0:
    print("Camera 43 Contrast")
    while c43 > 51.0:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.Contrast = request43.Contrast - 2.0
        print(request43.Contrast)
        c43 = c43 - 2.0  
        
#White Balance
cr42 = request42.WhiteBalance.CrGain
cb42 = request42.WhiteBalance.CbGain   
#print(cb42,' ',cr42)  # cb 127 cr 0 nornally

if cr42 >41.0:
    print("Camera 42 White Balance Cr gain")
    while cr42 > 41.0: 
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.WhiteBalance.CrGain = request42.WhiteBalance.CrGain - 1.0
        print(request42.WhiteBalance.CrGain)
        cr42 = cr42 - 1.0
        cr42=request42.WhiteBalance.CrGain    
if cr42 <39.0:
    print("Camera 42 White Balance Cr gain")
    while cr42 <39.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.WhiteBalance.CrGain = request42.WhiteBalance.CrGain + 1.0
        print(request42.WhiteBalance.CbGain)
        cr42 = cr42+1.0
if cb42 >61.0:
    print("Camera 42 White Balance Cb gain")
    while cb42 > 61.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.WhiteBalance.CbGain = request42.WhiteBalance.CbGain -1.0
        print(request42.WhiteBalance.CbGain)
        cb42 = cb42 - 1.0  
if cb42 <59.0:
    print("Camera 42 White Balance Cb gain")
    while cb42 <59.0:
        image42.SetImagingSettings({'VideoSourceToken' : token42, 'ImagingSettings' : request42})
        request42.WhiteBalance.CbGain = request42.WhiteBalance.CbGain + 1.0
        print(request42.WhiteBalance.CbGain)
        cb42 = cb42 + 1.0  
        
cr43 = request43.WhiteBalance.CrGain
cb43 = request43.WhiteBalance.CbGain   

if cr43 >= 1.0:
    print("Camera 43 White Balance Cr gain")
    while cr43 >=1.0: 
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.WhiteBalance.CrGain = request43.WhiteBalance.CrGain - 1.0
        print(request43.WhiteBalance.CrGain)
        cr43 = cr43 - 1.0
        cr43=request43.WhiteBalance.CrGain
        
if cb43 <126.5:
    print("Camera 43 White Balance Cb gain")
    while cb43 <126.5:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.WhiteBalance.CbGain = request43.WhiteBalance.CbGain + 1.0
        print(request43.WhiteBalance.CbGain)
        cb43 = cb43+1.0
if cb43 >127.5:
    print("Camera 43 White Balance Cb gain")
    while cb43 > 127.5:
        image43.SetImagingSettings({'VideoSourceToken' : token43, 'ImagingSettings' : request43})
        request43.WhiteBalance.CbGain = request43.WhiteBalance.CbGain - 1.0
        print(request43.WhiteBalance.CbGain)
        cb43 = cb43 - 1.0  



#catching streams
str42=cv2.VideoCapture('rtsp://192.168.15.42:554/2')
str43=cv2.VideoCapture('rtsp://192.168.15.43:554/2') 

#creating histogram
#42
ret,frame42=str42.read()
hsv = cv2.cvtColor(frame42,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 4, 5)
plt.imshow(hist,interpolation = 'nearest')

fig.add_subplot(2, 4, 6)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
    histr = cv2.calcHist([frame42],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
    
#creating histogram
#43
ret,frame43=str43.read()
hsv = cv2.cvtColor(frame43,cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0,1], None, [180, 256], [0, 180, 0, 256]) #hue 180 saturation 256
fig.add_subplot(2, 4, 7)
plt.imshow(hist,interpolation = 'nearest')
    
fig.add_subplot(2, 4, 8)
for i,col in enumerate(color): #each value corresponds to number of pixels in that image with its corresponding pixel value RGB
    histr = cv2.calcHist([frame43],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
