Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spam = [['cat', 'bat'], [10,20,30,40]]
spam
[['cat', 'bat'], [10, 20, 30, 40]]
spam.append(30,20,10)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    spam.append(30,20,10)
TypeError: list.append() takes exactly one argument (3 given)
spam = [['cat', 'bat'], [10,20,30,40], [30,20,10,5]]
spam
[['cat', 'bat'], [10, 20, 30, 40], [30, 20, 10, 5]]
spam[2]
[30, 20, 10, 5]
spam[2][1]
20
spam[1][1]
20
spam[1][0]
10
spam[2][3]
5
spam[0][1]
'bat'
spam=['cat', 'bat', 'dog', 'elephet']
spam[-2]
'dog'
spam[-3]
'bat'
spam[-1]
'elephet'
'The story of ' + spam[-1] + 'bitting' + 'a' + spam[-2] + ''
'The story of elephetbittingadog'
spam
['cat', 'bat', 'dog', 'elephet']
spam[1:3]
['bat', 'dog']
spam[0:4]
['cat', 'bat', 'dog', 'elephet']
len()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
len(una)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    len(una)
NameError: name 'una' is not defined
len(spam)
4
spam
['cat', 'bat', 'dog', 'elephet']
spam[1] = 'chocolate'
sapm
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    sapm
NameError: name 'sapm' is not defined
spam
['cat', 'chocolate', 'dog', 'elephet']
spam[1] = spam[3]
spam
['cat', 'elephet', 'dog', 'elephet']
spam[-1]
'elephet'
spam[-1] = 1234
spam
['cat', 'elephet', 'dog', 1234]
del
SyntaxError: invalid syntax
spam
['cat', 'elephet', 'dog', 1234]
spam * 2
['cat', 'elephet', 'dog', 1234, 'cat', 'elephet', 'dog', 1234]
spam
['cat', 'elephet', 'dog', 1234]
del spam[2]
spam
['cat', 'elephet', 1234]

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter the name of cat 1: 
dat
Enter the name of cat 2: 
fat
Enter name of cat 3: 
gat


================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter the name of cat 1: 
dat
Enter the name of cat 2: 
fat
Enter name of cat 3: 
gat
dat fatgat

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter the name of cat 1: 
fat
Enter the name of cat 2: 
gat
Enter name of cat 3: 
hat
fat gat hat

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
dat
Enter a name of cat 1 Or Enter nothing to stop program
casp
Enter a name of cat 2 Or Enter nothing to stop program
fat
Enter a name of cat 3 Or Enter nothing to stop program
gat
Enter a name of cat 4 Or Enter nothing to stop program
hatp
Enter a name of cat 5 Or Enter nothing to stop program
goldf
Enter a name of cat 6 Or Enter nothing to stop program
salku
Enter a name of cat 7 Or Enter nothing to stop program
galk
Enter a name of cat 8 Or Enter nothing to stop program
earn
Enter a name of cat 9 Or Enter nothing to stop program
sald
Enter a name of cat 10 Or Enter nothing to stop program

The cat name are: 
 dat
 casp
 fat
 gat
 hatp
 goldf
 salku
 galk
 earn
 sald

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
wea
Traceback (most recent call last):
  File "C:/Users/Exodus/Desktop/allMyCats.py", line 9, in <module>
    catNames = catNames + name
TypeError: can only concatenate list (not "str") to list
spam
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
sap = ['Newton', 'america', 'Brazi;', 'Cerman']
sap
['Newton', 'america', 'Brazi;', 'Cerman']
newton in sap
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    newton in sap
NameError: name 'newton' is not defined
Newton in sap
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    Newton in sap
NameError: name 'Newton' is not defined
sap
['Newton', 'america', 'Brazi;', 'Cerman']
Newton in ['Newton', 'america', 'Brazi;', 'Cerman']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    Newton in ['Newton', 'america', 'Brazi;', 'Cerman']
NameError: name 'Newton' is not defined
'Newtop' in sap
False
cat = ['fat','black', 'loud']
size, color, disposition = cat
cat
['fat', 'black', 'loud']
size
'fat'
black
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    black
NameError: name 'black' is not defined
size
'fat'
color
'black'
cat
['fat', 'black', 'loud']
size
'fat'
color
'black'
disposion
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    disposion
NameError: name 'disposion' is not defined. Did you mean: 'disposition'?
spam
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    spam
NameError: name 'spam' is not defined
sap
['Newton', 'america', 'Brazi;', 'Cerman']
sap.index(america)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    sap.index(america)
NameError: name 'america' is not defined
sap.index('america')
1
sap.index('cash')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    sap.index('cash')
ValueError: 'cash' is not in list

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
tad
Traceback (most recent call last):
  File "C:/Users/Exodus/Desktop/allMyCats.py", line 3, in <module>
    print('Enter a name of cat ' + str(len(catNames)) + ' Or Enter nothing to stop program')
TypeError: object of type 'NoneType' has no len()

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
taf
Traceback (most recent call last):
  File "C:/Users/Exodus/Desktop/allMyCats.py", line 3, in <module>
    print('Enter a name of cat ' + str(len(catNames)) + ' Or Enter nothing to stop program')
TypeError: object of type 'NoneType' has no len()

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
dat
Traceback (most recent call last):
  File "C:/Users/Exodus/Desktop/allMyCats.py", line 3, in <module>
    print('Enter a name of cat ' + str(len(catNames)) + ' Or Enter nothing to stop program')
TypeError: object of type 'NoneType' has no len()

================= RESTART: C:/Users/Exodus/Desktop/allMyCats.py ================
Enter a name of cat 0 Or Enter nothing to stop program
ter
Enter a name of cat 1 Or Enter nothing to stop program

The cat name are: 
 ter
sap
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sap
NameError: name 'sap' is not defined. Did you mean: 'map'?
def = ['Error']
SyntaxError: invalid syntax
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam
['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
['bat', 'rat', 'cat', 'hat', 'cat']
spam=[-2.-1,3.14.4,10,0,11,6,8]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
spam=[-2.-1,3.14,10,0,11,6,8]