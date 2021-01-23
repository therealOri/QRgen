import qrcode


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=50,
                   border=2)

print("What text/url would you like to have be turned into a QR code?: ")
data = input()

print("Converting...")
img = qrcode.make(data)
print("Done!")
print("\nMake sure to move code.png to another folder before making a new QRcode!")
img = qr.make_image(fill_color="black", back_color="white")
img.save("code.png")