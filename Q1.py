from tkinter.simpledialog import askfloat


class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    ## ask user for two input
    def askForInput(self):
        print('\nEnter the first number: ')
        self.num1 = int(input())
        print('\nEnter the second number: ')
        self.num2 = int(input())

    ## Adding 2 numbers
    def adder(self):
        return(self.num1 + self.num2)

    ## Subtracting 2 numbers
    def subtractor(self):
        return self.num1 - self.num2

    ## multiply 2 numbers
    def multiplier(self):
        return (self.num1 * self.num2)

    ## dividie 2 numbers
    def divider(self):
        return (self.num1 / self.num2)

    ## clear num1 and num2
    def clear(self):
        self.num1 = 0
        self.num2 = 0
        return ("\nInput has been clear! ")

cal = Calculator()
cal.askForInput()
print("\nAdding 2 inputs: " + str(cal.adder()))
print("Subtracting 2 inputs: " + str(cal.subtractor()))
print("Multiplying 2 inputs: " + str(cal.multiplier()))
print("Dividing 2 inputs: " + str(cal.divider()))
print(cal.clear())