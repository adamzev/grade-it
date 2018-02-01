''' draw a heading of size heading_size, split the rest of the page into
    prob_count (rounded up to nearest even number) evenly sized blocks leaving 1 inch margins
 '''
import random
import PyPDF2
from reportlab.pdfgen import canvas
from time import gmtime, strftime

def get_rand_color():
    return random.random(), random.random(), random.random()

inch = 72
width_in = 8.5
height_in = 11
margin_in = 1 # one inch margin on all sides

top_of_page = inch * height_in
width_px = int(width_in * inch)
height_px = int(height_in * inch)

print(width_px, height_px)

useable_w = width_px - 2 * margin_in * inch
useable_h = height_px - 2 * margin_in * inch

header_h_in = 1.5
header_h = header_h_in * inch
header_w = useable_w

content_w = useable_w
content_h = int(useable_h - header_h_in * inch)

margin_h_px = margin_in * inch
margin_w_px = margin_in * inch

print(useable_w, useable_h)

print(content_w, content_h)

cur_time = strftime("%Y-%m-%d_%H-%M", gmtime())
file_name = f"page_blocks_{cur_time}.pdf"
c = canvas.Canvas(file_name, pagesize=(8.5 * inch, 11 * inch))
c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)
c.rect(0, 0, width_px, height_px, 1, 1)
c.setStrokeColorRGB(0,100,0)
c.setFillColorRGB(0,100,0)
c.rect(margin_w_px, margin_h_px, useable_w, useable_h, 1, 1)
#c.setFont(font, p_font_size * point)
c.setStrokeColorRGB(100,0,0)
c.setFillColorRGB(100,0,0)
c.rect(margin_w_px, top_of_page - margin_h_px, header_w, -header_h, 1, 1)


top_of_probs = top_of_page - margin_h_px - header_h
number_of_probs = random.randint(2, 30)
print(number_of_probs)
number_of_cols = random.randint(1,5)
if number_of_probs % number_of_cols:
    number_of_probs = number_of_probs + number_of_cols - number_of_probs % number_of_cols
print(number_of_probs)
number_of_rows = number_of_probs // number_of_cols

print(number_of_rows, number_of_cols, "rows and cols")
prob_w = content_w / number_of_cols
prob_h = content_h / number_of_rows



for i in range(number_of_rows):
    for j in range(number_of_cols):
        c.setStrokeColorRGB(*get_rand_color())
        c.setFillColorRGB(*get_rand_color())
        c.rect(
            margin_h_px + prob_w * j,
            top_of_probs- prob_h * i,
            prob_w,
            -prob_h,
            1,
            1
        )


c.showPage()
c.save()
