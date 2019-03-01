"""
    创造迭代器对象
"""

# s  =  'python'
# it = iter(s)  #创建一个迭代器对象
# while True:
#     try:
#         print(next(it),end=' ')
#     except StopIteration:
#         pass

"""
    创建一个返回数字的迭代器，初始值为1，逐步递增1
"""
class myIterator:
    def __iter__(self):
        self.i = 1
        return self
    def __next__(self):
        n = self.i
        self.i += 1
        return n

iterClass = myIterator()
iTn = iter(iterClass)

for it in iTn:
    if it < 6:
        print(it,end=' ')

