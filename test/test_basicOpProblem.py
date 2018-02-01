from src.libs.basicOpProblem import BasicOpProblem

def test_mult_ans():
    mult = BasicOpProblem("mult", 12, 3)
    assert mult.ans == 36

def test_add_ans():
    add = BasicOpProblem("add", 12, 3)
    assert add.ans == 15
