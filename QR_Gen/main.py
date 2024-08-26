# import the pyqrcode 
import pyqrcode
import png  #  for png image


# take user input
# this is the text for which we want to generate a QR code
text = input("Enter the text to generate QR code: ")

# create a pyqrcode object by calling the create() method
# we will use our text as an argument
qr_code = pyqrcode.create(text)

# calling the svg() method of the qr_code object 
# creates the file named qr_code.svg in svg format
# the scale argument sets how large to draw a single image
qr_code.png('qr_code.png', scale = 8)