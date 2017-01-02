# Data Structures and Algorithms in Python  

https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275  

#### My solutions to exercises in ```Data Structures and Algorithms in Python```   
[click here](https://github.com/rarezhang/data_structures_and_algorithms_in_python/tree/master/exercises)  


# Reading notes  

### Python special attribute: __slots__
- allows you to explicityly state in your code which attributes you expect your object instance to have, with the expected results:
    * __faster__ attribute access  
    * potential __space savings__ in memory  
- read more: http://stackoverflow.com/questions/472000/usage-of-slots  


### template method pattern  
P 364  
- describe a generic computation mechanism that can be specialized for a particular application by redefining certain steps  


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
- disadvantage: inefficiencies  


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

### linked list
P 278  
- an alternative to array based sequence  
- keep elements in a certain order; a node is allocated for each elment  
- node(element, neighboring nodes)  
- advantage  (avoid disadvatage of array)  
    * The length of a dynamic array might be longer than the actual number of elements that it stores  
    * Amortized bounds for operations may be unacceptable in real-time systems  
    * Insertions and deletions at interior positions of an array are expensive  
- disadvantage  
    * elements of a linked list cannot be efﬁciently accessed by a numeric index k  
    
    
### link-based v.s. array-based sequences  
P 314  
- advantages of array-based sequence  
    * O(1) time access to an element based on an integer index  
    * operations with equivalent asymptotic bounds typically run a constant factor more efﬁciently with an array-based structure versus a linked   
    * array-based representations typically use proportionally less memory than linked structures  
- advantages of link-based sequence  
    * provide worst-case time bounds for operations  
    * support O(1) time insertions and deletions at arbitrary positions (most siginificant advantage)  
- disadvantages of array-based sequence  
    * insert or pop with index k uses O(n-k+1)  
- disadvantages of link-based sequence  
    * locating the kth element requires O(k) time traverse the list from the beginning <or O(n-k) if traversing backward from the end of a doubly linked list  
    * with linked lists, memory must be devoted not only to store a reference to each contained object, but also explicit references that link the nodes  
    
    
### singly linked lists  
P 279  P 280
- a collection of nodes that collectively from a linear sequence  
- no predetermined fixed size  
- node(element, next)  
- must keep a reference to the ```head``` of the list  
- traversing (link hopping / pointer hopping): starting at the head and moving from one node to another by follwing each nodes's next reference  


### circularly linked lists
P 288  
- have the tail of the list use its next reference to point back to the head of the list  
- has no beginning or end; must maintain a cufrrent node  


### doubly linked list
P 292  
- each node keeps an explicit reference to the node before it and a reference to the node after it  
- allow a greater variety of O(1) time update operations (including insertions and deletions at arbitrary positions within the list)  
- dummy nodes (sentinels): header node; trailer node  
    * advantage of using sentinels:  
       eliminate the special case  
       simplifies the logic of operations  
       the header and trailer nodes never change  
       treat all insretions in a unified manner  
    
    
### general trees
P 322  
- nonlinear data structures: much faster than using linear data structures  
    * relationship in a tree: hierarchical  
    * parent, child, ancestor, descendant  
    * top element: root  
    * each element (except top element):  
           + one parent  
           + zero or more children elements  
- provide nature organization for data  
- tree __T__ definition:  
    * a set of nodes  
    * nodes storing elements  
    * nodes have a parent-child relationship  
           + if __T__ is nonempty, it has root that has no parent  
           + each node __v__ of __T__ different from the root has a unique parent node __w__  
           + every node with parent __w__ is a child of __w__  
           + two nodes that are children of the same parent are siblings  
           + __v__ is external if __v__ has no children (known as leaves)  
           + __v__ is internal if it has one or more children  
           + node __u__ is an ancestor of a node __v__ if __u = v__ or __u__ is an ancestor of the parent of __v__  
           + node __v__ is a descendant of a node __u__ if __u__ is an ancestor of __v__  
    * edges and paths  
           + an edge of tree __T__ is a pair of nodes ( u , v ) such that __u__ is the parent of __v__, or vice versa  
           + a path of __T__ is a sequence of nodes such that any two consecutive nodes in the sequence form an edge  
    * ordered trees  
        there is a meaningful linear order among the children of each node  (e.g., arranging siblings left to right, according to their order)  
    * depth of a position (p): the number of ancestors of p, excluding p itself  
           + if p is root, depth = 0  
           + o.w. depth of p = 1 + depth of p's parent  
    * height of a position (p): 
           + if p is leaf, height = 0  
           + o.w. depth of p = 1 + max(heights of p's children)  
           + height(T) == height(root)  
           + height(T) == max(depth(leaf))
           
### recursive binary tree  
* either empty  
* or consists of  
    + a ndoe __r__ , the root of T, stores an element  
    + a binary tree, the left subtree of T  
    + a binary tree, the right subtree of T  


### binary trees  
- a binary tree is an ordered tree  
    * ever node has at most two children  
    * each child node is labeled as either left child or right child  
    * left child precedes a right child  
- left/right subtree: the subtree rooted at a left/right child of an internal node __v__  
- proper binary tree (full binary tree): each node has either zero or two children  
    * every internal node has exactly node has exactly two children  
- heights v.s. number of nodes  
    * maximum number of nodes grows exponentially  
    * depth d == level d  
    * level d has __at most__ 2^d nodes  
        + level 0: 2^0=1  
        + level 1: 2^1=2  
        + level 2: 2^2=4  
        + ......  


### linked structure for binary tree
- element | position | children | parent  
- `if` position==root `then` parent = None  
- `if` no child `then` left child / right child = None  


### linked structure for general tree  
P 349  
have each node store a single container of references to its children
    
    
### array based representations of binary tree
P 347  
- level numbering of the position in a binary tree: `f(p)`  
    * level numbering is based on potential position within the tree, not actural position of tree
    * `if` p is the root of T, `then` f(p) = 0   
    * `if` p is the left child of position q, `then` f(p)=2f(q)+1  
    * `if` p is the right child of position q, `then` f(p)=2f(q)+2  
- space usage: depends on the shape of the tree  
    * number of nodes: n
    * maxium value of f(p): fm
    * required array length: N = 1 + fm
    * worst case: N = 2^n - 1
- advantage:  
    * a position p can be reprensented by the single integer f(p)  
    * position based methods (root, parent, left, right) can be implemented using simple arithmetic operation on the number f(p)  
        + left child of p: 2f(p)+1  
        + right child of p: 2f(p)+2  
        + parent of p: floor[(f(p)−1)/2]  
- disadvantage:  
    * update operation are not efficient  
        + delete / promoting child: O(n)  
        

### tree traversal
P 350  P 352  P 354  
- a systematic way of accessing or visiting all the positions of T  
- preorder traversal: the root of T is visited first; the sub-trees rooted at its children are traversed recursively  
- postorder traversal: recursively traverses the subtrees rooted at the children of the root first; then visit the root  
- breadth-first travrsal: visit all the positions at depth d before visit the positions at depth d+1  
- inorder traversal (for binary tree): visit a position between the recursive traversals of its left and rigth subtrees (for every posiition p, visit p after all the position in the left subtree; before all the positions in the right subtree)  
    * binary search tree (application of the inorder traversal)
        + running time: proportional to the height (most efﬁcient when they have small height)  
        + position p stores an element e(p)  
        + elements stored in the left subtree of p are less than e(p)  
        + elements stored in the right subtree of p are greater than e(p)  
- euler tour traversal: walk around T  
    * start by going from the root toward its leftmost child, viewing the edges of T as being walks that we always keep to our left  
    * O(n): progresses exactly two times along each of the n-1 edges of the tree  
    * pre visit: when first reaching the position, that is, when the walk passes immediately left of the node in our visualization  
    * post visit: when the walk later proceeds upward from that position, that is, when the walk passes to the right of the node  
    
            
    
