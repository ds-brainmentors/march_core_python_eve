Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "this is string"
>>> a.upper()
'THIS IS STRING'
>>> b = "THIS IS ANOTHER STRING"
>>> b.lower()
'this is another string'
>>> a.lower()
'this is string'
>>> a
'this is string'
>>> a = a.upper()
>>> a
'THIS IS STRING'
>>> a.title()
'This Is String'
>>> a.captalize()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.captalize()
AttributeError: 'str' object has no attribute 'captalize'
>>> a.capitalize()
'This is string'
>>> c = "fgRTYfcgvh"
>>> c.swapcase()
'FGrtyFCGVH'
>>> d = "xfdcgvb"
>>> d.isalpha()
True
>>> e = "cfgvh2345"
>>> e.isalpha()
False
>>> a
'THIS IS STRING'
>>> a.isalpha()
False
>>> f = "22145432"
>>> f.isdigit()
True
>>> e.isdigit()
False
>>> e.isalnum()
True
>>> a.isalnum()
False
>>> " ".isspace()
True
>>> "g ".isspace()
False
>>> a.isascii()
True
>>> a
'THIS IS STRING'
>>> a.index("T")
0
>>> a.index("IS")
2
>>> a.index(" ")
4
>>> a.index(" ", 5)
7
>>> a.index("IS", 3)
5
>>> a
'THIS IS STRING'
>>> a.replace("I", "O")
'THOS OS STRONG'
>>> a.replace("TH", "E")
'EIS IS STRING'
>>> a.replace("H", "O")
'TOIS IS STRING'
>>> "this is python".replace(" ", "")
'thisispython'
>>> 