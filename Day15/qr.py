import qrcode

son = 'https://www.instagram.com/hm_son7/'
qr = qrcode.make(son)
qr.save('son.png')