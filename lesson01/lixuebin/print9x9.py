# 九九乘法表
a = 1
while a < 10:
    b = 1
    while True:
        if b <= a:
            print("{} x {} = {}".format(b, a, a*b),end="\t")
            b = b + 1
        else:
            print("")
            a = a + 1
            break


