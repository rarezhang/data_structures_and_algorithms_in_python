#################################################
# exercise
# R-1.1
def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False
print(is_multiple(10,5))
print(is_multiple(9,5))

# R-1.2
def is_even(k):
    if k % 2 == 0:
        return True
    else:
        return False
print(is_even(3))
print(is_even(-8))

# R-1.3
def minmax(data):
    min, max = data[0], data[0]
    for d in data:
        if d < min:
            min = d
        elif d > max:
            max = d
    return (min,max)
data = [10,9,5,1,2,26,5,5,8,9,6,-9]
print(minmax(data))

# R-1.4
def sum_square(n):
    # takes a positive integer n and returns
    # the sum of the squares of all the positive
    # integers smaller than n.
    s = 0
    for i in range(n):
        s += i**2
        #print(s)
    return s
print('R-1.4:',sum_square(5)) # 1+4+9+16 = 30

# R-1.5
# computes the sum from Exercise R-1.4,
# relying on Python’s comprehension syntax
# and the built-in sum function.
print(sum([i**2 for i in range(5)]))

# R-1.6
def sum_square_odd(n):
    # takes a positive integer n and returns
    # the sum of the squares of all the "odd" positive
    # integers smaller than n.
    s = 0
    for i in range(n):
        if i % 2 !=0:
            s += i**2
    return s
print("R-1.6:",sum_square_odd(5)) # 1 + 9 = 10

# R-1.7
print(sum([i**2 for i in range(10) if i % 2 != 0]))

# R-1.8
s = 'hello world'
n = len(s) # string s has length n
for i in range(len(s)):
    print("positive indices", s[i])
    print("negative indices", s[-n+i])

# R-1.9
## produce a range with values 50, 60, 70, 80
print(list(range(50,90,10))) # range(star,end,step)

# R-1.10
## produce a range with values
## 8, 6, 4, 2, 0, − 2, − 4, − 6, − 8
print(list(range(8,-10,-2)))

# R-1.11
##  produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
print([2**i for i in range(9)])

# R-1.12
##  returns a random element from a non-empty sequence
##  Using only the randrange function
import random
print(random.choice([0,1,2,3]))
print(random.randrange(4))  # return a random element from range(4) = [0,1,2,3]

# C-1.13
## reverses a list of n integers,
# so that the numbers are listed
# in the opposite order than they were before
lis = list(range(0,10,2))
print("R-1.13, original list:", lis)
lis_rev = []
while len(lis) != 0:
    lis_rev.append(lis.pop(len(lis)-1))
print("R-1.13, reversed list:", lis_rev)

# C-1.14
## takes a sequence of integer values.
## determines if there is a
## distinct pair of numbers in the sequence
## whose product is odd.
def product_id_odd(lis): # lis is []
    result =[]
    while len(lis) != 0:
        f = lis.pop(0)
        for i in lis:
            if f * i % 2 != 0:
                result.append((f,i))
    return result
l = list(range(6))
print(product_id_odd(l))

# C-1.15
# takes a sequence of numbers and determines
# if all the numbers are different from each other
def distinct_sequence(lis): # lis is []
    r = []
    for i in lis:
        if i not in r:
            r.append(i)
        else:
            return False
    return True
l1 = [8, 6, 4, 2, 0]
l2 = [8, 9, 9, 8]
print(distinct_sequence(l1))
print(distinct_sequence(l2))

# C-1.18
# produce the list
# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
l = [i*(i+1) for i in range(10)]
print(l)

# C-1.19
# comprehension syntax to produce the list [ a , b , c , ..., z ]
print(ord('a')) # get the asc_ii
print(chr(97))  # get the character from asc_ii
l = [chr(i) for i in range(ord('a'),ord('z')+1)]
print(l)

# C-1.20
# randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.
print(random.randint(0,10)) # return a int between 0 and 10
l = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
def custom_shuffle(lis):
    results = []
    index = []
    while len(results) != len(lis):
        i = random.randint(0,len(lis)-1)
        if i not in index:
            index.append(i)
            results.append(lis[i])
    return results
for i in range(10): # print out 10 shuffle results
    print(custom_shuffle(l))

# C-1.22
# takes two arrays a and b of length n
# storing int values, and
# returns the dot product of a and b
def dot_product(a,b):
    if len(a) != len(b):
        print('a and b should have same # of elements')
    else:
        return [aa*bb for aa,bb in zip(a,b)]

a = [1,2,3]
b = [2,3,4]
print(dot_product(a,b))

# C-1.24
## counts the number of vowels in a given
## character string.
def count_vowel(str):
    vowel = ['a','o','e','i','u']
    count = 0
    for s in str:
        if s in vowel:
            count += 1
    return count
s = 'hello world'
print('# of vowel in s:',count_vowel(s))

# C-1.25
print(ord('a')) # get the asc_ii: 97
print(ord('z')) # 122
print(ord('A')) # 65
print(ord('Z')) # 90
print(ord(' ')) # 32, space

def remove_punctuation(str):
    alph =[chr(32)] + [chr(i) for i in range(ord('A'),ord('Z')+1)] + [chr(i) for i in range(ord('a'),ord('z')+1)]
    result = []
    for s in str:
        if s in alph:
            result.append(s)
    return ''.join(result)
strs = 'Let\'s try, Mike'
print('original str:',strs)
print('remove punctuation:',remove_punctuation(strs))

# C-1.26
'''
a = int(input('please input an integer a'))
b = int(input('please input an integer b'))
c = int(input('please input an integer c, where c=a+b , c=a-b , c=a*b'))
if a+b == c:
    print('a+b=c')
elif a-b == c:
    print('a-b=c')
elif a*b == c:
    print('a*b=c')
else:
    print('wrong input')
'''

# C-1.27
def factors_3(n):
    k = 1
    res_1, res_2 = [],[]
    while k * k < n:   # will lost k * k = n
        if n % k == 0:
            res_1.append(k) # k
            res_2 = [n//k] + res_2
        k += 1
    if k * k == n:  # special case if n is square
        res_1.append(k)
    return res_1 + res_2
print(factors_3(100))

# C-1.28
# Euclidean norm of v.
def euclidean_norm(v): # v: list of numbers
    e = 0
    for i in v:
        e += i**2
    return e**0.5

print(euclidean_norm([3,4]))

# P-1.29
# Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
# recursion for permutation
# ! for recursion: analysis the first round very carefully
# permutation [a,b,c] = [a + permutation[b,c], b + permutation[a,c], c + permutation[a,b]]
# permutation[b,c] = [b + permutation[c]], permutation[c] = c
# permutation[a,c] = [a + permutation[c]], permutation[c] = c
# permutation[a,b] = [a + permutation[b]], permutation[b] = b
chas = ['c','a','t','d','o','g']
def permutation(chs):
    if len(chs) == 1:
        return chs
    results = []
    for c in chs:
        remaining_chs = [x for x in chs if x!=c]  # remaining list
        sub = permutation(remaining_chs)
        for s in sub:
            results.append(c+s)
    return results

print(permutation(chas))

# P-1.30
# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
def divide_2(i):
    if i < 0: print('please input a positive integer')
    if i >= 2:
        return 1 + divide_2(i/2)
    else:
        return 0

print(divide_2(30))

# P-1.30
# “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged.
def make_change(charge,given):
    change = float("{0:.1f}".format(given - charge))
    money = {100:'100$ bill', 20:'20$ bill', 10:'10$ bill', 5:'5$ bill', 1:'1$ bill', 0.5:'50c coin', 0.1:'10c coin'}
    m = [100,20,10,5,1,0.5,0.1]
    if change < 0:
        print('Money is not enough. You still own me:', abs(change))
    elif change == 0:
        print('Thank you for coming.')
    else:
        print('Here is your change.')
        for i in m:
            n = change // i
            if n != 0:
                print(int(n), ":",money.get(i))
                change = change % i

make_change(18.2,100)

# P-1.31
# calculator
'''
while True:
    first = float(input('Please input the first number:'))
    if isinstance(first, (float)):
        break
while True:
    sign = input('Please choose: + - * /:')
    if sign in ['+','-','*','/']:
        break
while True:
    second = float(input('Please input the second number:'))
    if isinstance(second, (float)):
        break
if sign == '+':
    print(first+second)
elif sign == '-':
    print(first-second)
elif sign == '*':
    print(first*second)
else:
    print(first/second)
'''

'''
# P-1.33
# simulates a handheld calculator.
import re
strs = input('this is a calculator, input your equation: x operator y >> ')
cal = re.search(r'([0-9]*\.?[0-9]*)([\+\-\*\/])([0-9]*\.?[0-9])',strs)
first, second = float(cal.group(1)), float(cal.group(3))
operator = cal.group(2)
s = "the result is: "
if operator == '+':
    print(s, first + second)
elif operator == '-':
    print(s, first - second)
elif operator == '*':
    print(s, first * second)
elif operator == '/':
    print(s, first / second)
else:
    print('there is something wrong with your input.')
'''

# P-1.34
import random
sentence = 'I will never spam my friends again.'
length = len(sentence)
times = 5
mistakes = 2
random_list = []
for i in range(mistakes):
    random_list.append(random.randint(1,times))
for i in range(times):
    if i in random_list:
        index = random.randint(0,length)
        print(i+1,':',sentence[:index]+sentence[index+3:])
    else:
        print(i+1,':',sentence)


# P-1.35
# birthday paradox
import random
test = range(5,105,5)
loop_time = 100
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for t in test:
    for l in range(loop_time):
        r = {}
        te = t
        count = 0
        while te > 0:
            mon = random.randint(1,12)
            day = random.randint(1,months.get(mon))
            birthday = str(mon) +'-'+str(day)
            if birthday in r:
                r[birthday]+=1
            else:
                r[birthday]=1
            te -= 1
            if any(v > 1 for v in r.values()): count+=1
    print(t,"people in the room, odds that people have the same birthday:",count/loop_time)

'''
# P-1.36
# Write a Python program that inputs a list of words, separated by white-
# space, and outputs how many times each word appears in the list.
def word_count(str): # string: list of words, separated by white space
    words = str.split()
    dictionary = {}
    for w in words:
        if w in dictionary: # if w is in the keys of the dictionary
            dictionary[w]+=1
        else:
            dictionary[w]=1
    for w,c in dictionary.items():
        print('word:',w,'# of times:',c)

#s = """As the first four major 2016 presidential hopefuls look to highlight their differences, one bond ties the quartet together: criticism of their campaign logos."""

#word_count(s)
'''