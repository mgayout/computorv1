def validSign(token):
    if token in "+-*/=" and len(token) == 1:
        return True
    return False

def validValue(token):
    if token.isdigit():
        return True
    if '.' in token and token[0] != '.' and token[len(token) - 1] != '.':
        return True
    elif token.startswith("X^") and len(token) >= 3 and all(c in "0123456789." for c in token[2:]):
        return True
    return False
