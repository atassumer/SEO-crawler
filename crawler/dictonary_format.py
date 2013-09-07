names = ['a','b','c','d']

for i,k in enumerate(names):
    exec(k + '=%s' % i)  #k is the values

print a
print b
print c