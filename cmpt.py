from myparser import validSign, validValue
import re

class computor:

    def __init__(self, arg):
        self.values = {0: [], 1: []}
        self.degree = 0
        self.discriminant = 0
        self.solution = []
        self.parse(arg)
        self.regroup(self.values)
        print(f"Reduced form: {self.format(self.reduce(self.values))}= 0")
        print(self.checkReducedForm(self.values[0]))
        if self.degree == 0:
            return
        elif self.degree == 1:
            print(self.getSolutionD1(self.values[0]))
        elif self.degree == 2:
            print(self.getDiscriminant())
        elif self.degree > 3:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return

    def parse(self, arg):
        tokens = re.findall(r'[+-]?\s*\d+(?:\.\d+)?\s*[*\/]\s*X(?:\^-?\d+)?|[=+-]', arg)
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

    def regroup(self, values):
        for i in range(len(values)):
            j = 0
            while j < len(values[i]):
                current = values[i].pop(j)
                k = 0
                while k < len(values[i]):
                    if current["expo"] == values[i][k]["expo"]:
                        temp = values[i].pop(k)
                        sign_current = -1 if current["sign"] == "-" else 1
                        sign_temp = -1 if temp["sign"] == "-" else 1
                        new_nb = sign_current * current["nb"] + sign_temp * temp["nb"]
                        current["nb"] = abs(new_nb)
                        current["sign"] = '-' if new_nb < 0 else '+'
                        continue
                    k += 1
                values[i].insert(j, current)
                j += 1

    def reduce(self, values):
        i = 0
        while i < len(values[1]):
            current = values[1].pop(i)
            j = 0
            while j < len(values[0]):
                if current["expo"] == values[0][j]["expo"]:
                    temp = values[0].pop(j)
                    sign_current = -1 if current["sign"] == "-" else 1
                    sign_temp = -1 if temp["sign"] == "-" else 1
                    new_nb = sign_current * current["nb"] + sign_temp * temp["nb"]
                    current["nb"] = abs(new_nb)
                    current["sign"] = '-' if new_nb < 0 else '+'
                    continue
                j += 1
            values[0].insert(i, current)
            i += 1
        return values[0]

    def format(self, values):
        equation = ""
        for value in values:
            if len(equation) == 0 and value["sign"] == '+':
                equation = str(value["nb"]) + " * X^" + str(value["expo"]) + " "
            elif len(equation) == 0 and value["sign"] == '-':
                equation = value["sign"] + str(value["nb"]) + " * X^" + str(value["expo"]) + " "
            else:
                equation += value["sign"] + " " + str(value["nb"]) + " * X^" + str(value["expo"]) + " "
        equation = equation.replace(".0 ", " ")
        return equation

    def checkReducedForm(self, values):
        before = False
        degree = 0
        for value in values:
            if value["expo"] > degree:
                degree = value["expo"]
            if value["nb"] != 0:
                before = True
        if degree > 0 and before is True:
            sentence = "Polynomial degree : " + str(degree)
            sentence = sentence.replace(".0", "")
        elif degree == 0 and before is True:
            sentence = "No solution."
        else:
            sentence = "Any real number is a solution."
        self.degree = degree
        return sentence

    def getSolutionD1(self, values):
        a = 0
        b = 0
        for value in values:
            if value["expo"] == 1:
                a = value["nb"] if value["sign"] == '+' else value["nb"] * -1
            elif value["expo"] == 0:
                b = value["nb"] * -1 if value["sign"] == '+' else value["nb"]
        print("yo")
        return

    def getDiscriminant(self):

        return ""
