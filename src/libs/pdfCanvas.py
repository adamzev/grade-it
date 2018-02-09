''' draw a heading of size heading_size, split the rest of the page into
    prob_count (rounded up to nearest even number) evenly sized blocks leaving 1 inch margins
 '''


import random
import PyPDF2
from reportlab.pdfgen import canvas
from time import gmtime, strftime

class PdfCanvas():
    def __init__(self, file_prefix, append_time=True, page_size_in=(8.5, 11), inch=72, margin_in=1, folder="sheets"):
        if append_time:
            cur_time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            file_name = "{}/{}_{}.pdf".format(folder, file_prefix, cur_time)
            
        self.file_name = file_name
        self.canvas = canvas.Canvas(file_name, pagesize=(page_size_in[0] * inch, page_size_in[1] * inch))
        self.c = self.canvas
        self.width_in = page_size_in[0]
        self.height_in = page_size_in[1]
        self.inch  = inch # size of an inch in pixels
        self.margin_in = margin_in
        self.top_of_page = inch * page_size_in[1]
        self.header_h_in = 1.5
        self.set_useable_area()
        self.header_w_px = self.useable_w_px
        self.content_w_px = self.useable_w_px
        self.content_h_px = self.useable_h_px - self.header_h_px

        self.top_of_probs = self.top_of_page - self.margin_px - self.header_h_px

    @property
    def width_px(self):
        return self.convert_to_px(self.width_in)


    @property
    def margin_px(self):
        return self.convert_to_px(self.margin_in)

    @property
    def height_px(self):
        return self.convert_to_px(self.height_in)

    @property
    def header_h_px(self):
        return self.convert_to_px(self.header_h_in)


    def convert_to_px(self, x):
        return int(x * self.inch)
        
    def set_useable_area(self):
        self.useable_w_px = self.width_px - 2 * self.margin_px
        self.useable_h_px = self.height_px - 2 * self.margin_px


    def get_header_rect(self):
        return self.margin_px, self.top_of_page - self.margin_px, self.header_w_px, -1 * self.header_h_px

    def get_useable_rect(self):
        return self.margin_px, self.margin_px, self.useable_w_px, self.useable_h_px

    def set_prob_layout(self, number_of_probs, number_of_cols):
        if number_of_probs % number_of_cols:
            number_of_probs = number_of_probs + number_of_cols - number_of_probs % number_of_cols
        self.number_of_probs = number_of_probs
        self.number_of_cols = number_of_cols
        self.number_of_rows = number_of_probs // number_of_cols
        self.prob_w = self.content_w_px // number_of_cols
        self.prob_h = self.content_h_px // self.number_of_rows
        self.top_of_probs = self.top_of_page - self.margin_px - self.header_h_px

    def get_rect_for_prob_num(self, prob_num):
        prob_num -= 1
        j = prob_num % self.number_of_cols
        i = prob_num // self.number_of_cols
        x = self.margin_px + self.prob_w * j
        y = self.top_of_probs - self.prob_h * i
        w = self.prob_w
        h = -1 * self.prob_h
        return x, y, w, h