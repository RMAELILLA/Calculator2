# redo calculator with oop
from user_display import UserDisplay
from calculator_add import CalculatorAdd

calculator_operator2 = UserDisplay()
calculator_addition = CalculatorAdd()

# evaluate the chosen math operations
math_operator = calculator_operator2.math_operator()

# if input is "Addition"
if math_operator.lower == "addition":
    first_number = calculator_operator2.user_number
    second_number = calculator_operator2.user_number
# if input is "Subtraction"

# if input is "Multiplication"

# if input is "Division"

# ----------------------------------------------
# ask user if wants to input again
    # if yes
    # if no
        # display appreciation