s = input()
new_s = ""
shift = 2
alphavite = "абвгдеёжзийклмнопрстуфхцшщъьэюя"
for character in s:
    if character == " ":
        new_s += character
    else:
        j = 0
        for letter in alphavite:
             if letter == character:
                new_s += alphavite[(j + shift)%len(alphavite)]
                     j += 1
    print(new_s)
