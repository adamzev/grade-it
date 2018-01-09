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

class DrawProblem:
    def __init__(self):
        pass

    @staticmethod
    def drawBasicOpProblem(problem, cnv):
        if problem.orientation == 'vert':
            DrawProblem.drawVertBasicOpProblem(problem, cnv)
        elif problem.orientation == 'horiz':
            DrawProblem.drawHorizBasicOpProblem(problem, cnv)

    @staticmethod
    def drawVertBasicOpProblem(problem, cnv):
        top_of_page = 10 * inch
        line_size = p_char_spacing * point
        cnv.drawString( 1.3 * inch, top_of_page, str(problem.num1) )
        
        cnv.drawString( 1.3 * inch, top_of_page - line_size * 1, str(problem.num2) )
        cnv.drawString( 1 * inch, top_of_page - line_size * 1, problem.op_symbol )

    @staticmethod
    def drawHorizBasicOpProblem(problem, cnv):
        pass



class BasicOpProblem:
    def __init__(self, num1=None, num2=None, operation=None, orientation='vert'):
        if operation not in ["add", "sub", "mult", "div"]:
            raise ValueError("Unsupported Operation Type: Must be \"add\", \"sub\", \"mult\", or \"div\"")
        if orientation not in ['vert', 'horiz']:
            raise ValueError("Unsupported Orientation Type: Must be \"vert\", or \"horiz\"")
        self.num1 = num1
        self.prob_type = "BasicOp"
        self.num2 = num2
        self.operation = operation
        self.orientation = orientation
        self.op_symbol = self.set_symbol()
        self.ans = self.set_ans()

    def set_ans(self):
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "sub":
            return self.num1 - self.num2
        elif self.operation == "mult":
            return self.num1 * self.num2
        elif self.operation == "div":
            return self.num1 // self.num2


    def set_symbol(self):
        if self.operation == "add":
            return '+'
        elif self.operation == "sub":
            return u"\u2796" # Heavy Minus http://www.fileformat.info/info/unicode/char/2796/index.htm
            #return 	u"\u2212" # Minus http://www.fileformat.info/info/unicode/char/2212/index.htm
        elif self.operation == "mult":
            return '\xc3\x97'
        elif self.operation == "div":
            return '\xc3\xb7'

    def set_nums(self, min_ = 1, max_ = 10):
        self.num1 = random.randint(min_, max_)
        self.num2 = random.randint(min_, max_)

    def set_num1(self, min_ = 1, max_ = 10):
        self.num1 = random.randint(min_, max_)

    def set_num2(self, min_ = 1, max_ = 10):
        self.num2 = random.randint(min_, max_)


def make_pdf_file(output_filename, np = 1):
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont(font, p_font_size * point)
    prob = BasicOpProblem(12, 15, "add", "vert")
    DrawProblem.drawBasicOpProblem(prob, c)
    c.showPage()
    c.save()

def gen_addition():
    ans = list()
    prob_text = ""
    prob_text += "Seed {}\n".format(seed_num)
    for i in range(1,11):
        a = random.randint(1,100)
        b = random.randint(1,100)
        ans.append(a + b)
        
        prob_text += str(i) + ") " + str(a) + " + " + str(b)+'\n'
    
    ans_text = ""
    ans_text += "Answer Key\n"
    
    for i in range(1,11):
        ans_text += "{}) {}\n".format(i ,ans[i-1])
    return prob_text
  
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