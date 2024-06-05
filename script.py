import alphabets
phrase = str.lower(input("Input text: "))
output = str()
for i in phrase:
    if i in alphabets.ENG:
        language = alphabets.ENG
    elif i in alphabets.RU:
        language = alphabets.RU
    elif i in alphabets.NUMS:
        language = alphabets.NUMS
    index = language.index(i) + 1
    try:
        output += language[index]
    except IndexError:
        output += language[0]

print("Result: " + output)