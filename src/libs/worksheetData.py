from basicOpProblem import BasicOpProblem

class WorksheetData:
    header = {}
    problems = []
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
        
        # load default specs and replace with those the chosen
        self.specs = self.default_specs[problem_type]
        for spec in specs:
            self.specs[spec] = specs[spec]

    def create_header(self, subject, instructions):
        self.header['company_name'] = "Tiny-Robot"
        self.header['subject'] = subject
        self.header['instructions'] = instructions

    def create_problems(self, problem_type, min_value, max_value, problem_count):
        self.problems = []
        for i in range(1, problem_count + 1):
            problem = BasicOpProblem(problem_type)
            problem.randomize_nums(min_value, max_value)
            self.problems.append(problem)