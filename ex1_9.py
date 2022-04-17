'''

You are given two strings of n characters each and an additional parameter k. In 
each string there are n − k + 1 substrings of length k, and so there are Θ(n2) 
pairs of substrings, where one substring is from one string and one is from the other. 
For a pair of substrings, we define the match-count as the number of opposing 
characters that match when the two substrings of length k are aligned. 
The problem is to compute the match-count for each of the Θ(n2) pairs of substrings 
from the two strings. Clearly, the problem can be solved with O(kn2) operations 
(character comparisons plus arithmetic operations). But by better organizing the 
computations, the time can be reduced to O(n2) operations. (From Paul Horton.)


'''

def match_count1(s1, s2, k):
    # Brute force O(kn^2)
    n = len(s1)
    ans = [[0]*(n-k+1) for _ in range(n-k+1)]
    def count(s1, s2):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                cnt += 1
        return cnt
    for i in range(n-k+1):
        for j in range(n-k+1):
            ans[i][j] = count(s1[i:i+k], s2[j:j+k])
    return ans  

def match_count2(s1, s2, k):
    # Optimized O(n^2)
    n = len(s1)
    ans = [[-1]*(n-k+1) for _ in range(n-k+1)]
    for l in range(n-k+1):
        i = 0
        j = i+l
        cnt = 0
        for ii in range(k):
            if s1[i+ii] == s2[j+ii]:
                cnt += 1        
        ans[i][j] = cnt  
        for i in range(k, n):
            j = i+l
            if j >= n: break
            if s1[i-k] == s2[j-k]:
                cnt -= 1
            if s1[i] == s2[j]:
                cnt += 1
            # print(i,j,l)
            ans[i-k+1][j-k+1] = cnt
    for l in range(n-k+1):
        j = 0
        i = j+l
        cnt = 0
        for ii in range(k):
            if s1[i+ii] == s2[j+ii]:
                cnt += 1        
        ans[i][j] = cnt  
        for j in range(k, n):
            i = j+l
            if i >= n: break
            if s1[i-k] == s2[j-k]:
                cnt -= 1
            if s1[i] == s2[j]:
                cnt += 1
            # print(i,j,l)
            ans[i-k+1][j-k+1] = cnt
    return ans


import string
import random
from timeit import default_timer as timer
from datetime import timedelta

if __name__ == "__main__":
    a = 'adcfgftfc'
    b = 'accatggcf'
    for r in match_count1(a, b, 4):
        print(r)
    print("=========================")
    for r in match_count2(a, b, 4):
        print(r)
    n, k = 1000, 300
    s1 = ''
    for i in range(n):
        s1 += chr(random.randint(0, 25)+ord('a'))
    s2 = list(s1)
    print(len(s1), len(s2))    
    random.shuffle(s2)
    s2 = ''.join(s2)
    start = timer()
    sol1 = match_count1(s1, s2, k)
    end = timer()
    print(timedelta(seconds=end-start))
    start = timer()
    sol2 = match_count2(s1, s2, k)
    end = timer()
    print(timedelta(seconds=end-start))
    for r1, r2 in zip(sol1, sol2):
        if r1 != r2:
            print(r1, r2)
        # print(sum(r1), sum(r2))


      

    
    
