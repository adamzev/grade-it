import random
class BasicOpProblem:
    def __init__(self, operation=None, num1=None, num2=None):
        if operation not in ["add", "sub", "mult", "div"]:
            raise ValueError("Unsupported Operation Type: Must be \"add\", \"sub\", \"mult\", or \"div\"")

        self.num1 = num1
        self.prob_type = "BasicOp"
        self.num2 = num2
        self.operation = operation
        self.op_symbol = self.set_symbol()

    @property
    def ans(self):
        if not self.num1 or not self.num2:
            raise ValueError("Answer not set yet. Num1 and Num2 are required.")
        if self.operation == "add":
            return self.num1 + self.num2
        elif self.operation == "sub":
            return self.num1 - self.num2
        elif self.operation == "mult":
            return self.num1 * self.num2
        elif self.operation == "div":
            return self.num1 // self.num2


    def set_symbol(self):
        if self.operation == "add":
            return '+'
        elif self.operation == "sub":
            return u"\u2796" 
            # Heavy Minus http://www.fileformat.info/info/unicode/char/2796/index.htm
            #return 	u"\u2212" # Minus http://www.fileformat.info/info/unicode/char/2212/index.htm
        elif self.operation == "mult":
            return '\xc3\x97'
        elif self.operation == "div":
            return '\xc3\xb7'

    def set_nums(self, min_=1, max_=10):
        self.num1 = random.randint(min_, max_)
        self.num2 = random.randint(min_, max_)


    def set_num1(self, min_=1, max_=10):
        self.num1 = random.randint(min_, max_)

    def set_num2(self, min_=1, max_=10):
        self.num2 = random.randint(min_, max_)
