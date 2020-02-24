import pyqrcode 
from pyqrcode import QRCode 

# Take input(link or text)    
print("Please eneter the data")
text_or_a_link = input()
  
# Generate QR code 
url = pyqrcode.create(text_or_a_link) 
#save QR code   
url.svg("qrcode.svg", scale = 8) 