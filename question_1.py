def balanced_parenthesis(a):
    s = []

    for i in a:
        if i in ['(', '[', '{']:
            s.append(i)

        else:
            if len(s) == 0:
                return False
            elif i == '}' and (s[-1] in ['[', '(']):
                return False
            elif i == ']' and (s[-1] in ['(', '{']):
                return False
            elif i == ')' and (s[-1] in ['{', '[']):
                return False
            else:
                s.pop()
    return len(s) == 0
