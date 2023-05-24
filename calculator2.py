# redo calculator with oop
from user_display import UserDisplay
from calculator_operator import CalculatorOperator

class Calculator2:
    def __init__(self):
        self.user_display = UserDisplay()
        self.calculator_operator = CalculatorOperator()
    def run(self):
        math_operator = self.user_display.math_operator().lower()

        if math_operator in ["addition", "subtraction", "multiplication", "division"]:
            first_number = self.user_display.user_number()
            second_number = self.user_display.user_number()

            if math_operator == "addition":
                addition = self.calculator_operator.cal_add(first_number, second_number)
                self.user_display.display_addition(addition)
            elif math_operator == "subtraction":
                subtraction = self.calculator_operator.cal_subtract(first_number, second_number)
                self.user_display.display_subtraction(subtraction)
            elif math_operator == "multiplication":
                multiplication = self.calculator_operator.cal_multiply(first_number, second_number)
                self.user_display.display_multiplication(multiplication)
            elif math_operator == "division":
                division = self.calculator_operator.cal_divide(first_number, second_number)
                self.user_display.display_division(division)
            
        else:
            print("I don't understant your input, please choose one only in the four math operators.")

        self.math_operator2()

    def math_operator2(self):
        math_calculator2 = self.user_display.math_operator2()

        if math_calculator2.lower() == "y":
            self.run()
        elif math_calculator2.lower() == "n":
            print("Thank you for using this program. Have a Good day!")
        else:
            print("Please choose 'y' only if yes or 'n' only if no")

math_calculator = Calculator2()
math_calculator.run()