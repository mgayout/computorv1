from parser import validChar,validSign

class computor:

    def __init__(self):
        self.arg = ""
        self.reduced_form = ""
        self.polynomial_degree = 0
        self.discriminant = 0
        self.solution = []

    def run(self, arg):
        self.parse(arg)
        self.printInfo()
        return
    
    def parse(self, arg):
        if validChar(arg):
            raise ValueError("Bad format")
        self.arg = arg.split(" ")
        if validSign(self.arg):
            raise ValueError("Bad format")

        
#Character valid
#Format : chiffre + signe
#Format : 1 seul '='
    
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
