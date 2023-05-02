import operator as op

class TooManyProblems(Exception):
    """Raised when the problem list is too long"""
    
    def __init__(self, *args: object) -> None:
        self.message = "Error: Too many problems."
        super().__init__(self.message)

class BadOperator(Exception):
    """Raised when the anything orther + or - is used"""
    
    def __init__(self, *args: object) -> None:
        self.message = "Error: Operator must be '+' or '-'."
        super().__init__(self.message)

class NonNumericOperand(Exception):
    """Raised when the anything orther + or - is used"""
    
    def __init__(self, *args: object) -> None:
        self.message = "Error: Numbers must only contain digits."
        super().__init__(self.message)


class OperandTooLong(Exception):
    """Raised when the anything orther + or - is used"""
    
    def __init__(self, *args: object) -> None:
        self.message = "Error: Numbers cannot be more than four digits."
        super().__init__(self.message)


def check_operand_length(number):
    if len(number) > 4:
        return False
    return len(number)

def check_operand_composition(number):  
    if not number.isnumeric():
        return False
    return True
    

def check_operator(operator):
    if operator not in ('+', "-"):
        return False
    return True
    
ops = {
    "+" : op.add,
    "-" : op.sub,
}

def calc_spaces(len_of_number, len_of_calc):
    return (len_of_calc - len_of_number)


def create_equal_line(len_calc, line_list):
    line_list.extend(len_calc*['-'])
    line_list.extend(4*[' '])


def text_line(num_spaces, num, row_list, operator=None):
    digits = [*num]
    if operator:
        row_list.append(operator)
    row_list.extend(num_spaces*[' '])
    row_list.extend(digits)
    row_list.extend(4*[' '])

    return row_list

def arithmetic_arranger(problems, calculate=False):
    top_numbers=[]
    bottom_numbers=[]
    equals_line=[]
    solution_line=[]
    arranged_problems = ""
    if len(problems) > 5:
        return "Error: Too many problems."
        
    
    for problem in problems:
        problem_as_list = problem.split()
        
        top_num, operator, bot_num = problem_as_list
        
        if not check_operand_length(top_num):
            return "Error: Numbers cannot be more than four digits."
        else:
            len_top = check_operand_length(top_num) 


        if not check_operand_length(bot_num):
            return "Error: Numbers cannot be more than four digits."
        else:
            len_bot = check_operand_length(bot_num)  

        if not check_operand_composition(top_num):
            return "Error: Numbers must only contain digits."

        if not check_operand_composition(bot_num):
            return "Error: Numbers must only contain digits."
        

        if not check_operator(operator):
            return "Error: Operator must be '+' or '-'."



        len_calc = max(len_top, len_bot) + 2
        top_spaces = calc_spaces(len_top, len_calc)
        top_row = text_line(top_spaces,top_num,top_numbers)

        bottom_spaces = calc_spaces(len_bot, len_calc) - 1
        mid_row = text_line(bottom_spaces,bot_num, bottom_numbers, operator)

        create_equal_line(len_calc, equals_line)

        if calculate:
            solution = str(ops.get(operator)(int(top_num), int(bot_num)))
            solution_spaces = calc_spaces(len(str(solution)), len_calc)
            solution_row = text_line(solution_spaces, solution, solution_line)
        else:
            solution = None 
            solution_row = solution_line


    if solution:
        arranged_problems = ''.join(top_row[:-4]) + '\n' + ''.join(mid_row[:-4]) + '\n' + ''.join(equals_line[:-4]) + '\n' + ''.join(solution_row[:-4])
    
    else:
        arranged_problems = ''.join(top_row[:-4]) + '\n' + ''.join(mid_row[:-4]) + '\n' + ''.join(equals_line[:-4])

    return arranged_problems