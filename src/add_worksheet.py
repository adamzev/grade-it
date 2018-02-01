from libs.pdfCanvas import PdfCanvas
from libs.drawProblem import DrawProblem
from libs.basicOpProblem import BasicOpProblem
import qrcode
from qrcode.image.pure import PymagingImage
from reportlab.lib.utils import ImageReader


number_of_probs = 16
number_of_cols = 2

pdf = PdfCanvas("add_worksheet")
c = pdf.c
pdf.set_prob_layout(number_of_probs, number_of_cols)
font='Courier'

c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)
c.setFont(font, 16)

header_rect = pdf.get_header_rect()
company_name = "Tiny-Robot"
subject = "Addition"
instructions = ""
name = "Name: ______________"
date = "Date: ______________"
c.drawString(header_rect[0], header_rect[1], company_name)
c.drawString(header_rect[0], header_rect[1] - 25, subject)
c.drawString(header_rect[0] + 140, header_rect[1], name)
c.drawString(header_rect[0] + 140, header_rect[1] - 25, date)



ans_txt = ""
for i in range(1, number_of_probs + 1):
    prob_rect = pdf.get_rect_for_prob_num(i)
    c.drawString(prob_rect[0], prob_rect[1], str(i)+")")
    prob = BasicOpProblem("add")
    prob.set_nums(1, 99)
    DrawProblem.drawBasicOpProblem(prob_rect, prob, pdf, 'vert')
    ans_txt+= str(i)+") " + str(prob.ans) + '\n'

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 2,
    border = 4,
)

# Add data
qr.add_data(ans_txt)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.png")
rlImg = ImageReader('image.png')
c.drawImage(rlImg, header_rect[0] + 375, header_rect[1] - 90)

c.showPage()
c.save()
