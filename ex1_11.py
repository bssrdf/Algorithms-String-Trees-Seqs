'''
Let T be a text string of length m and let S be a multiset of n characters. 
The problem is to find all substrings in T of length n that are formed by the 
characters of S. For example, let S = {a, a, b, c} and T = 'abahgcabah'. Then 
'caba' is a substring of T formed from the characters of S.
Give a solution to this problem that runs in O(m) time. The method should 
also be able to state, for each position i, the length of the longest substring 
in T starting at i that can be formed from S.

'''


from collections import Counter


def findAllSubstringsLengthNBF(T, S):
    n, m = len(S), len(T)
    s = Counter(S)
    ans = []
    for i in range(m-n):
        s1 = Counter(T[i:i+n])
        if s1 == s:
            ans.append(T[i:i+n])
    return ans


def findAllSubstringsLengthN(T, S):
    # use a sliding window of size n
    # keep track of the characters in the window
    cnt, req = Counter(), Counter(S)
    m, n = len(T), len(S)    
    # ans, needed = [], [True]*26
    ans, needed = [], {}
    for c in req:
        # needed[ord(c)-ord('a')] = False
        needed[c] = False
    for i in range(m):        
        if T[i] in req:
            cnt[T[i]] += 1
            if cnt[T[i]] >= req[T[i]]:                
                # needed[ord(T[i])-ord('a')] = True # if the required number of T[i] is reached, 
                needed[T[i]] = True # if the required number of T[i] is reached, 
                            # mark needed by 1
        if i >= n-1: 
            j = i-n+1            
            # if all(needed): # all required are in the window, got one candidate
            if all(needed.values()): # all required are in the window, got one candidate
               ans.append(T[j:i+1])
            if T[j] in req:
                cnt[T[j]] -= 1
                if cnt[T[j]] < req[T[j]]: # if the supply of T[j] is not enough
                    # needed[ord(T[j])-ord('a')] = False  # mark needed 
                    needed[T[j]] = False  # mark needed 
    return ans         
            
import random
import string

from timeit import default_timer as timer
from datetime import timedelta

if __name__ == "__main__":
    a = 'abahgcabah'
    b =  ['a', 'a', 'b', 'c']
    print(findAllSubstringsLengthN(a,b))
    a = 'abahgcabah'
    b =  ['a', 'b']
    print(findAllSubstringsLengthN(a,b))
    a = 'abahgcahab'
    b =  ['a', 'b', 'h']
    print(findAllSubstringsLengthN(a,b))
    m = 100000
    x = []
    while len(x) < m:
        a = list(string.ascii_lowercase)
        x += a
    for _ in range(10):
        random.shuffle(x)
    x = ''.join(x)
    b = ['a', 'b', 'a', 'c', 'd', 'f']
    # print(x)
    start = timer()
    # print(findAllSubstringsLengthNBF(x,b))
    end = timer()
    print(timedelta(seconds=end-start))
    start = timer()
    # print(findAllSubstringsLengthN(x,b))
    end = timer()
    print(timedelta(seconds=end-start))
    with open('actg3.data') as f:
        x = '' 
        for line in f.readlines():
           x += line.strip()   
    print(len(x))
    # b = ['a']*50 + ['c']*50 + ['t']*40 + ['g']*70
    b = ['a']*252 + ['c']*262 + ['t']*252 + ['g']*234
    #b = ['a']*2 + ['c']*3 + ['t']*3 + ['g']*5
    # print('XXX', Counter(x[600000:601000]))
    start = timer()
    # sol1 = findAllSubstringsLengthNBF(x,b)    
    end = timer()
    print(timedelta(seconds=end-start))
    
    start = timer()
    sol2 = findAllSubstringsLengthN(x,b)    
    end = timer()    
    print(timedelta(seconds=end-start))

    # print(len(sol2), len(sol1)) 
    # print(sol1, sol2)
    # print(Counter(sol1[0]))
    # for s1, s2 in zip(sol1, sol2):
    #     if s1 != s2:
    #         print(s1, s2)
    x = 'tataacaaccctgattacatcaagctacgctccggtgcgttgcctcggacgagt'
    s = ['a', 'a', 'c', 'g', 't', 'g']
    s = ['c', 't', 't', 'g', 'g', 'g']
    print(findAllSubstringsLengthN(x,s))    
    

    
     