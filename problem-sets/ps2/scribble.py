test = "rare"
L = ["f","t","r","e"]
guess = ""
for char in test:
    if char in L:
        guess += char
    else:
        guess += "*"
print(guess)