from libs.pdfCanvas import PdfCanvas
from libs.drawProblem import DrawProblem
from libs.basicOpProblem import BasicOpProblem
import qrcode
from qrcode.image.pure import PymagingImage
from reportlab.lib.utils import ImageReader

class WorksheetGen:
    default_specs = { 
        "add": {
            "min_val": 1,
            "max_val": 99,
            "qr": "on",
            "problem_count": 16,
            "font": "Courier",
            "font_size": 16,
            "columns": 2,
            "paper_size": "letter",
            "folder": "sheets",
        }
    }
    def __init__(self, name, problem_type, specs):
        ''' name: string, name of the worksheet used as file prefix
            specs: dict, contains the following optional keys:
                    min_val, 
                    max_val
                    qr (bool)
                    problem_count
                    font
                    font_size
                    columns
                    paper_size
                    folder
                '''
        if problem_type not in self.default_specs:
            raise ValueError("Unsupported problem type")
        self.specs = self.default_specs[problem_type]
        for spec in specs:
            self.specs[spec] = specs[spec]
        canvas_specs = {}
        for attr in ['folder']: # more attr will be added later
            canvas_specs[attr] = self.specs[attr]
        self.pdf = PdfCanvas(name, **canvas_specs)
        self.c = self.pdf.c
        print(self.specs['problem_count'], self.specs['columns'])
        self.pdf.set_prob_layout(self.specs['problem_count'], self.specs['columns'])
        self.c.setStrokeColorRGB(0,0,0)
        self.c.setFillColorRGB(0,0,0)
        self.c.setFont(self.specs['font'], self.specs['font_size'])
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
        
