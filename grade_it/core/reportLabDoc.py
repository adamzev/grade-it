from time import gmtime, strftime

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Table

from lib.reportLabStyle import getWorksheetStyleSheet
from core.problem_sets import problem_number

class ReportLabDoc():
    default_specs = { 
        "qr": True,
        "append_time": True,
        "header": True,
        "font": "Courier",
        "font_size": 16,
        "columns": 2,
        "paper_size": "letter",
        "folder": "sheets",
    }

    paper_size = {
        "letter" : letter
    }
    def __init__(self, problems, specs):

        self.specs = self.default_specs
        #override the defaults with anything that has been set
        for spec in specs:
            self.specs[spec] = specs[spec]
        
        self.name = self.specs['name']
        self.folder = self.specs['folder']
        self.problems = problems

        file_name = self.file_name()
        self.styleSheet = getWorksheetStyleSheet()
        doc = SimpleDocTemplate(file_name, pagesize=self.paper_size[self.specs['paper_size']])


        # container for the 'Flowable' objects

        self.worksheet = []

        if self.specs['header']:
            self.header()
        # check specs for font and style overrides
        # check specs for header and create one if asked
        # check specs for columns and create table
        # display each problem in a cell
        self.body()
        doc.build(self.worksheet)

    def file_name(self):
        if self.specs['append_time']:
            cur_time = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            file_name = "{}/{}_{}.pdf".format(self.folder, self.name, cur_time)
        else:
            file_name = "{}/{}.pdf".format(self.folder, self.name)
        return file_name
    
    def header(self):
        company_name = Paragraph("Tiny-Robot", self.styleSheet["Heading3"])
        name = Paragraph("Name:  _________________________", self.styleSheet["Heading3"])
        subject = Paragraph("Addition", self.styleSheet["Heading3"])
        date = Paragraph("Date:  _________________________", self.styleSheet["Heading3"])
        data = [[company_name, name], [subject, date]]

        if self.specs['qr']:
            qr_image = Image(self.specs['qr_file'])
            data = [[company_name, qr_image], [subject, ""], [name, ""], [date, ""]]
            t=Table(data, style=[
                            ("VALIGN", (0,3), (0,3), "TOP"),
                            ('ALIGN', (1,0), (1,3),'RIGHT'),
                            ('SPAN', (1,0), (1,3)),
                            
            ])
        else:
            data = [[company_name, name], [subject, date]]
            t=Table(data,colWidths='*', style=[
                            ('ALIGN',(0,0), (0,0),'LEFT'),
                            ('ALIGN',(1,0), (1,0),'RIGHT'),
                            ('ALIGN',(0,1), (0,1),'LEFT'),
                            ('ALIGN',(1,1), (1,1),'RIGHT'),              
            ])
        self.worksheet.append(t)

    def body(self):
        data = []
        row = []
        for i, problem in enumerate(self.problems):
            problem_num_text = problem_number(i+1)
            problem_table = problem.reportlab_display()
            #print(problem_table)
            inner_data = [[problem_num_text, problem_table]]
            # TODO find height of problem, find the minimum of pages
            # space the row Heights evenly over those pages 
            # or only worry about spacing evenly if it can fit to 1 page
            inner_table = Table(inner_data, colWidths='*', rowHeights=72, style=[
                ("VALIGN", (0,0), (1,0), "TOP")
            ])
            row.append(inner_table)
            if i % self.specs['columns']:
                data.append(row)
                row = []
        if row:
            data.append(row)
        t=Table(data, colWidths='*', style=[])
        self.worksheet.append(t)