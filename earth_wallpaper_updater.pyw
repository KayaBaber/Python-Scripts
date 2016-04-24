import ctypes
import os
import urllib
from PIL import Image
import datetime as dt

drive = "C:\\"
folder = "images"
image = "temp.jpg"
image_path = os.path.join(drive, folder, image)
print("Downloading...")
extra1=""
extra2=""
extra3=""
extra4=""
t = dt.datetime.now()
if t.month < 10:
    extra1="0"
if t.day < 10:
    extra2="0"   
if (t.hour+6)%24 < 10:
    extra3="0"
if (t.minute/10) == 0:
    extra4="0"
url = ("http://rammb.cira.colostate.edu/ramsdis/online/images/himawari-8/full_disk_ahi_true_color/full_disk_ahi_true_color_" +
       str(t.year)+
       extra1+str(t.month)+
       extra2+str(t.day)+
       extra3+str((t.hour+6)%24)+
       extra4+str((t.minute/10)*10)
       + "00.jpg")
print(url)
urllib.urlretrieve(url, image_path)
im = Image.open(image_path)
w, h = im.size
drive = "C:\\"
folder = "images"
image = "cover.jpg"
cover_path = os.path.join(drive, folder, image)
cover = Image.open(cover_path)
im.paste(cover,(0,h-68))
im.save(image_path,"JPEG")
SPI_SETDESKWALLPAPER = 20 
print("Setting Wallpaper...")
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 3)
