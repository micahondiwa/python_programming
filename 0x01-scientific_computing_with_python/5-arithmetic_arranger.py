def arithmetic_arranger(problems, show_answers=False):
    # Checking if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Variables for storing each line of the arranged problem
    first_operand = ""
    operator_and_second_operand = ""
    underline = ""
    results = ""

    # Remove white space
    for problem in problems:
        problem = problem.replace(" ", "")

        # Check if operator is supported
        if "+" in problem:
            problem = problem.split("+")
            operator = "+"
        elif "-" in problem:
            problem = problem.split("-")
            operator = "-"
        else:
            return "Error: Operator must be '+' or '-'."
        
        # Check if operands are digits only
        if not (problem[0].isdigit() and problem[1].isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Check if operands have more than 4 digits
        if len(problem[0]) > 4 or len(problem[1]) > 4:
            return "Error: Numbers cannot be more than four digits"
        
        # Width for formatting
        width = max([len(problem[0]), problem[1]]) + 2

        # Calculating answers if show_answers = True
        if show_answers:


        first_operand += problem[0].rjust(width) + "    "
        operator_and_second_operand += operator + problem[1].rjust(width - 1) + "    "
        underline += "-" * (width) + "    "
