from myparser import validSign, validValue

class computor:

    def __init__(self):
        self.values = []
        self.sign = []
        self.reduced_form = ""
        self.polynomial_degree = 0
        self.discriminant = 0
        self.solution = []

    def run(self, arg):
        self.parse(arg)
        self.printInfo()
        return
    
    def parse(self, arg):
        splited_arg = arg.split(" ")
        sign = False
        equal = 0
        for token in splited_arg:
            if sign is True and validSign(token, equal) is True:
                if token == "=":
                    equal += 1
                self.sign.append(token)
            elif sign is False and validValue(token) is True:
                self.addValue(token)
            else:
                raise ValueError("Bad format")
            sign = not sign
        if equal != 1 or sign is False:
            raise ValueError("Bad format")

    def addValue(self, token):        
        return

    
    def printInfo(self):
        print(f"Reduced form: {self.reduced_form}")
        print(f"Polynomial degree: {self.polynomial_degree}")
        if self.polynomial_degree > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
        if self.discriminant == 0:
            print(f"The solution is:\n{self.solution}")
        elif self.discriminant > 0:
            print(f"Discriminant is strictly positive, the two solutions are:\n{self.solution}")
        else:
            print(f"Discriminant is strictly negative, the two complex solutions are:\n{self.solution}")
