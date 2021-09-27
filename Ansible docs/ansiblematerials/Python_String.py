Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> type(x)
<class 'int'>
>>> name="Raghul Ramesh"
>>> type(name)
<class 'str'>
>>> y="20"
>>> type(y)
<class 'str'>
>>> today=thursday
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    today=thursday
NameError: name 'thursday' is not defined
>>> name="Raghul Ramesh"
>>> len(name)
13
>>> name[0]
'R'
>>> name[1]
'a'
>>> name[5]
'l'
>>> name[0:5]
'Raghu'
>>> name[0:6]
'Raghul'
>>> name[:6]
'Raghul'
>>> name[7:]
'Ramesh'
>>> name[0]
'R'
>>> name[1]
'a'
>>> name[12]
'h'
>>> name[-1]
'h'
>>> name
'Raghul Ramesh'
>>> name[-2]
's'
>>> name[-6:]
'Ramesh'
>>> name[7:]
'Ramesh'
>>> name[7:12]
'Rames'
>>> name[7:13]
'Ramesh'
>>> name
'Raghul Ramesh'
>>> name[:]
'Raghul Ramesh'
>>> name[::2]
'Rgu aeh'
>>> name[::3]]
SyntaxError: unmatched ']'
>>> name[::3]
'Rh mh'
>>> name[::-1]
'hsemaR luhgaR'
>>> name[5]
'l'
>>> name[1::2]
'ahlRms'
>>> name='Raghul Ramesh'
>>> name
'Raghul Ramesh'
>>> name="Raghul Ramesh"
>>> name
'Raghul Ramesh'
>>> tech="Python Programming"
>>> tech='Python Programming'
>>> college="st's joseph engineering college"
>>> college
"st's joseph engineering college"
>>> university=""SRM" University"
SyntaxError: invalid syntax
>>> university='"SRM" University'
>>> university
'"SRM" University'
>>> mycar="\"EcoSport\" is my car it got manafactured by 'FORD' motor company"
>>> mycar
'"EcoSport" is my car it got manafactured by \'FORD\' motor company'
>>> mycar='"EcoSport" is my car it got manafactured by \'FORD\' motor company'
>>> mycar
'"EcoSport" is my car it got manafactured by \'FORD\' motor company'
>>> print(mycar)
"EcoSport" is my car it got manafactured by 'FORD' motor company
>>> about_python="Python was developed by Guido van rossum.
SyntaxError: EOL while scanning string literal
>>> about_python='''Python was developed by Guido van rossum.
He is from netherland.
It was released on 1991.
'''
>>> print(about_python)
Python was developed by Guido van rossum.
He is from netherland.
It was released on 1991.

>>> about_python='''Python was developed by Guido van rossum.
He is from netherland.
It was released on 1991.'''
>>> print(about_python)
Python was developed by Guido van rossum.
He is from netherland.
It was released on 1991.
>>> tech_list='''Python
AI
Spark
Cloud
Devapps
Perl
Unix
Oracle
Java
Mainframe'''
>>> print(tech_list)
Python
AI
Spark
Cloud
Devapps
Perl
Unix
Oracle
Java
Mainframe
>>> tech_list1="Python
SyntaxError: EOL while scanning string literal
>>> '''Python
AI
Spark
Cloud
Devapps
Perl
Unix
Java
MainFrame'''
'Python\nAI\nSpark\nCloud\nDevapps\nPerl\nUnix\nJava\nMainFrame'
>>> #First line
>>> #Secondline
>>> #Third line
>>> '''
First line
Second line
third line'''
'\nFirst line\nSecond line\nthird line'
>>> name
'Raghul Ramesh'
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> name
'Raghul Ramesh'
>>> name.upper()
'RAGHUL RAMESH'
>>> name
'Raghul Ramesh'
>>> name.lower()
'raghul ramesh'
>>> name
'Raghul Ramesh'
>>> name.swapcase()
'rAGHUL rAMESH'
>>> name="raghul ramesh"
>>> name
'raghul ramesh'
>>> name.capitalize()
'Raghul ramesh'
>>> name
'raghul ramesh'
>>> name.title()
'Raghul Ramesh'
>>> name
'raghul ramesh'
>>> name="Raghul Ramesh"
>>> name
'Raghul Ramesh'
>>> name.casefold()
'raghul ramesh'
>>> help(name.casefold)
Help on built-in function casefold:

casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.

>>> name="Malini"
>>> name.isalpha()
True
>>> salary="1000"
>>> salary.isalpha()
False
>>> salary.isdigit()
True
>>> name.isdigit()
False
>>> dir(name)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> eid="rraghu12"
>>> eid.isalnum()
True
>>> name
'Malini'
>>> name.isupper()
False
>>> tech="PYTHON"
>>> tech.isupper()
True
>>> tech.islower()
False
>>> name.istitle()
True
>>> name="   Raghul Ramesh    "
>>> name
'   Raghul Ramesh    '
>>> name.strip()
'Raghul Ramesh'
>>> name
'   Raghul Ramesh    '
>>> tech
'PYTHON'
>>> tech.strip()
'PYTHON'
>>> name
'   Raghul Ramesh    '
>>> name.lstrip()
'Raghul Ramesh    '
>>> name.rstrip()
'   Raghul Ramesh'
>>> city="Chennai-Bangalore-Hyderabad-Pune-Mumbai-Kolkatta-Delhi"
>>> print(city)
Chennai-Bangalore-Hyderabad-Pune-Mumbai-Kolkatta-Delhi
>>> city.split("-")
['Chennai', 'Bangalore', 'Hyderabad', 'Pune', 'Mumbai', 'Kolkatta', 'Delhi']
>>> tech
'PYTHON'
>>> tech.index('T')
2
>>> tech.find('T')
2
>>> name="Raghul Ramesh Chennai"
>>> name.find("Chennai")
14
>>> name.index("Chennai")
14
>>> name.index('z')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    name.index('z')
ValueError: substring not found
>>> name.find('z')
-1
>>> name
'Raghul Ramesh Chennai'
>>> name.index('a')
1
>>> help(name.index)
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> name.find('a')
1
>>> name.rindex('a')
19
>>> name.rfind('a')
19
>>> name="Raghul Ramesh"
>>> name.center(30)
'        Raghul Ramesh         '
>>> name.center(30,"-")
'--------Raghul Ramesh---------'
>>> name.center(30,"*")
'********Raghul Ramesh*********'
>>> name.center(50,"*")
'******************Raghul Ramesh*******************'
>>> name.ljust(30)
'Raghul Ramesh                 '
>>> name.ljust(30,"-")
'Raghul Ramesh-----------------'
>>> name.rjust(30)
'                 Raghul Ramesh'
>>> name.rjust(30,"-")
'-----------------Raghul Ramesh'
>>> name="Ramesh from Chennai which is part of India"
>>> name
'Ramesh from Chennai which is part of India'
>>> name.replace('Chennai','Bangalore')
'Ramesh from Bangalore which is part of India'
>>> name="Ramesh is from chennai and he is working in chennai as chennai is his hometown"
>>> name
'Ramesh is from chennai and he is working in chennai as chennai is his hometown'
>>> name.repalce("chennai","Pune")
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    name.repalce("chennai","Pune")
AttributeError: 'str' object has no attribute 'repalce'
>>> name.replace("chennai","Pune")
'Ramesh is from Pune and he is working in Pune as Pune is his hometown'
>>> name.replace("chennai","Pune",1)
'Ramesh is from Pune and he is working in chennai as chennai is his hometown'
>>> name.replace("chennai","Pune",2)
'Ramesh is from Pune and he is working in Pune as chennai is his hometown'
>>> name="Raghul Ramesh"
>>> name.replace('a','A')
'RAghul RAmesh'
>>> name.replace('ae','AE')
'Raghul Ramesh'
>>> make.translate('ae','AE')
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    make.translate('ae','AE')
NameError: name 'make' is not defined
>>> name.translate('ae','AE')
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    name.translate('ae','AE')
TypeError: translate() takes exactly one argument (2 given)
>>> name.maketrans('ae','AE')
{97: 65, 101: 69}
>>> ord('a')
97
>>> ord('A')
65
>>> ord('e')
101
>>> ord('E')
69
>>> change=name.maketrans('ae','AE')
>>> name.translate(change)
'RAghul RAmEsh'
>>> name="I!n@dia"
>>> ord('!')
33
>>> ord('@')
64
>>> name.maketrans('a','XY')
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    name.maketrans('a','XY')
ValueError: the first two maketrans arguments must have equal length
>>> name
'I!n@dia'
>>> name.translate({33:None,64:None})
'India'
>>> 