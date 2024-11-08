import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://www.youtube.com/watch?v=K-a8s8OLBSE&list=PLmU8B4gZ41icKdheg4d2KZBgDR1wSWfbH&index=2")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("TS.png")
