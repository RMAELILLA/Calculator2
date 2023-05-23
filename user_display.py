# ask user to choose math operations between "Addition", "Subtraction", "Multiplication", or "Division"
class UserDisplay:
    def math_operator(self):
        user_operator = input("Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication' or 'Division': ")
        return user_operator
    def user_number(self):
        first_number = float(input("Please enter number: "))
        return first_number
    def display_addition(self, addition):
        print("The sum is: " + str(addition))