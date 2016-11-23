# Data Structures and Algorithms in Python  

https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275  

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


### Python sequence types  
P 206  
- list; tuple; str  
(based on low-level sequence -> array)  
P 208 - 209
- each cell of an array must use the __same number of bytes__  
- referential arrays: at the lowest level, what is stored is a consecutive sequence of __memory addresses__ at which the elements of the sequence reside  ->  although the relative size of the individual elements may vary, the number of bits used to store the memory address of each element is fixed  

### copy
- shallow copy: new list, it references the same elements as in the first list
- deep copy: new list with new elements 
```
import copy
copy.copy()  # shallow copy  
copy.deepcopy()  # deep copy  
```


