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
def fib3(n):
  
    if(n == 0 or n == 1): return [[1,1],[1,0]]
    fff = fib3(n//2)
    def mul(A,B):
        BT = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
        return list(map(lambda a: 
                    list(
                      map(lambda b:
                      sum(map(lambda x,y: x*y,a,b)),BT)
                    )
                    ,A))
    if n%2 == 0:return mul(fff,fff) 
    else: return mul(mul(fff,fff),[[1,1],[1,0]])

aa = []
dd ='aa'
aa+=list(dd)
print(aa)