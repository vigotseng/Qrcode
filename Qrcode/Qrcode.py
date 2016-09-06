#-*-coding: utf-8-*-

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

file = open('test.txt')
r = file.readlines()
print r
for i in r:
    qr.add_data('%s'%i)
    print i
qr.make(fit=True)

img = qr.make_image()
img.save('1.png')
