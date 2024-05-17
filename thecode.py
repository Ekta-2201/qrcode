import qrcode

from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=8,border=4,) # type: ignore

qr.add_data("https://www.linkedin.com/in/ek-ta-a6943924a/")
qr.make(fit=True)
img=qr.make_image(fill_color="pink",back_color="black")
img.save("mylinkdinaccount.png")