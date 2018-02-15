from libs.pdfCanvas import PdfCanvas
import random
import PyPDF2
from reportlab.pdfgen import canvas
from time import gmtime, strftime

number_of_probs = random.randint(2, 30)
print(number_of_probs)
number_of_cols = random.randint(1,5)

pdf = PdfCanvas("prob_nums")
c = pdf.c
pdf.set_prob_layout(number_of_probs, number_of_cols)


c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)


for i in range(1, number_of_probs + 1):
    prob_rect = pdf.get_rect_for_prob_num(i)
    c.drawString(prob_rect[0], prob_rect[1], str(i)+")")
    #c.rect(*prob_rect, 1, 0)
c.showPage()
c.save()
