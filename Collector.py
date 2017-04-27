Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> [1,4,5,2,7]
[1, 4, 5, 2, 7]
>>> ['Bob', 'Sue']
['Bob', 'Sue']
>>> a = [1,2,3,4]
>>> names = ['Bob', 'Sue']
>>> a
[1, 2, 3, 4]
>>> names
['Bob', 'Sue']
>>> a[0]
1
>>> a[2]
3
>>> a[1]
2
>>> a[3]
4
>>> names[0]
'Bob'
>>> names[1]
'Sue'
>>> a.append(8)
>>> a
[1, 2, 3, 4, 8]
>>> a[4]
8
>>> a
[1, 2, 3, 4, 8]
>>> a[2]
3
>>> a[2] = 10
>>> a
[1, 2, 10, 4, 8]
>>> range(4,11)
range(4, 11)
>>> List(range(4,11))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    List(range(4,11))
NameError: name 'List' is not defined
>>> list(range(4,11))
[4, 5, 6, 7, 8, 9, 10]
>>> [x*2 for x in range(1,11)]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> list(range(2,21))
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
>>> [x for x in range(2,21)if x % 2 == 0]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> evens = [x for x in range(2,21)if x % 2 == 0]
>>> evens
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> a
[1, 2, 10, 4, 8]
>>> [y+1 for y in a]
[2, 3, 11, 5, 9]
>>> [z for z in a if z >= 8]
[10, 8]
>>> hi = 'hello world'
>>> hi
'hello world'
>>> hi[0]
'h'
>>> hi[10]
'd'
>>> list(hi)
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> ord('H)
    
SyntaxError: EOL while scanning string literal
>>> ord('H')
72
>>> [ord(x) for x in list(hi)]
[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
>>> 
