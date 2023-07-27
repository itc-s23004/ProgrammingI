def make_addfunc():
    def add(x, y):
        return x + y

    return add


add_func = make_addfunc()
result = add_func(1, 10)
print(result)
