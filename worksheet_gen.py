from libs.pdfCanvas import PdfCanvas
from libs.drawProblem import DrawProblem
from libs.basicOpProblem import BasicOpProblem
import qrcode
from qrcode.image.pure import PymagingImage
from reportlab.lib.utils import ImageReader

class WorksheetGen:
    def __init__(self, name, specs):
        ''' name: string, name of the worksheet used as file prefix
            specs: dict, contains the follow keys:
                required:
                    problem_type
                optional:
                    problem_count
                    font
                    font_size
                    columns
                    paper_size
                '''
        self.number_of_probs = specs.get('problem_count', 10)
        self.number_of_cols = specs.get('columns', 2)

        self.pdf = PdfCanvas(name)
        self.c = self.pdf.c
        self.pdf.set_prob_layout(self.number_of_probs, self.number_of_cols)
        font = specs.get('font', 'Courier')
        self.c.setStrokeColorRGB(0,0,0)
        self.c.setFillColorRGB(0,0,0)
        self.c.setFont(font, specs.get('font_size', 16))
        self.create_header()

    def create_header(self):
        header_rect = self.pdf.get_header_rect()
        company_name = "Tiny-Robot"
        subject = "Addition"
        instructions = ""
        name = "Name: ______________"
        date = "Date: ______________"
        self.c.drawString(header_rect[0], header_rect[1], company_name)
        self.c.drawString(header_rect[0], header_rect[1] - 25, subject)
        self.c.drawString(header_rect[0] + 140, header_rect[1], name)
        self.c.drawString(header_rect[0] + 140, header_rect[1] - 25, date)


    def create_sheet(self):
        ans_txt = ""
        for i in range(1, self.number_of_probs + 1):
            prob_rect = self.pdf.get_rect_for_prob_num(i)
            self.c.drawString(prob_rect[0], prob_rect[1], str(i)+")")
            prob = BasicOpProblem("add")
            prob.set_nums(1, 99)
            DrawProblem.drawBasicOpProblem(prob_rect, prob, self.pdf, 'vert')
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
        header_rect = self.pdf.get_header_rect()
        self.c.drawImage(rlImg, header_rect[0] + 375, header_rect[1] - 90)

        self.c.showPage()
        return self.c.save()
