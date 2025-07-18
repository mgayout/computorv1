
def validChar(arg):
    if not all(c in "X0123456789+-*/^= " for c in arg):
        return True
    return False

def validSign(arg):
    sign = False
    egal = 0
    for token in arg:
        #print(token, sign, egal)
        if sign is False:
            if token.isdigit():
                pass
            elif token == "X":
                pass
            elif token.startswith("X^") and all(c in "0123456789" for c in token[2:]):
                pass
            else:
                return True
        elif sign is True:
            if token in "+-*/":
                pass
            elif token == "=":
                egal += 1
            else:
                return True
        sign = not sign
    if egal != 1 or sign is False:
        return True
    return False