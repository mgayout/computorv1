from cmpt import computor

def test(arg):
    print(arg)
    cmpt = computor(arg)
    print("-----------------------------")

def main():

    test("0 * X^1 = 0 * X^0")
    #test("5 * X^0 + 4 * X^0 - 99 * X^1 - 32 * X^0 = 4 * X^0 - 5 * X^0")
    #test("5 * X^0 + 4 * X^0 = 4 * X^0")
    #test("5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0")
    #test("8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0")
    #test("5 * X^0 + 4 * X^1 = 4 * X^0") # Correct
    #test("5 * X^0 + 4 * X = 4 * X^0") # Correct X or X^1
    #test("* X^0 + 4 * X^1 = 4 * X^0") # Incorrect start with sign (before =)
    #test("5 * X^0 + 4 * X^1 + = 4 * X^0") # Incorrect end with sign (before =)
    #test("5 * X^0 + 4 * X^1 = + 4 * X^0") # Incorrect start with sign (after =)
    #test("5 * X^0 + 4 * X^1 = 4 * X^0 +") # Incorrect end with sign (after =)
    #test("5 +* X^0 + 4 * X^1 = 4 * X^0") # Incorrect double sign
    #test("5 * X^0 + 4 * X^1 == 4 * X^0") # Incorrect double egal
    #test("5 * X^0 = + 4 * X^1 = 4 * X^0") # Incorrect double equation
    #test("5a * X^0 + 4 * X^1 = 4 * X^0") # Incorrect alphabetic character
    #test("a * X^0 + 4 * X^1 = 4 * X^0") # Incorrect alphabetic character 2
    #test("= 5 * X^0 + 4 * X^1") # Incorrect start with =
    #test("5 * X^0 + 4 * X^1 =") # Incorrect end with =
    #test("5* X^0 + 4 * X^1 = 4 * X^0") # Incorrect missing space
    #test("5 * X^0 + 4 * X^ = 4 * X^0") # Incorrect missing expo after X^

if __name__ == "__main__":
    main()
