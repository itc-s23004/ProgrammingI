import random

a = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
b = random.choice(a)
c = random.choice(a)


while True:
    if b == "g" and "t":
        print("g t")
        break
    else:
        for i in (b, c):
            print(b, c)
        b = random.choice(a)
        c = random.choice(a)
