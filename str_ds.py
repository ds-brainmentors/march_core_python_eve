Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3 - 5 // 4 % 4
4
>>> 5 / (2+3-5)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    5 / (2+3-5)
ZeroDivisionError: division by zero
>>> 5 * 5 ** 2 - 3 / 2 + 1
124.5
>>> 5 + 4 / 3 * 2 ** 4
26.333333333333332
>>> 4 / 3
1.3333333333333333
>>> 2 ** 2 ** 3
256
>>> s = ''
>>> type(s)
<class 'str'>
>>> s = " "
>>> type(s)
<class 'str'>
>>> s= ' "
SyntaxError: EOL while scanning string literal
>>> s = "this is python programming"
>>> s
'this is python programming'
>>> # indexing
>>> s[0]
't'
>>> s[1]
'h'
>>> s[2]
'i'
>>> s[9]
'y'
>>> s[12]
'o'
>>> s[4]
' '
>>> s[100]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s[100]
IndexError: string index out of range
>>> len(s)
26
>>> s[26]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[26]
IndexError: string index out of range
>>> s[25]
'g'
>>> s1 = input("Enter string: ")
Enter string: welcome to coding
>>> s1
'welcome to coding'
>>> s1[len(s1)-1]
'g'
>>> s1[len(s1)-3]
'i'
>>> s1[-1]
'g'
>>> s1[-4]
'd'
>>> s1[len(s1)]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s1[len(s1)]
IndexError: string index out of range
>>> s1[-len(s1)]
'w'
>>> len(s1)
17
>>> # slicing
>>> s
'this is python programming'
>>> s[0:5]
'this '
>>> s[2:10]
'is is py'
>>> s[5:100]
'is python programming'
>>> s[-5:-1]
'mmin'
>>> s[9:1]
''
>>> s[0:15:2]
'ti spto '
>>> s[0:15:3]
'tssyo'
>>> # s[start:stop:step]
>>> s[:5]
'this '
>>> s[4:]
' is python programming'
>>> s[:]
'this is python programming'
>>> s[-5:]
'mming'
>>> s[2:-2]
'is is python programmi'
>>> s[-5:25]
'mmin'
>>> s[9:1:-1]
'yp si si'
>>> s[10:0:-1]
'typ si sih'
>>> s[10:0:-2]
'tps i'
>>> s[::-1]
'gnimmargorp nohtyp si siht'
>>> # ask user to enter first name and last name. PRint them reverse
>>> # abc
>>> # xyz
>>> # zyx cba
>>> 
================== RESTART: D:/March/core_python_evening/ques_1.py ==================
enter first name: gautam
enter last name: gupta
atpug matuag
>>> 