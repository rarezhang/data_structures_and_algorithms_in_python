# Data Structures and Algorithms in Python  

https://www.amazon.com/Structures-Algorithms-Python-Michael-Goodrich/dp/1118290275  

#### My solutions to exercises in ```Data Structures and Algorithms in Python```   
[click here](https://github.com/rarezhang/data_structures_and_algorithms_in_python/tree/master/exercises)  


# Reading notes  

### sort VS sorted  
P 559  
- sort: list class -> rearrange the contents of list  
- sorted fun; produces a new list containing the elements of an arbitrary collection in sorted order  

### Python special attribute: __slots__
- allows you to explicitly state in your code which attributes you expect your object instance to have, with the expected results:
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
3. __parameterization__: public use -> cleaner interface; nonpublic function -> having the desired recursive parameters

### why recursion  
P 200  
advantage:  
1. avoid complex case analyses and nested loops  
2. more readable algorithm descriptions  
disadvantage:  
1. keep track of nested call (memory issue)  
2. stack data structure: convert a recursive algorithm into a non-recursive algorithm (memory: storing only minimal information)  

### tail recursion  == linear recursion  
P 200  
- any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing recursion  
- any tail recursion can be reimplemented non-recursively by enclosing the body in a loop for repetition, and replacing a recursive call with new parameters by a reassignment of the existing parameters to those values  

### recursion tips
replace a recursive algorithm by an iterative algorithm by pushing the parameters that would normally be passed to the recursive function onto a stack.  
In fact, you are replacing the program stack by one of your own.  


### recursion design pattern: divide-and-conquer  
- divide: If the input size is smaller than a certain threshold (say, one or two elements), solve the problem directly using a straightforward method and return the solution so obtained. Otherwise, divide the input data into two or more disjoint subsets  
- conquer: Recursively solve the subproblems associated with the subsets  
- combine: Take the solutions to the subproblems and merge them into a solution to the original problem  


### in-place  
P 581  
- an algorithm is __in-place__ if it uses only a small amount of memory in addition to that needed for the original input.  

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
- keep elements in a certain order; a node is allocated for each element  
- node(element, neighboring nodes)  
- advantage  (avoid disadvantage of array)  
    * The length of a dynamic array might be longer than the actual number of elements that it stores  
    * Amortized bounds for operations may be unacceptable in real-time systems  
    * Insertions and deletions at interior positions of an array are expensive  
- disadvantage  
    * elements of a linked list cannot be efficiently accessed by a numeric index k  
    
    
### link-based v.s. array-based sequences  
P 314  
- advantages of array-based sequence  
    * O(1) time access to an element based on an integer index  
    * operations with equivalent asymptotic bounds typically run a constant factor more efficiently with an array-based structure versus a linked   
    * array-based representations typically use proportionally less memory than linked structures  
- advantages of link-based sequence  
    * provide worst-case time bounds for operations  
    * support O(1) time insertions and deletions at arbitrary positions (most significant advantage)  
- disadvantages of array-based sequence  
    * insert or pop with index k uses O(n-k+1)  
- disadvantages of link-based sequence  
    * locating the k-th element requires O(k) time traverse the list from the beginning <or O(n-k) if traversing backward from the end of a doubly linked list  
    * with linked lists, memory must be devoted not only to store a reference to each contained object, but also explicit references that link the nodes  
    
    
### singly linked lists  
P 279  P 280
- a collection of nodes that collectively from a linear sequence  
- no predetermined fixed size  
- node(element, next)  
- must keep a reference to the ```head``` of the list  
- traversing (link hopping / pointer hopping): starting at the head and moving from one node to another by following each node's next reference  


### circularly linked lists
P 288  
- have the tail of the list use its next reference to point back to the head of the list  
- has no beginning or end; must maintain a current node  


### doubly linked list
P 292  
- each node keeps an explicit reference to the node before it and a reference to the node after it  
- allow a greater variety of O(1) time update operations (including insertions and deletions at arbitrary positions within the list)  
- dummy nodes (sentinels): header node; trailer node  
    * advantage of using sentinels:  
       eliminate the special case  
       simplifies the logic of operations  
       the header and trailer nodes never change  
       treat all insertions in a unified manner  
    
    
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
    * maximum value of f(p): fm
    * required array length: N = 1 + fm
    * worst case: N = 2^n - 1
- advantage:  
    * a position p can be represented by the single integer f(p)  
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
- breadth-first traversal: visit all the positions at depth d before visit the positions at depth d+1  
- inorder traversal (for binary tree): visit a position between the recursive traversals of its left and right subtrees (for every position p, visit p after all the position in the left subtree; before all the positions in the right subtree)  
    * binary search tree (application of the inorder traversal)
        + running time: proportional to the height (most efficient when they have small height)  
        + position p stores an element e(p)  
        + elements stored in the left subtree of p are less than e(p)  
        + elements stored in the right subtree of p are greater than e(p)  
- euler tour traversal: walk around T  
    * start by going from the root toward its leftmost child, viewing the edges of T as being walks that we always keep to our left  
    * O(n): progresses exactly two times along each of the n-1 edges of the tree  
    * pre visit: when first reaching the position, that is, when the walk passes immediately left of the node in our visualization  
    * post visit: when the walk later proceeds upward from that position, that is, when the walk passes to the right of the node  
    
### binary tree review  
T: a nonempty binary tree  
n: number of nodes  
nE: number of external nodes  
nI: number of internal nodes  
h: height of T  
T has following properties  
1. h + 1 ≤ n ≤ 2^(h + 1) − 1  
2. 1 ≤ nE ≤ 2^h  
3. h ≤ nI ≤ 2^h − 1  
4. log(n+1)− 1 ≤ h ≤ n − 1  
Also,if T is proper,then T has the following properties:  
1. 2h + 1 ≤ n ≤ 2^(h+1) − 1  
2. h + 1 ≤ nE ≤ 2^h  
3. h ≤ nI ≤ 2^h − 1  
4. log(n+1)− 1 ≤ h ≤ ( n − 1 )/ 2  
  
Question 1. What is the maximum height of a binary tree with n nodes?  
Answer:  n-1  
  
Question 2. What is the minimum height of a binary tree with n nodes?  
Answer:  floor(log2(n))  
  
Question 3.  Consider a tree in which each node contains a maximum of 4 children (a quad tree). What is the minimum height of a quad tree that contains 21 nodes, what is the maximum height of a quad tree that contains 21 nodes?  
Answer:  The max number of nodes in level k is 4^k. Therefore we will have 1 + 4 + 16 + 64 + … total nodes in a tree.  So the min height is 2 and max height is 20  
  
Question 4. What is the maximum number of external nodes (or leaves) for a binary tree with height H?  
Answer:  2^H  
  
Question 5. What is the maximum number of internal nodes (or leaves) for a binary tree with height H?  
Answer:  2^H - 1  
  
Question 6. Discuss advantages of using hash tables versus binary search trees  
Answer:  hash tables are great for applications that require quick search and updates, but do not require any order information. A “balanced” BST can maintains fairly quick search capability (log n) and order information  
  
Question 7. Assuming each node in a BST takes 20 bytes of storage, how much memory is necessary to store a “perfect” binary tree of height 3? What is the amount of memory necessary if the tree is a “Full” tree of height 3 with minimal number of nodes?  
Answer:  A perfect binary tree of height 3 has 23+1 – 1 = 15 nodes. Therefore it requires 300 bytes to store the tree. If the tree is full of height 3 and minimum number of nodes, the tree will have 7 nodes. So we need 140 bytes to store the tree.  

     
### priority queue
P 385 P 386   
- a collection of prioritized elements that allows:  
    * arbitrary element insertion  
    * the removal of the element that has first priority  
- key  
    * model an element and its priority as a key-value pair  
    * when an element is added to a priority queue, user designates its priority by providing an associated key  
    * element with the __minimum__ key will be the next to be removed from the queue (element with key 1 will be given priority over an element with key 2)  
    
    
### binary heap
P 392  
- a binary tree T: stores a collection of items at its positions and that satisfies:
    * a relational property defined in terms of the way keys are stored in T  
        + __heap order property__ : in a heap T, for every position p other than the root, the key sorted at p is greater than or equal to the key stored at p's parent  
        + minimum key is stored at the root of T  
        + keys on a path from the root to a leaft are in nondecreasing order  
    * a structural property defined in terms of the shape of T  
        + __complete binary tree property__ : leaf i has 2^i (0 ≤ i ≤ h−1) nodes; remaining nodes at level h reside in the left most possible positions  
        + have as small a height as possible  
- height of a heap  
    * h: the height of T  
    * a heap T storing n entries has height `h = floor[log(n)]`  
    * implies: update operations on a heap ~ the height of T ~ O(log(n))  
- use the structure of a binary tree to find a compromise between elements being entirely unsorted and perfectly sorted  
- can perform both insertions and removals on __priority queue__ in logarithmic time  


### maps: associative arrays  
P 424  
- a search for a key and its associated value can be performed efficiently  
- keys: unique  
- values: not necessarily unique  

### hash tables  
P 432  P 433  P 438  
- supports the abstraction of using __keys as indices__ with a syntax: M[k]  
- hash function: 
    * goal: map each key k to an integer in the range [0, N-1], N is the capacity of the bucket array A for a hash table  
    * use the hash function value `h(k)` as an index into our bucket array  
    * item (k,v) store in the bucket A[h(k)]  
    * bucket array: 
        + ideally: keys will be distributed in the range from 0 to N-1 by a hash function  
        + practically: may be two or more distinct keys get mapped to the same index  
    * collision: two different items be mapped to the same bucket in A -> avoid  
    * collision-handling:  
        + separate chaining: have each bucket A[j] store its own secondary container  
        + open addressing: linear probing; quadratic probing  
        + double hashing: choose a secondary hash function  
    * hash function = hash code + compression function  
        + hash code for key: independent of a specific hash table size (can be used for a hash table of any size)； need not be in the range [0, N-1]  
        + polynomial hash code: Xn-1 + a ( Xn−2 + a ( Xn−3 + ···+ a ( X2 + a ( X1 + a X0 ))···)); choice of a for English words: 33,37,39 and 41  
        + cyclic-shift hash code: take the leftmost x bits and placing those on the rightmost side of the representation; bitwise operators << and >>  
        + python: hash() -> return the hash value(integers) of the object; only immutable data type  
        + compression function: mapping the hash code into the range [0, N-1]; minimize the number of collisions for a given set of distinct hash codes  
        + division method: maps an integer i to (i mod N); N: prime->not engouth  
        + MAD method (Multiply-Add-and-Divide): maps an integer i to [(ai+b) mod p] mod N  
        
        
### skip list  
P 459  
- provide a clever compromise to efficiently support search and update operations  
    * skip list for a map: a series of lists {S0, S1, ... Sh}  
    * Si: a subset of the items of M (sorted by increasing keys)  
    * Si contains a randomly generated subset of the items in list Si-1; Si has n/2^i items  
    * two sentinel keys: −∞ and +∞  
    * h: the height of skip list S = log(n)  
- two dimensional collection of positions arranged horizontally into __levels__ and vertically into __towers__  
    * level: Si  
    * tower: contains positions storing the same item across consecutive lists  
- a collection of __h__ doubly linked lists aligned at towers, which are also doubly linked lists  
- search and update: O(log(n)) on average  

    
        
### set & multi-set (bag) & multi-map 
* set  
    - unordered collection of elements with duplicates  
    - supports efficient membership tests  
    - like keys of a map without any auxiliary values  
    - any data structure used to implement a map can be modified to implement the set with similar performance guarantees  
* multi-set (bag)  
    - a set like container that allows duplicates  
* multi-map  
    - associates values with keys  
    - same key can be mapped to multiple values  


### binary search tree  
P 482 P 483  
- a binary tree T: with each position p storing a key-value pair (k,v):
    * keys stored in the left subtree of p are less than k  
    * keys stored in the right subtree of p are greater than k  
- inorder traversal: visits positions in increasing order of their keys  
- binary search tree is an efficient implementation of a map with n entries only if its height is small    

   
### balanced search trees
P 497  
- rotation: operation to re-balance a binary search tree (maintain the binary search tree property)  
    * rotate a child to be above its parent  
    * transform the left formation into the right; or the right formation into the left  
- tri-node restructuring  
    * consider a position x; its parent y; and grandparent z  
    * restructure the subtree rooted at z in order to reduce the overall path length to x and its subtree  
        + 1: Let (a, b, c) be a left-to-right (inorder) listing of the positions x, y, and z, and let (T1 ,T2 ,T3 ,T4) be a left-to-right (inorder) listing of the four subtrees of x, y, and z not rooted at x, y, or z.  
        + 2: Replace the subtree rooted at z with a new subtree rooted at b.  
        + 3: Let a be the left child of b and let T1 and T2 be the left and right subtrees of a, respectively.  
        + 4: Let c be the right child of b and let T3 and T4 be the left and right subtrees of c, respectively.  
    
    
### AVL trees
P 503  P 505  
- balancing strategy: guarantee worst-case logarithmic running time for all fundamental map operations  
- height balance property:  for every position p of T, the heights of the children of p differ by at most 1  
- any binary search tree that satisfies the __height balance property__ is an AVL tree  
- a subtree of an AVL tree is itself an AVL tree  
- the height of an AVL tree soring n entries is `log(n)`  
- a position is __balanced__ if the absolute value of the difference between the heights of its children is at most 1  
- AVL tree == every position is balanced  


### splay trees 
P 512  
- splaying: a move-to-root operation 
    * guarantee the efficiency of splay trees  
    * more frequently accessed elements to remain to the root  

    
### (2,4) trees
P 524  
- multi-way search tree: internal nodes may have more than two children  
    * has at least two children  
    * stores a collection of items of the form (k, x), where k is a key and x is an element  
    * contains d-1 items, where d is the number of children  
    * contains 2 pseudo-items: k0=−∞, kd=∞  
    * Children of each internal node are “between” items  
        + all keys in the subtree rooted at the child fall between keys of those items  
    * external nodes are just placeholders  
    
    
### red-black trees
P 534  
- a binary search tree: with nodes colored read and black  
- use O(1) structural changes after an update in order to stay balanced  
    * root property: root is black  
    * red property: the children of a red node are black  
    * depth property: all nodes with zero or one children have the same black depth (defines as the number of black ancestors)  
- can construct a corresponding (2,4) tree by merging every red node into its parent  


### sorting algorithms  
[read the summary here](https://github.com/rarezhang/sorting_algorithms)
- insertion sort: an excellent algorithm for sorting small sequences; quite effective for sorting sequences that are already almost sorted     
- selection sort  
- bubble sort  
- heap sort: in place; natural choice on small and medium sized sequences; not stable      
- merge sort: not in place; excellent algorithm for situations where the input is stratified across various levels of the computer’s memory hierarchy
    + Tim-sort: bottom-up merge sort (takes advantage of some initial runs in the data while using insertion-sort to build additional runs): python/Java(7)  
- quick sort: in place; C/Java(6) sorting algorithm  
- bucket sort: excellent choice for sorting entries with small integer keys   
- radix sort: excellent choice for sorting entries with small integer keys  

P 584  
- comparison-based sorting has an O(n*logn) worst-case lower bound  
- can represent a comparison-based sorting algorithm with a decision tree  
- the running time of a comparison-based sorting algorithm must be greater than or equal to the height of the decision tree  

### stable sorting  
P 587  
- a sorting algorithm is stable if, for any two entries ( ki , vi ) and ( kj , vj ) of S such that ki = kj
and ( ki , vi ) precedes ( kj , vj ) in S before sorting (that is, i < j), entry ( ki , vi ) also
precedes entry ( kj , vj ) after sorting  
- stability is important for a sorting algorithm
because applications may want to preserve the initial order of elements with the same key  


### python's built-in sorting function
- ```list.sort()```: in-place  
- ```sorted(any iterable object)```: produce a new ordered object  
- sorting according to a key function:  
    + decorate-sort-undecorate design pattern  
        * each element of the list is temporarily replaced with a "decorated" version that includes the result of the key function applied to the element  
        * list is sorted based upon the natural order of the keys  
        * decorated elements are replaced by the original elements  
    + key function: one-parameter function (accepts an element as a parameter and returns a key)  
        * e.g., len() -->  
        ```
        alist = ['yellow', 'blue', 'cyan', 'green', 'red']
        alist.sort(key=len)
        # ['red', 'blue', 'cyan', 'green', 'yellow']
        ```
    + reverse keyword parameter: can be set to True to cause the sort order to be from largest to smallest  
        * reverse=True -->  
        ```
        alist = ['red', 'blue', 'cyan', 'green', 'yellow']
        alist.sort(key=len, reverse=True)
        # ['yellow', 'green', 'blue', 'cyan', 'red']
        ```

# brute force  
P 604 P 606
- when we have something we wish to search for or when we wish to optimize
some function  
- enumerate all possible configurations of the inputs involved and pick the best of all
these enumerated configurations  
     
        
### dynamic programming  
P 604 P 616  
- can be applied in certain settings to solve a problem in polynomial time that appears at first to require exponential time to solve  
- can be used to take problems that seem to require exponential time and produce polynomial-time algorithms to solve them  
- used for optimization problems:  
- components of a dynamic programming solution:  
    + Simple Subproblems: There has to be some way of repeatedly breaking the global optimization problem into subproblems. Moreover, there should be a way to parameterize subproblems with just a few indices, like i, j, k, and so on  
    + Subproblem Optimization: An optimal solution to the global problem must be a composition of optimal subproblem solutions  
    + Subproblem Overlap: Optimal solutions to unrelated subproblems can contain subproblems in common  

    
### greedy method  
P 604 p 623  
- allows us to approximate solutions to hard problems, gives rise to optimal algorithms  
- applied to optimization problems, where we are trying to construct some structure while minimizing or maximizing some property of that structure  


### trie:  
(comes from the word re```trie```val)  
P 621 P 630  
- tree-based data structure for storing strings in order to support fast pattern matching  
- standard trie T for S:  
    + each node of T, except the root, is labeled with a character of Σ  
    + the children of an internal node of T have distinct labels  
    + T has s leaves, each associated with a string of S, such that the concatenation of the labels of the nodes on the path from the root to a leaf v of T yields the string of S associated with v  
    + an internal node in a standard trie T can have anywhere between 1 and |Σ| children  
    + perform a search in T for a string X: tracing down from the root the path indicated by the characters in X  
- compressed trie (Patricia trie)  
    + ensures each internal node in the trie has at least two children  
    + compressing chains of single-child nodes into individual edges  
    + an internal node v of T is redundant if v has one child and is not the root  
    + nodes in a compressed trie are labeled with strings  
    + searching in a compressed trie is not necessarily faster than in a standard tree  
- suffix trie (suffix tree | position tree)  
    + save space over a standard trie by using several space compression techniques: uses O(n) space  
    + can construct the suffix trie for a string of length n with an incremental algorithm: O(|Σ|*(n^2))  
    
    
### graphs  
P 642  
- a way of representing relationships that exist between pairs of objects  
    + a set of objects (vertex | nodes)  
    + a collection of pairwise connections between objects (edges | arcs)  
- directed | undirected edge  
    + directed: edge (u,v) is said to be **directed** from u to v if the pair (u,v) is ordered, with u preceding v  
    + undirected: edge (u,v) is said to be undirected if the pair (u,v) is not ordered  
- directed | undirected graph  
    + directed: all the edges in a graph are directed  
    + undirected: all the edges in a graph are undirected  
- adjacent: (u,v) are adjacent if there is an edge whose end vertices are u and v  
- self-loop: if two endpoints coincide  
- simple graph: no parallel edges or self-loop  
- path: a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each edge is incident to its predecessor and successor
vertex  
- cycle: path that starts and ends at the same vertex, and that includes at least one edge  
- an undirected graph with n vertices and m edges:  
    + if graph is connected, then m ≥ n − 1  
    + if graph is a tree, then m = n − 1  
    + if graph is a forest, then m ≤ n − 1  
    

    
### data structures for graphs 
- edge list:  
    + simplest; not the most efficient   
    + e.g., 
        * (u)-e-(v); (u)-g-(w); (v)-f-(w); (w)-h-(z)  
        * V: [u, v, w, z]  
        * E: [e, f, g, h]  
- adjacency list  
    + group the edges of a graph by storing them in smaller, secondary containers that are associated with each individual vertex  
    + e.g., 
        * (u) --> e, g  
        * (v) --> e, f  
        * (w) --> g, g, h  
        * (z) --> h  
- adjacency map  
    + let the opposite endpoint of each incident edge serve as a key in the map, with the edge structure serving as the value  
    + e.g., 
        * (u) --> (v)->e, (w)->g  
        * (v) --> (u)->e, (w)->f  
        * (w) --> (u)->g, (v)->f, (z)->h  
        * (z) --> (w)->h  
- adjacency matrix  
    + e.g., 
        *             0 1 2 3  
        * (u) --> 0 |   e g  |  
        * (v) --> 1 | e   f  |  
        * (w) --> 2 | g f   h|  
        * (z) --> 3 |     h  |  

| Operation | Edge List | Adj. List | Adj. Map | Adj. Matrix|
|----------|----------|----------|---------|-----------|
| vertex_count() | O(1) | O(1) | O(1) | O(1) |
| edge_count() | O(1) | O(1) | O(1) | O(1) |
| vertices() | O(n) | O(n) | O(n) | O(n) |
| edges() | O(m) | O(m) | O(m) | O(m) |
| get_edge(u,v) | O(m) | O(min(dv,du)) | O(1) exp. | O(1) |
| degree(v) | O(m) | O(1) | O(1) | O(n) |
| incident_edges(v) | O(m) | O(dv) | O(dv) | O(n) |
| insert_vertex(x) | O(1) | O(1) | O(1) | O(1) | O(n^2) |
| remove_vertex(v) | O(m) | O(dv) | O(dv) | O(n^2) |
| insert_edge(u,v,x) | O(1) | O(1) | O(1) exp. | O(1) |
| remove_edge(e) | O(1) | O(1) | O(1) exp. | O(1) |  


### graph traversals 
P 660  
- a systematic procedure for exploring a graph by examining all of its vertices and edges  
- a traversal is efficient if it visits all the vertices and edges in time proportional to their number --> in linear time  
    * reachability: determine how to travel from one vertex to another  
    * undirected:      
        + testing whether G is connected  
        + computing a spanning tree of G, if G is connected  
        + computing the connected components of G  
        + computing a cycle in G, or reporting that G has no cycles  
    * directed:  
        + Computing a directed path from vertex u to vertex v, or reporting that no such path exists  
        + finding all the vertices of G that are reachable from a given vertex s  
        + determine whether G is acyclic  
        + determine whether G is strongly connected  

# directed acyclic graphs & topological ordering  
P 677  
- direct graphs without directed cycles  
- topological ordering of G is an ordering v1 ,..., vn of the vertices of G such that for every edge (vi, vj) of G, it is the case that i < j  
- G has a topological ordering if and only if it is acyclic  
- topological sorting: computing a topological ordering of a directed graph  


# weighted graphs 
P 681  
- weighted graphs: a graph that has a numeric label associated with each edge --> the weight of edge  
- length of a path: the sum of the weights of the edges  
- distance from a vertex *u* to a vertex *v* in G --> d(u, v), is the length of a
minimum-length path (shortest path) from u to v, if such a path exists ( d(u, v) = ∞ if there is no path)  


# shortest path tree  
P 691  
- all shortest paths form a rooted tree  