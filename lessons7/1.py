def get_sum (*args):
    res = 0
    for i in args:
        res += i

    return res;
args1 = [2, 3, 5, 5, 5, 5, 5]
print(get_sum(*args1))