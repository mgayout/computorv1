from myparser import validSign, validValue
import re

class computor:

    def __init__(self, arg):
        self.values = {0: [], 1: []}
        self.reduced_form = ""
        self.polynomial_degree = 0
        self.discriminant = 0
        self.solution = []
        self.parse(arg)
        print(self.values)
        self.reduce()
        print(self.values)

    def parse(self, arg):
        tokens = re.findall(r'[+-]?\s*\d+(?:\.\d+)?\s*[*\/]\s*X(?:\^-?\d+)?|[=+-]', arg)
        print(tokens)
        sign = False
        equal = 0

        for token in tokens:
            token = token.strip()
            tok = token.split(" ")
            for t in tok:
                if sign is True and validSign(t) is True:
                    if t == "=":
                        equal += 1
                elif sign is False and validValue(t) is True:
                    pass
                else:
                    raise ValueError("Bad format")
                sign = not sign
            self.addValue(tok, equal)
        if equal != 1 or sign is False:
            raise ValueError("Bad format")


    def addValue(self, token, equal):
        if equal == 1 and len(token) == 1 and token[0] == "=":
            return
        elif len(token) == 4:
            sign = token[0]
            nb = token[1]
            expo = token[3].split("^")[1]
        else:
            sign = "+"
            nb = token[0]
            expo = token[2].split("^")[1]
        self.values[equal].append({"sign": sign, "nb": float(nb), "expo": float(expo)})

    def reduce(self):
        print("---------------------------------------")
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                print(f"self.values[i] = {self.values[i]}")
                print(j, len(self.values[i]))
                current = self.values[i].pop(j)
                for k in range(len(self.values[i])):
                    print(current, self.values[i][k])
                    if current["expo"] == self.values[i][k]["expo"]:
                        print("yo")
                        temp = self.values[i].pop(k)
                        sign_current = -1 if current["sign"] == "-" else 1
                        sign_temp = -1 if temp["sign"] == "-" else 1
                        new_nb = sign_current * current["nb"] + sign_temp * temp["nb"]
                        current["nb"] = abs(new_nb)
                        current["sign"] = '-' if new_nb < 0 else '+'
                self.values[i].insert(j, current)

    
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
