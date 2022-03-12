import qrcode
import os


#Default
"""
version=1,
error_correction=qrcode.constants.ERROR_CORRECT_L,
box_size=10,
border=1,
"""


def clear():
    os.system("cls||clear")


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=1,
)

data = input("What data would you like to put int the QR code?: ")
clear()
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")


file_name = input("Output file name: ")
clear()
img.save(file_name)
print(f"Created QR code: {file_name}")


