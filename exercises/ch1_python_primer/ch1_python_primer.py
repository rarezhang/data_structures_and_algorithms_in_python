## this project is running by python 3.4.3
# file - setting - project: xxxx - project interpreter

__author__ = 'wlz'

import sys
#print(sys.version)  # python 3.4.3

'''
# p25
print( 'Welcome to the GPA calculator. ')
print( 'Please enter all your letter grades, one per line. ')
print( 'Enter a blank line to designate the end.' )
points = { 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67,'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}
num_courses = 0
total_points = 0
done = False

while not done:
    grade = input()
    if grade == '':
        done = True
    elif grade not in points:   # not the keys of points
        print("Unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))
'''
########################################################################
'''
# The bool class
print(bool())  # return False
foo = 'non-empty string'
num = 1
print(bool(foo))
print(bool(num))

# The int class
## binary, octal, or hexadecimal
int_1 = 10   # Decimal
int_2 = 0b001 # binary: 0bxxxxxxx
int_3 = 0o52 # octal: 0oxxxxxxxxx
int_4 = 0x7f # hexadecimal: 0x xxxxxxx
print(int_1,int_2,int_3,int_4) # print out as decimal
print(bin(10))  # decimal to binary
print(bin(0o52)) # octal to binary
print(bin(0x7f))  # hexadecimal to binary
## to hex
print(hex(int_1))
## to decimal
print(int('1010',2))
print(int('0xa',16))
## truncate
print(int(3.14),int(3.99))  # all return 3
print(int(-3.99))  # return -3
str = '125'
print(int(str))  # the base must be 10
str = '7f'
print(int(str, 16))  # if the base is not 10, must point out

# The float class
f = 2.   # float
print(f)
f = 3e4
print(f)
print(float('7'))  # string to folat

# The sequence class
## list, tuple, string
str = 'hello'
print(str*4)
print(list(str)) # string to list
a = ['h', 'e', 'l', 'l', 'o']
print(".".join(a)) # list to string
# a tuple of length one
a = (1)
b = (1,)
print(type(a))  # class int
print(type(b))  # class tuple
str = 'don\'t worry'  # \ is the escape character
print(str)
print(str+'\n'+str) # \n new line
print(str+'\t'+str) # \t tab
print('20\u20AC')

# set
## math set: no duplicates, no order
## VS list: check if an element is in a set
set_1 = {'red','blue','green'} # actually this is hash table
print(set_1)
list_1 = ['red','blue','green']
print(set(list_1)) # list to set
print(list(set_1)) # set to list

# dictionary
## hash table -> key:value
d = { 'ga' : 'Irish' , 'de' : 'German' }
print(d.keys()) # a list of keys
print(d.values()) # a list of values
print(d.items()) # a list of tuples

# Arithmetic Operators
print(10/3)  # get float
print(10//3)  # get int
'''

########################################################################
# function
'''
## default value
def add_all(a,b=1,c=1):   # the default value for b and c
    return a+b+c

print(add_all(5)) # return 7
print(add_all(5,2,2)) # return 9
print(add_all(a=5,c=2)) # return 8
'''
######################################################################################
'''
# example to use default value
## function to calculate grades, can change points
def compute_gpa(grades, points={'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points: # compare g with points.keys
            num_courses += 1
            total_points += points[g]
    return total_points / num_courses

print(compute_gpa(['A','B']))
# change A:4.0 -> A:3.8
print(compute_gpa(['A','B'],points={'A+': 4.0, 'A': 3.8, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}))

# hash function
h = hash('1')
b = hash('a')
print(h,b, sep='<->') # define separator in the print function
'''
#################################################################################
'''
# raising an exception
def absolute(a):
    if a < 0:
        raise ValueError('\'a\' cannot be negative!')
    else:
        return -a
print(absolute(5))
#print(absolute(-5))

# check the type of the input
def check_type(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numeric')
    else:
        print('this is numeric data')

check_type(1.5)
#check_type('string')
'''
###############################################################################
'''
## python generator
def factors(n):
    for k in range(1,n+1):   # actually generate [1....n]
        if n % k ==0:
            yield k   # use yield instead of return
            # if use return, there will be only one element
print(list(factors(100)))

### a more efficient way
def factors_2(n):
    k = 1
    while k * k < n:   # will lost k * k = n
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:  # special case if n is square
        yield k
print(list(factors_2(100)))  #not generated in strictly increasing order
'''
###########################################
'''
#Comprehension Syntax
lis = range(10)
print(lis)
## list comprehension
print([i*i for i in lis])
print([i for i in lis if i > 4])
## set comprehension
print({i**3 for i in lis})
## dictionary comprehension
print({i: i**2 for i in lis if i > 3})  ## get a dictionary quickly
'''
#################################################
'''
# Packing and Unpacking of Sequences
a,b,c,d = range(4)
print(a) # return 0
a = range(4)
print(list(a)) # return list [1,2,3,4]
'''
