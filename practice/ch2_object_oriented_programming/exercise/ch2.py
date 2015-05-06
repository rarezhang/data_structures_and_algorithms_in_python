# R-2.4
from classes.Flower import Flower
rose = Flower()
# default object value
print(rose._name, rose._petal, rose._price)
# setting the value
rose.set_name("rose: American Beauty")
rose.set_petal(10)
rose.set_price(8.5)
print(rose._name, rose._petal, rose._price)
# getting the value
print(rose.get_name(),rose.get_petal(),rose.get_price())

# R-2.5
## test 'charge' and 'make_payment' method, input must be a number
from classes.CreditCard import CreditCard
my_credit_card = CreditCard("wenli zhang", "ICBC", "123 456 789", 1000)
my_credit_card.charge(100)
print(my_credit_card._balance)
my_credit_card.make_payment(100)
print(my_credit_card._balance)
#my_credit_card.charge('str') # will raise a type error

# R-2.6
## test make_payment method, input must be a positive number
#my_credit_card.make_payment(-10) # will raise a type error

# R-2.7
## test the "nonzero balance using an optional ﬁfth parameter"
my_cc = CreditCard('cate', 'Chase', '345 213 456', 1000)
print(my_cc._balance) # default balance is 1
my_cc = CreditCard('cate', 'Chase', '345 213 456', 1000, 55)
print(my_cc._balance) # use the input variable balance = 55

# R-2.9
from classes.Vector import Vector
## test Vector __sub__ method
v1, v2 = Vector(3), Vector(3)
print(v1, v2)
for i in range(3):
    v1[i] = i+2
    v2[i] = i+1
print(v1, v2)
print(v1-v2)

# R-2.10
## test Vector __neg__
v = Vector(0)
print(v)
v = Vector(5)
print(v)
for i in range(5):
    v[i] = i * 3
print(v)
print(-v)

# R-2.11
u = v + [1,2,3,4,5]
print(u)
u = [1,2,3,4,5] + v
print(u)

# R-2.12
print(u)
print(u*3)
print(u*1.9)

# R-2.13
print(3*u)

# R-2.14
# C-2.25
# mul method for the Vector class, can multiply a number and vector
print(v,u)
print(v*3)
print(v*u) # dot product

# R-2.15
# test the Vector constructor: take an int or a list
ve = Vector(4)
print(ve)
li = [1,2,3,4]
ve = Vector(li)
print(ve)
li = []
ve = Vector(li)
print(ve)

# R-2.17
from classes.Animal import *
a = Animal()
r = Racer(1,'red')

# R-2.18
from classes.Progression import *
FibonacciProgression(2,2).print_progression(8)  # start value 2 and 2, find the 8th value

# R-2.19
#print(2**63/128)  # 7.205759403792794e+16
ArithmeticProgression(128,0).print_progression(10) # increment 128, start with 0

# R-2.22
from classes.sequence_abc import Sequence

# C-2.24
class Book:
    """
    all the books in the store
    """
    def __init__(self):
        self._bookname = 'book name'
        self._ISBN = 'X123456789'
        self._author = ['author 1', 'author 2']
        self._stock = 1
        self.price = 10.0

class User:
    """
    all the users
    """
    def __init__(self):
        self._username = 'default user name'
        self._purchased = ['book 1','book 2']
        self._balance = 100.00 # dollars

    def view_book_list(self):
        return self._purchased


class Buy:
    """
    user buy a book
    """
    def __init__(self):
        self._transaction = 't125'

    def buy(self, book, user):
        # check stock from book class
        # check balance from user class
        # if success
            # book stock -1
            # user balance - book.price, user.purchased.append(book name)
        pass

class Read:
    """
    user read a book
    """
    def __init__(self):
        self._software = 'pdf reader'

    def read(self,user,book):
        # check if book in user.purchased
            # if success:
            # read book
        pass

# C-2.26
from classes.ReversedSequenceIterator import *
li = [1,1,2,3,4,6,8,4,5,6]
s = ReversedSequenceIterator(li)
for i in range(len(li)):
    print(next(s))

# C-2.27
from classes.Range import *
r = Range(1,22,3) # start, stop, step
print(list(r))
if 7 in r:
    print('test the __contain__ method, in')
if 5 in r:
    print('test __contain__ method, not in')
else:
    print('success')

# C-2.28
from classes.CreditCard import *
my_credit_card2 = PredatoryCreditCard('wenli','ICBC','X0125 4589 1458',1000,10,0.085,5)
print('initial balance:', my_credit_card2.get_balance()) # 10
for i in range(15):
    my_credit_card2.charge(1)
    print('current calls:', i+5, 'balance:',my_credit_card2.get_balance())

# C-2.29
print('initial balance:', my_credit_card2.get_balance()) # 34, mini_pay:34*0.3=10.2
my_credit_card2.make_payment(9)
print(my_credit_card2.get_balance()) # 34-9+5(late fee)

# C-2.30
print('initial balance:', my_credit_card2.get_balance())
my_credit_card2.charge(10)
print('current balance:', my_credit_card2.get_balance())

# C-2.31
AbsoluteProgression().print_progression(10)
AbsoluteProgression(2,200).print_progression(10)
AbsoluteProgression(200,2).print_progression(10)

# C-2.32
SquarerootProgression().print_progression(10)