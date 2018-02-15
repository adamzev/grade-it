from core.reportLabDoc import ReportLabDoc
from core.problem_sets import problem_number

def ScreenDisplay(problems, specs={}):
    for i, problem in enumerate(problems):
        print(problem_number(i+1))
        print()
        problem.screen_display()
        print()

def ReportLabDisplay(problems, worksheet_specs={}):
    c = ReportLabDoc(problems, worksheet_specs)
    return c.file_name