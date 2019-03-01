'''
写一个生成器函数myodd(x) 来生成一系列奇数
    如:
      myodd(10) 可以生成1, 3, 5, 7, 9
'''

def myodd(x):
    for i in range(x):
        if i % 2 == 1:
            yield i

odd = myodd(10)
for x in odd:
    print(x,end=' ')
