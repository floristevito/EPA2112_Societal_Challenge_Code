import qrcode
from fpdf import FPDF


for i in range(2):
    fpdf1 = FPDF(orientation = 'L', unit = 'mm', format='A4')
    fpdf1.add_page()
    fpdf1.image("../../data/QR_Posters_v2.jpg", x=0, y=0, h=210)

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

    fpdf1.image("qr_{}.png".format(id), x=125, y=40, h=50)
    fpdf1.output("qr_poster_{}.pdf".format(id), 'F')