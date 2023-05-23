# redo calculator with oop
from user_display import UserDisplay
from calculator_add import CalculatorAdd

calculator_operator2 = UserDisplay()
calculator_addition = CalculatorAdd()

math_operator = calculator_operator2.math_operator()
first_number = calculator_operator2.user_number()
second_number = calculator_operator2.user_number()

# if input is "Addition"
if math_operator == "addition":
    addition = calculator_addition.cal_add(first_number, second_number)
    calculator_operator2.display_addition(addition)
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