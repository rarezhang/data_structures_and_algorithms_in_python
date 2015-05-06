# main
# P95
from classes.CreditCard import CreditCard
import random
# test the CreditCard class
# create 3 credit card accounts
wallet = []
wallet.append(CreditCard('John Bowman','California Saving','123 456',5000))
wallet.append(CreditCard('John Bowman','California Federal','852 569',4000))
wallet.append(CreditCard('John Bowman','California Finance','789 456',9000))

# charge certain money from each account
for val in range(1,17):
    wallet[0].charge(val*random.randint(1,5))
    wallet[1].charge(val*random.randint(1,5))
    wallet[2].charge(val*random.randint(1,5))

# check current accounts
for c in range(3):
    print("customer:", wallet[c].get_customer())
    print("bank:", wallet[c].get_bank())
    print("account:", wallet[c].get_account())
    print("limit:", wallet[c].get_limit())
    print("balance:", wallet[c].get_balance())
    while wallet[c].get_balance()>300:
        wallet[c].make_payment(300)
        print('new balance:', wallet[c].get_balance())
    print('--------------------')




# P99
# test the Vector class
from classes.Vector import Vector
# create a vector
v = Vector(5) # 5 elements in the vector
print(v)
# set the element, __setitem__
v[1]=23
v[-1] = 45
print(v)
# add two vectors. __add__
u = v + v
print(u)
# implicit iteration
total = 0
# __len__
# __getitem__
for element in v:
    total += element
print(v,total)


# P 101
# test the Vector class
from classes.SequenceIterator import SequenceIterator
seq = SequenceIterator([1,2,3,4,5])
for s in seq:
    print("s",s)
## how to use next() ??

# P 102
## test range(), lazy evaluation
r = range(1,10)
print(r)
print(len(r))
print(r[0])

# test PredatoryCreditCard class
from classes.CreditCard import PredatoryCreditCard
mycd = PredatoryCreditCard('John Bowman','California Saving','123 456',5000,0.085)
mycd.process_month()

# P 114
## test the Progression class
## unit test
from classes.Progression import Progression, ArithmeticProgression, GeometricProgression, FibonacciProgression
print('Default progression:')
Progression().print_progression(10)
p = Progression()
print(p.print_progression(5))

print('Arithmetic progression:')
ArithmeticProgression(5).print_progression(4) # increment 5
ArithmeticProgression(5,2).print_progression(4) # increment 5, start with 2

print('Geometric progression:')
GeometricProgression().print_progression(10) # default base
GeometricProgression(3).print_progression(10) # base 3

print('Fibonacci progression:')
FibonacciProgression().print_progression(10) # default start value
FibonacciProgression(4,5).print_progression(10) # with start value 4 and 5

# test SequenceIterator
from classes.SequenceIterator import *
li = [1,1,2,3,4,6,8,4,5,6]
s = SequenceIterator(li)
for i in range(len(li)):
    print(next(s))