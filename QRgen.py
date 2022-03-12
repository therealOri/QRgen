import qrcode


#Default
##-------------------------------------------##
"""
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=1,
"""
##-------------------------------------------##


#QR config
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)


#Set what the QR code will contain.
data = input("What data would you like to put int the QR code?: ")
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white") #Can be changed.

#Give a name for the QR code image/file.
file_name = input("Output file name: ")
img.save(file_name)
