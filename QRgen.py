import qrcode


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,#Don't change this.
                   box_size=50,#This changes how big the code will be.
                   border=2) #This changes how big/thicc the border of the qrcode will be.

print("What text/url would you like to have be turned into a QR code?: ")
data = input()

print("Converting...")
img = qrcode.make(data)
print("Done!")
print("\nMake sure to move code.png to another folder and rename it to whatever before making a new QRcode!")
img = qr.make_image(fill_color="black", back_color="white") #This changes the qrcode's look/what colors are used.
name = input('What would you like the name of the code called?: ')
img.save(name)
