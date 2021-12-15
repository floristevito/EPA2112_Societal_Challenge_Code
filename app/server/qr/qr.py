import qrcode

for i in range(20):
    id = 1400 + i
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://challenges.social/#/form/?qr_id={}'.format(id))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_{}.png".format(id))