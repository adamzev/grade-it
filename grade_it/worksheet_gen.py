import sys
import random

from core.basicOpProblem import BasicOpProblem
from core.textProblem import TextProblem

from core.displayMethod import ScreenDisplay, ReportLabDisplay 

from core.problem_sets import create_problems, get_ans
from lib.qr import get_qr_code


SCREEN = "screen"
PDF = "pdf"
# TODO rename BasicOp to SimpleArthimatic

def generate_worksheet(worksheet_specs, display_method="pdf"):
    # store the data
    problem_types = [BasicOpProblem, TextProblem]

    # TODO instead of storing the seed create a mongo database that 
    # stores an index to the answer key

    if worksheet_specs.get('random_seed'):
        random.seed(int(worksheet_specs['random_seed'], base=16))
    else:
        seed = random.randrange(sys.maxsize)
        random.seed(seed)
        worksheet_specs['random_seed'] = hex(seed)

    problems = []
    for problem_group in worksheet_specs['problem_groups']:
        
        for problem_type in problem_types:
            if problem_group['group_name'] in problem_type.name:
                p_type = problem_type
                break
        else:
            raise ValueError("Unhandled problem type")

        problems.extend(create_problems(problem_group['count'], p_type, problem_group['specs']))
    ans_text = get_ans(problems, "text")
    ans_list = get_ans(problems, "list")
    print(ans_list)

    if worksheet_specs['qr']:
        # TODO: switch magic number of 320 to be a calculation regarding how big the qr code will be
        if worksheet_specs['qr_type'] == "answer_key":
            qr_text = ans_text
        elif worksheet_specs['qr_type'] == "form_code":
            qr_text = worksheet_specs['random_seed']
        if len(ans_text) > 320: 
            worksheet_specs['qr_file'] = get_qr_code(qr_text, "image", size="small")
        else:
            worksheet_specs['qr_file'] = get_qr_code(qr_text, "image")

    if display_method == "screen":
        ScreenDisplay(problems)
    
    if display_method == "report_lab_pdf" or display_method == "pdf":
        ReportLabDisplay(problems, worksheet_specs)

if __name__ == "__main__":
    worksheet_specs = {
        "name": "add",
        "qr": True, 
        "qr_type": "form_code", # or "answer_key"
        "random_seed": "BCBA8F9752",
        "problem_groups": [
            {
                "count": 14,
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
