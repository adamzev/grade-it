from core.basicOpProblem import BasicOpProblem
from core.textProblem import TextProblem

from core.displayMethod import ScreenDisplay, ReportLabDisplay 

from core.problem_sets import create_problems, get_ans_text
from lib.qr import get_qr_code

SCREEN = "screen"
PDF = "pdf"
# TODO rename BasicOp to SimpleArthimatic

def generate_worksheet(worksheet_specs, display_method="pdf"):
    # store the data
    problem_types = [BasicOpProblem, TextProblem]
    problems = []
    for problem_group in worksheet_specs['problem_groups']:
        
        for problem_type in problem_types:
            if problem_group['group_name'] in problem_type.name:
                p_type = problem_type
                break
        else:
            raise ValueError("Unhandled problem type")

        problems.extend(create_problems(problem_group['count'], p_type, problem_group['specs']))

    if worksheet_specs['qr']:
        ans_text = get_ans_text(problems)
        # TODO: switch magic number of 320 to be a calculation regarding how big the qr code will be
        if len(ans_text) > 320: 
            worksheet_specs['qr_file'] = get_qr_code(ans_text, "image", size="small")
        else:
            worksheet_specs['qr_file'] = get_qr_code(ans_text, "image")

    if display_method == "screen":
        ScreenDisplay(problems)
    
    if display_method == "report_lab_pdf" or display_method == "pdf":
        ReportLabDisplay(problems, worksheet_specs)

if __name__ == "__main__":
    worksheet_specs = {
        "name": "first_test",
        "qr": True, 
        "problem_groups": [
            {
                "count": 40,
                "group_name": "basicOp",
                "specs": {
                    "type": "add",
                    "randomize": True,
                    "min_value": 1,
                    "max_value": 100

                }
            }
        ]
    }

    
    generate_worksheet(worksheet_specs, display_method=PDF)
