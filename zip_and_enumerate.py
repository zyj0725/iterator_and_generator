'''
    zip(iter1,iter2,iter3...)
    enumerate(iterable,start=0)
'''

bank = ['工商银行','农业银行','中国银行','建设银行','交通银行']
tel_num = [95588,95599,95566,95533,95559,10086]
for b in zip(bank):
    print(b)
print()
for b,t in zip(bank,tel_num):
    print(b,t)
print()
for n,b,t in zip(range(3),bank,tel_num):
    print(n,b,t)
print()
for b in enumerate(bank):
    print(b)
print()
for b in enumerate(bank,start=10):
    print(b)
print()