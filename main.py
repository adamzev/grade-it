import random
import PyPDF2
from reportlab.pdfgen import canvas

pdf_w = PyPDF2.PdfFileWriter()

point = 1
inch = 72
h_font_size = 14 # heading font size
p_font_size = 32 # problem font size
p_char_spacing = p_font_size
seed_num = 12
random.seed(seed_num)
font='Helvetica'

def gen_mx_b():
    ans = list()

    for i in range(1,11):
        print(i, end=") ")
        m = random.randint(-8,15)
        x = random.randint(-8,15)
        b = random.randint(-8,15)
        y = m * x + b
        ans.append(x)
        print(str(m) + "x + " + str(b) + " = " + str(y))
    
    print("Answer Key")
    for i in range(1,11):
    
        print(i, end=") ")
        print(ans[i-1])

if __name__ == "__main__":
    filename = 'worksheet.pdf'
    make_pdf_file(filename)
    print ("Wrote", filename)