a = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]

def str_to_float_coordi(s):
    p = s.split(",")
    return list(map(float, p))

def str_to_float_coordi_list(s_list):
    return list(map(str_to_float_coordi, s_list))

f_coordi_list = str_to_float_coordi_list(a)

print(f_coordi_list)

