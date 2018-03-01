def problem_number(num, seperator=") "):
    return str(num)  + seperator

def create_problems(problem_count, problem_type, problem_specs):
    problem_set = []
    for _ in range(problem_count):
        problem_set.append(problem_type(problem_specs))
    return problem_set

def get_ans(problems, format):
    ans_list = []
    ans_txt = ""
    for i, problem in enumerate(problems):
        ans_list.append(problem.ans)
        ans_txt += problem_number(i+1) + str(problem.ans) + '\n'
    if format == "text":
        return ans_txt
    if format == "list":
        return ans_list