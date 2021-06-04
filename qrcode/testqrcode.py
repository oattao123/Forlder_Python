import qrcode 
import tkinter
size = int(input("box size :"))
char1 = input("char :")
color = input("color :")
qr = qrcode.QRCode(
    version=1,
    box_size=size,
    border=5
)
data = char1 
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color=color)
img.save('qrcode1.png')