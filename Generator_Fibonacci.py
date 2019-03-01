'''
    使用yield实现斐波那契数列
'''

def fibonacci(num):
    f1,f2,count = 0,1,0
    while count <= num:
        yield f1
        f1,f2 = f1+f2,f1
        count += 1

fib_gene = fibonacci(10)
while True:
    try:
        print(next(fib_gene),end=' ')
    except StopIteration:
        break

