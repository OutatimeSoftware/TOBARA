def getTer(eq):

    terms = 0

    for char in eq:
        if (char == '+'):
            terms += 1

    return (terms + 1)