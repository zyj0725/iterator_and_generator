'''
    写一个生成器函数primes(n) 来成生成n以内的所有素数
     1) 打印100 以内的全部素数
     2) 打印100 以内的全部素数的和
'''
def primes(n):
    if n < 2:
        pass
    for x in range(2,n):
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            yield  x

gene_primes = primes(100)
for prime in gene_primes:
    print(prime,end=' ')
print()
print("100以内素数的和为:",sum(primes(100)))