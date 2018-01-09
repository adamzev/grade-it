number_of_probs = 24
number_of_cols = 2

pdf = PdfCanvas("add_worksheet")
c = pdf.c
pdf.set_prob_layout(number_of_probs, number_of_cols)

c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)

for i in range(1, number_of_probs + 1):
    prob_rect = pdf.get_rect_for_prob_num(i)
    c.drawString(prob_rect[0], prob_rect[1], str(i)+")")
    
c.showPage()
c.save()
