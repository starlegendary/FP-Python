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
def gib3(n):
    base =  [[1,1,1],[1,0,0],[0,1,0]]
    if(n == 0 or n == 1): return base

    fff = gib3(n//2)
    
    def mul(A,B):
        return list(map(lambda a: 
                    list(
                      map(lambda b:
                      sum(map(lambda x,y: x*y,a,b)),
                      [[B[j][i] for j in range(len(B))] 
                      for i in range(len(B[0]))])
                    )
                    ,A))
                    
    fff = mul(fff,fff) 
    if n%2 == 0:return fff 
    else: return mul(fff,base)

def rev(ls): #reverse a list recursion
      if len(ls) <= 1: return ls
      print(ls[1:-1])
      rest = rev(ls[1:-1])
      print(rest)
      return [ls[-1]]+rest+[ls[0]]

def ps(n): #print triangle dots
    if(n == 0): return "*" 
    print('*'*n)
    rest = ps(n-1)
    print(rest)
    return rest + "*"
def seq(n,i ):
    if i == 0: return ['0'*(2*n)]
    result = seq(n,i-1)
    rest = []
    part = list(map("".join,set(perm( '1'*i + '0'*(n-i) ,n))))
    for x in part:
        rest += list(map(lambda y: x+y, part))

    return result + rest

def seq3(n):
    from itertools import permutations as perm
    def inner(s):
        if '1' not in s: return [s]
        result = inner('0'+s[:-1])
        rest = []
        part = list(map("".join,set(perm(s,len(s)))))
        for x in part:
            rest += list(map(lambda y: x+y, part))

        return result + rest
    return inner('1'*n)
def fib(n):
    if n < 2: return 1
    else: return fib(n-1)+fib(n-2)
def gib(n, mem):
    if len(mem) > n: return mem[n]
    else: 
        mem.append(gib(n-1, mem)+gib(n-2, mem))
        return mem[-1]
for i in range(10):
    print(gib3(i)[0][0])