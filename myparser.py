def validSign(token, equal):
    if token in "+-*/=" and len(token) == 1:
        return True
    return False

def validValue(token):
    if token.isdigit() or token == "X":
        return True
    elif token.startswith("X^") and len(token) >= 3 and all(c in "0123456789" for c in token[2:]):
        return True
    return False

#if not all(c in "X0123456789^" for c in token):
#        return True