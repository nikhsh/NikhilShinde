import qrcode
#qr = qrcode.make("hello welcome to world")
#qr.save('mycode.png')

qr = qrcode.QRCode(
	version=1,
	box_size=15,
#	bonder=5
	)

data = "https://www.facebook.com/profile.php?id=100004250956769"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill="black",black_color='white')
img.save('Nikhilshindefacebook.png')
