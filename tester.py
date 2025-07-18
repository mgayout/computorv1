from parser import validChar,validSign

def parse(arg):
    print(arg)
    if validChar(arg):
        return True
    new_arg = arg.split(" ")
    if validSign(new_arg):
        return True
    return False

def main():
    print(parse("5 * X^0 + 4 * X^1 = 4 * X^0")) # Correct
    print(parse("5 * X^0 + 4 * X = 4 * X^0")) # Correct X or X^1
    print(parse("* X^0 + 4 * X^1 = 4 * X^0")) # Incorrect start with sign (before =)
    print(parse("5 * X^0 + 4 * X^1 + = 4 * X^0")) # Incorrect end with sign (before =)
    print(parse("5 * X^0 + 4 * X^1 = + 4 * X^0")) # Incorrect start with sign (after =)
    print(parse("5 * X^0 + 4 * X^1 = 4 * X^0 +")) # Incorrect end with sign (after =)
    print(parse("5 ** X^0 + 4 * X^1 = 4 * X^0")) # Incorrect double sign
    print(parse("5 * X^0 + 4 * X^1 == 4 * X^0")) # Incorrect double egal
    print(parse("5 * X^0 = + 4 * X^1 = 4 * X^0")) # Incorrect double equation
    print(parse("5a * X^0 + 4 * X^1 = 4 * X^0")) # Incorrect alphabetic character
    print(parse("a * X^0 + 4 * X^1 = 4 * X^0")) # Incorrect alphabetic character 2
    print(parse("= 5 * X^0 + 4 * X^1")) # Incorrect start with =
    print(parse("5 * X^0 + 4 * X^1 =")) # Incorrect end with =
    print(parse("5* X^0 + 4 * X^1 = 4 * X^0")) # Incorrect missing space
    print(parse("5 * X^0 + 4 * X^ = 4 * X^0")) # Incorrect missing expo after X^
    print(parse("5 * X^0 + 4 * X^1 = 4 * X^0")) # Incorrect


if __name__ == "__main__":
    main()


#DOUBLE SIGN +-
#Missing expo