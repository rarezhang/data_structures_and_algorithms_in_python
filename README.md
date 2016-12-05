# Data Structures and Algorithms in Python  

https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275  

## My solutions to exercises in ```Data Structures and Algorithms in Python```   
[click here](https://github.com/rarezhang/data_structures_and_algorithms_in_python/tree/master/exercises)  


# Reading notes  

### designing recursive algorithms  
P 199  
1. __test for base cases__: at least one; every recursive calls will eventually reach a base case; handling of each base case should not use recursion  
2. __recur__: if not a base case, perform one or more recursive calls; makes progress towards a base case  
3. __parameterization__: public use -> cleaner interface; nopublic function -> having the desired recursive parameters

### why recursion  
P 200  
advantage:  
1. avoid complex case analyses and nested loops  
2. more readable algorithm descriptions  
disadvantage:  
1. keep track of nested call (memory issue)  
2. stack data structure: convert a recursive algorithm into a nonrecursive algorithm (memory: storing only minimal information)  

### tail recursion  == linear recursion  
P 200  
- any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing recursion  
- any tail recursion can be reimplemented nonrecursively by enclosing the body in a loop for repetition, and replacing a recursive call with new parameters by a reassignment of the existing parameters to those values  

### recursion tips
replace a recursive algorithm by an iterative algorithm by pushing the parameters that would normally be passed to the recursive function onto a stack.  
In fact, you are replacing the program stack by one of your own.  



### Python sequence types  
P 206  P 214 P 224
- list: dynamic array, allows to add elements to the list, with no apparent limit on the overall capacity of the list  
- tuple: immutable, more memory efficient than lists  
- str: an array of characters (not an array of references) -> compact array  
(based on low-level sequence -> array)  
P 208 - 209
- each cell of an array must use the __same number of bytes__  
- referential arrays: at the lowest level, what is stored is a consecutive sequence of __memory addresses__ at which the elements of the sequence reside  ->  although the relative size of the individual elements may vary, the number of bits used to store the memory address of each element is fixed  
-- disadvantage: inefficiencies  

### copy
P 210  
- shallow copy: new list, it references the same elements as in the first list
- deep copy: new list with new elements 
```
import copy
copy.copy()  # shallow copy  
copy.deepcopy()  # deep copy  
```

### compact array 
P 212  
-- advantages: computing performance; memory usage; stored consecutively in memory
```
import array  
# https://docs.python.org/3/library/array.html
# array_name = array(typecode, [Initializers])
# type code: allows the interpreter to determine precisely how many bits are needed per element of the array
primes = array.array('i', [2, 3, 5, 7, 11, 13, 17, 19])
```

### efficiency of string  
__strings are immutable__  
the series of concatenations take O(n^2) time  
```
letters += c  # do not use this
```

### stacks  
P 251  
- a collection of objects  
- LIFO: last in first out  
- user may insert objects into a stack at any time, but only access the most recently inserted object that remains  
- fundamental operations: push & pop  

### queues
P 261
- a collection of objects
- FIFO: first in first out
- elements can be inserted at any time, but only the element that has been in the queue the longest can be next removed
- fundamental operations: enqueue & dequeue

### double ended queues (deque)
P 269
- supports insertion and deletion at both the front and the back of the queue
- fundamental operations: add_first, add_last, delete_first & delete_last
```
# e.g.,
from collections import deque
# list-like container with fast appends and pops on either end
# https://docs.python.org/3/library/collections.html#collections.deque
d = deque('a')
d.append('b')
d.appendleft('c')
d.extend('de')  # extend the left side
```