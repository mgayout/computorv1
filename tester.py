from myparser import validSign, validValue

def parse(arg):
    #print(f"{arg} = ", end="")
    splited_arg = arg.split(" ")
    sign = False
    equal = 0
    for token in splited_arg:
        #print(token, sign)
        if sign is True and validSign(token, equal) is True:
            if token == "=":
                equal += 1
            pass
        elif sign is False and validValue(token) is True:
            pass
        else:
            return False
        sign = not sign
    if equal != 1 or sign is False:
        return False
    return True

def main():
    print(parse("5 * X^0 + 4 * X^1 = 4 * X^0")) # Correct
    print(parse("5 * X^0 + 4 * X = 4 * X^0")) # Correct X or X^1
    print(parse("* X^0 + 4 * X^1 = 4 * X^0")) # Incorrect start with sign (before =)
    print(parse("5 * X^0 + 4 * X^1 + = 4 * X^0")) # Incorrect end with sign (before =)
    print(parse("5 * X^0 + 4 * X^1 = + 4 * X^0")) # Incorrect start with sign (after =)
    print(parse("5 * X^0 + 4 * X^1 = 4 * X^0 +")) # Incorrect end with sign (after =)
    print(parse("5 +* X^0 + 4 * X^1 = 4 * X^0")) # Incorrect double sign
    print(parse("5 * X^0 + 4 * X^1 == 4 * X^0")) # Incorrect double egal
    print(parse("5 * X^0 = + 4 * X^1 = 4 * X^0")) # Incorrect double equation
    print(parse("5a * X^0 + 4 * X^1 = 4 * X^0")) # Incorrect alphabetic character
    print(parse("a * X^0 + 4 * X^1 = 4 * X^0")) # Incorrect alphabetic character 2
    print(parse("= 5 * X^0 + 4 * X^1")) # Incorrect start with =
    print(parse("5 * X^0 + 4 * X^1 =")) # Incorrect end with =
    print(parse("5* X^0 + 4 * X^1 = 4 * X^0")) # Incorrect missing space
    print(parse("5 * X^0 + 4 * X^ = 4 * X^0")) # Incorrect missing expo after X^

if __name__ == "__main__":
    main()
