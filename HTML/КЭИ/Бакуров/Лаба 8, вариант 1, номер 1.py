def f():
    def g(x):
        return x + 5
    return g
k = int(input(": "))
cnt = f()
print(cnt(k))