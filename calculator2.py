# redo calculator with oop
from user_display import UserDisplay
from calculator_operator import CalculatorOperator

class Calculator2:
    def __init__(self):
        self.user_display = UserDisplay()
        self.calculator_operator = CalculatorOperator()
    def run(self):
        math_operator = self.user_display.math_operator()
        math_operator = math_operator.lower()
        first_number = self.user_display.user_number()
        second_number = self.user_display.user_number()

        if math_operator == "addition":
            addition = self.calculator_operator.cal_add(first_number, second_number)
            self.user_display.display_addition(addition)
# if input is "Subtraction"

# if input is "Multiplication"

# if input is "Division"

# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
        # display appreciation

math_calculator = Calculator2()
math_calculator.run()

# else:
#    print("error occur")