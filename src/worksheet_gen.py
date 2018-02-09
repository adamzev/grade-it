from libs.pdfCanvas import PdfCanvas
from libs.drawProblem import DrawProblem
from libs.basicOpProblem import BasicOpProblem
import qrcode
from qrcode.image.pure import PymagingImage
from reportlab.lib.utils import ImageReader
from libs.worksheetData import WorksheetData

def generate_worksheet(name, problem_type, specs):
    # store the data
    data = WorksheetData(name, problem_type, specs)

    # create the canvas/pdf
    self.pdf = PdfCanvas(data)

    # display the data


        print(self.specs['problem_count'], self.specs['columns'])
        self.pdf.set_prob_layout(self.specs['problem_count'], self.specs['columns'])
        self.c.setStrokeColorRGB(0,0,0)
        self.c.setFillColorRGB(0,0,0)
        self.c.setFont(self.specs['font'], self.specs['font_size'])


        self.c.drawString(header_rect[0], header_rect[1], company_name)
        self.c.drawString(header_rect[0], header_rect[1] - 25, subject)
        self.c.drawString(header_rect[0] + 140, header_rect[1], name)
        self.c.drawString(header_rect[0] + 140, header_rect[1] - 25, date)


    def create_sheet(self):
        ans_txt = ""
        for i in range(1, self.specs['problem_count'] + 1):
            prob_rect = self.pdf.get_rect_for_prob_num(i)
            self.c.drawString(prob_rect[0], prob_rect[1], str(i)+")")
            prob = BasicOpProblem("add")
            prob.set_nums(self.specs['min_val'], self.specs['max_val'])
            DrawProblem.drawBasicOpProblem(prob_rect, prob, self.pdf, 'vert')
            ans_txt+= str(i)+") " + str(prob.ans) + '\n'
        if self.specs['qr']:
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
        self.c.save()
        return self.pdf.file_name
        
