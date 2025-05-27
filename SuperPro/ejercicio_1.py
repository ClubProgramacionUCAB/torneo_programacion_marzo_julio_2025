inpt = input()

fours = {
    'I': 'V',
    'X': 'L',
    'C': 'D'
}

nines = {
    'I': 'X',
    'X': 'C',
    'C': 'M'
}

mult = {
    'I': 1,
    'X': 10,
    'C': 100,
}

vals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

sol = 0

skip = False

for i, ch in enumerate(inpt):
    if skip:
        skip = False
        continue
    if ch in ['I', 'X', 'C'] and i != len(inpt) - 1 and (fours[ch] == inpt[i + 1] or nines[ch] == inpt[i + 1]):
        next = inpt[i + 1]
        if fours[ch] == next:
            sol += 4 * mult[ch]
        if nines[ch] == next:
            sol += 9 * mult[ch]
        skip = True
    else:
        sol += vals[ch]

print(sol)
