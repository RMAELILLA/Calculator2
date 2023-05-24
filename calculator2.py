# redo calculator with oop
from user_display import UserDisplay
from calculator_operator import CalculatorOperator

class Calculator:
    def __init__(self):
        self.user_display = UserDisplay()
        self.calculator_operator = CalculatorOperator()

math_operator = user_operator.math_operator()
math_operator = math_operator.lower()
first_number = user_operator.user_number()
second_number = user_operator.user_number()

if math_operator == "addition":
    addition = calculator_operator.cal_add(first_number, second_number)
    user_operator.display_addition(addition)
# if input is "Subtraction"

# if input is "Multiplication"

# if input is "Division"

# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
        # display appreciation
else:
    print("error occur")