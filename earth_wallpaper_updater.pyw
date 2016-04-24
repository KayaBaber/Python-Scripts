import ctypes
import os
import urllib
from PIL import Image
import datetime as dt

drive = "C:\\"
folder = "images"
image = "now.jpg"
image_path = os.path.join(drive, folder, image)
print("Downloading...")


extra1=""
extra2=""
extra3=""
extra4=""
t = dt.datetime.utcnow()

hour=t.hour
day=t.day
month=t.month
year=t.year
if (t.minute-30):
    hour-=1
if (hour)<0:
    day-=1
if day<0:
    month-=1
if month<0:
    year-=1
    
if month < 10:
    extra1="0"
if day < 10:
    extra2="0"   
if hour < 10:
    extra3="0"
if (((t.minute-30)%60)/10) == 0:
    extra4="0"
url = ("http://rammb.cira.colostate.edu/ramsdis/online/images/himawari-8/full_disk_ahi_true_color/full_disk_ahi_true_color_" +
       str(t.year)+
       extra1+str(month)+
       extra2+str(day)+
       extra3+str(hour)+
       extra4+str((((t.minute-30)%60)/10)*10)
       + "00.jpg")
print(url)
urllib.urlretrieve(url, image_path)
imNow = Image.open(image_path)



image = "before.jpg"
image_path = os.path.join(drive, folder, image)
print("Downloading...")
extra1=""
extra2=""
extra3=""
extra4=""
hour=t.hour
day=t.day
month=t.month
year=t.year
if (t.minute-30):
    hour-=1
if (hour-12)<0:
    day-=1
if day<0:
    month-=1
if month<0:
    year-=1
    
    
if month < 10:
    extra1="0"
if day < 10:
    extra2="0"   
if (t.hour-12)%24 < 10:
    extra3="0"
if (t.minute/10) == 0:
    extra4="0"
url = ("http://rammb.cira.colostate.edu/ramsdis/online/images/himawari-8/full_disk_ahi_true_color/full_disk_ahi_true_color_" +
       str(year)+
       extra1+str(month)+
       extra2+str(day)+
       extra3+str((t.hour-12)%24)+
       extra4+str((t.minute/10)*10)
       + "00.jpg")
print(url)
urllib.urlretrieve(url, image_path)
imBefore = Image.open(image_path)


image = "base.jpg"
image_path = os.path.join(drive, folder, image)
imBase = Image.open(image_path)


w, h = imNow.size
image = "cover.jpg"
cover_path = os.path.join(drive, folder, image)
cover = Image.open(cover_path)
imNow.paste(cover,(0,h-68))
imBefore.paste(cover,(0,h-68))

baseW, baseH = imBase.size

imBase.paste(imBefore,(240,165))

imBase.paste(imNow,(1280+570, 140))

image = "final.jpg"
image_path = os.path.join(drive, folder, image)

imBase.save(image_path,"JPEG")
SPI_SETDESKWALLPAPER = 20 
print("Setting Wallpaper...")
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
