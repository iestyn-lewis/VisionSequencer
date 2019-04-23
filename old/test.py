# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:51:16 2015

@author: ilewis
"""


x = 'hello there'
print x
x = x.replace('there', 'abby')
print x

for i in range(1, 10):
    print 'hello' + ' ' + str(i)
    
a=[1,2,3,4,5,6,7]

print [num in a where num < 2]