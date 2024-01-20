class Calculator:
    def __init__(self):
        "this is the init function"
        pass
    
    def add(self, a, b):
        "this is the add function"
        sum = a+b
        return sum

    def subtract(self, a, b):
        "this is the subtract function"
        sub = a-b
        return sub

    def divide(self, a, b):
        "this is the divide function"
        div = a/b
        return div

    def multiply(self, a, b):
        "this is the multiply function"
        mul = a*b
        return mul

    def __str__(self):
        "welcome to the calculator"