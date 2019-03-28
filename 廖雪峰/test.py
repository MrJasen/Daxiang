# words = ['a','b','c']
# for w in  words:
#     print(w,len(w))

# for a in range(5):
#     print(a)

def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b

fib(10)