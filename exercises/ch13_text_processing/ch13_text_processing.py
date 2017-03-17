"""
chapter 13: Text Processing
"""

# P 605
# pattern-matching problem: find P in T  
# brute force 
# worst-case running time of the brute-force method: O(m*n)
def find_brute(T, P):
    """
    return the lowest index of T at which substring P begins (or else -1)
    """
    n, m = len(T), len(P)  # introduce convenient notations 
    # try every potential starting index within T
    for i in range(n-m+1):  # worst case: O(n-m+1)
        k = 0  # an index into pattern P
        # k-th character of P matches
        while k < m and T[i+k] == P[k]:  # worst cast: O(m) 
            k += 1  # an index into pattern P 
        if k == m:  # if we reached the end of pattern 
            return i  # substring T[i:i+m] matches P 
    return -1  # failed to find a match starting with any i
    
t = 'fjalfjeorj'
p = 'alf'
r = find_brute(t, p)
print(r)


# p 608 
# Boyer-Moore algorithm O(m*n) 
# avoid comparisons between P and a sizable fraction of the characters in T
# improve the running time of the brute-force algorithm by adding two potential time-saving heuristics 
#   - looking-glass heuristic: when testing a possible placement of P against T, begin the comparisons from the end of P and move backward to the front of P  
#   - character-jump heuristic: During the testing of a possible placement of P within T, a mismatch of text character T[i]=c with the corresponding pattern character P[k] is handled as follows. If c is not contained anywhere in P, then shift P completely past T[i] (for it cannot match any character in P). Otherwise, shift P until an occurrence of character c in P gets aligned with T[i] 
def find_boyer_moore(T, P):
    """
    return the lowest index of T at which substring P begins (or else -1)
    """
    n, m = len(T), len(P)  # introduce convenient notations 
    if m == 0:  # trivial search for empty string 
        return 0
    last = {}  # build 'last' dictionary: {'c' in P: index in P} 
    for k in range(m):
        last[P[k]] = k  # later occurrence overwrites 
    # align end of pattern at index m-1 of text 
    i = m - 1  # an index into T
    k = m - 1  # an index into P 
    while i < n:
        if T[i] == P[k]:  # a matching character
            if k == 0:
                return i  # pattern begins at index i of text 
            else:
                i -= 1  # examine previous character of both T and P 
                k -= 1
        else:  # mismatch
            j = last.get(T[i], -1)  # find the index of T[i] in P, -1 if not found
            i += m - min(k, j+1)  # case analysis for jump step , i index of T
            k = m - 1  # restart at end of pattern, k index of P 
    return -1  # not found  
    
t = 'fjalfjeorj'
p = 'alf'
r = find_boyer_moore(t, p)
print(r)


# P 612 - P 613
# Knuth-Morris-Pratt Algorithm: O(n+m)
# pre-compute (failure function) self-overlaps between portions of the pattern so that when a mismatch occurs at one location, we immediately know the maximum amount to shift the pattern before continuing the search
# failure function: 
#   - indicate the proper shift of P on a failed comparison; 
#   - defined as the length of the longest prefix of P that is suffix of P[1:k+1] 
#   - how many of the immediately preceding characters can be reused to restart the pattern 

# O(m)
def compute_kmp_fail(P):
    """
    utility that computes and returns KMP fail list
    failure function guarantees that all the ignored comparisons are redundant—they would involve comparing the same matching characters over again
    """
    m = len(P)
    fail = [0] * m  # by default, presume overlap of 0 everywhere
    j = 1  # j loop through P 
    k = 0  # k always at the beginning of P, indicating how many overlaps 
    while j < m:  # compute f(j) during this pass, if non-zero
        if P[j] == P[k]:  # k + 1 characters match thus far 
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:  # k follows a matching prefix 
            k = fail[k-1]
        else:
            j += 1
    return fail 

p = 'amalgamation'    
f = compute_kmp_fail(p)
print(list(p))
print(f)        


# worst-case O(2*n) 
def find_kmp(T, P):
    """
    return the lowest index of T at which substring P begins (or else -1)
    """
    n, m = len(T), len(P)  # introduce convenient notations 
    if m == 0:  # trivial search for empty string
        return 0
    fail = compute_kmp_fail(P)  # rely on utility to pre-compute 
    j = 0  # index into text 
    k = 0  # index into pattern 
    while j < n:
        if T[j] == P[k]:  # P[0:1+k] matched thus far
            if k == m - 1: 
                return j -m + 1  # match is complete 
            j += 1  # try to extend match 
            k += 1
        elif k > 0:
            k = fail[k-1]  # reuse suffix of P[0:k]
        else:
            j += 1
    return -1  # reached end without match 
    
t = 'xxamalgamationxxx'
print(find_kmp(t, p))      



# P 616
# matrix chain-product 
# determine the parenthesization of the expression defining the product A that minimizes the total number of scalar multiplications performed  
# dynamic programming algorithm for the matrix chain-product problem 
def matrix_chain(d):
    """
    O(n**3)
    :para d: a list of n+1 numbers such that size of k-th matrix is d[k]*d[k+1]
    :return: n-by-n table such that N[i][j] represents the minimum number of multiplications needed to compute the product of Ai through Aj inclusive   
    """
    n = len(d) - 1  # number of matrices 
    N = [[0] * n for i in range(n)]  # initialize n-by-n result to 0
    for b in range(1, n):
        for i in range(n-b):
            j = i + b
            N[i][j] = min(N[i][k] + N[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j))
    return N 

# test 
# matrix chain: (2,5)(5,3)(3,8)(8,4) --> (2,4)
# d: a list of n+1 numbers such that size of k-th matrix is d[k]*d[k+1]
d = [2, 5, 3, 8, 4] 
N = matrix_chain(d)
for n in N:
    print(n)
'''
[0, 30, 78, 142]
[0, 0, 120, 156]
[0, 0, 0, 96]
[0, 0, 0, 0]
'''



# P 620    
# longest common subsequence 
# given X and Y, find a longest string S that is a subsequence of both X and Y  
# dynamic programming algorithm for the LCS problem
# O(n*m)
def LCS(X, Y):
    """
    return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]
    """
    n, m = len(X), len(Y)  # introduce convenient notations 
    L = [[0] * (m+1) for k in range(n+1)]  # n+1 (X) rows; m+1 (Y) columns 
    for j in range(n):  # for X
        for k in range(m):  # for Y 
            if X[j] == Y[k]:  # align this match 
                L[j+1][k+1] = L[j][k] + 1
            else:  # choose to ignore one character
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L             

x = 'GTTCC'  # n = 5
y = 'ATTC'  # m = 4
l = LCS(x, y)
print()
for ll in l:
    print(ll)
    
'''
L: (n+1)*(m+1) --> (5+1)*(4+1)
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 1, 1, 1]
[0, 0, 1, 2, 2]
[0, 0, 1, 2, 3]
[0, 0, 1, 2, 3]
'''


def LCS_solution(X, Y, L):
    """
    return the longest common substring of X and Y, given LCS table L 
    """
    solution = []
    j, k = len(X), len(Y)
    while L[j][k] > 0:  # common characters remain 
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))  # return left-to-right version 

print(LCS_solution(x, y, l))


# P 623 
# text compression & greedy method 
# reduce the space usage by allowing common groups of characters (e.g., those from the ASCII, with fewer bits)
# Huffman code: uses a variable-length encoding specifically optimized for a given string X over any alphabet 
# saves space over a fixed-length encoding by using short code-word strings to encode high-frequency characters and long code-word strings to encode low-frequency characters
# Huffman coding: takes two binary trees with the smallest frequencies and merges them into a single binary tree; repeats the process until only one tree is left
# constructs an optimal prefix code for a string of length n with d distinct characters in O(n+d*log(d)) time.    