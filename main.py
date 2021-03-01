def e(num): return num ==1
a = [1,1,1]
def checkall( f, ls):
    return sum(list(map(f,ls))) == len(ls)
def checkone(f, ls):
    for i in ls: 
        if f(i): return True
    return False
print(checkall(lambda x: x == 1, a))
def sth(a):
    def inner(b):
        return a==b
    return inner
print(sth(10)(10))