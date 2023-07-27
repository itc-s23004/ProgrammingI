s = ""
for i in range(1, 10):
    for j in range(1, 10):
        b = i * j
        s += "{:2d},".format(b)
    s += "\n"

print(s)
