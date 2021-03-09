"""def valid_parentheses(string: str):
    if (len(string) == 0):
        return True
    else:
        parenteses = 0
        for caractere in string:
            if caractere == ')':
                parenteses += -1
                if parenteses < 0:
                    return False
            elif caractere == '(':
                parenteses += 1
        if parenteses == 0:
            return True
        else:
            return False"""


def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False


print(valid_parentheses("hi(hi)()"))
