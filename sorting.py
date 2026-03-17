print("hello world")
#这是一个计算定积分的函数
def integral(func, a, b, n):
    h = (b - a) / n
    total = 0
    for i in range(n):
        total += func(a + i * h)
    return total * h
