'''

Suffix-prefix matching. 

Give an algorithm that takes in two strings α and β, of lengths n and m, and 
finds the longest suffix of α that exactly matches a prefix of β. The algorithm 
should run in O(n + m) time.

'''

from zalgorithm import zarray


def longestSuffixPrefix(a, b):    
    c = b + "$" + a 
    z = zarray(c)     
    mx, res = 0, ''
    for i in range(len(c)):
        idx = i-len(b)-1 
        if  z[i] == (len(a) - idx) and z[i] > mx:
            mx = z[i]            
            res = a[idx:idx+z[i]]
    return res

if __name__ == "__main__":
    a = 'defabc'
    b = 'abcdef'
    print(longestSuffixPrefix(a, b))
    a = 'defabce'
    b = 'abcdef'
    print(longestSuffixPrefix(a, b))
    a = 'defabsdsdfncxxiwewsdcsrunadkfncxxnrnsp'
    b = 'fncxxiwewsdcsdihjmsdjkm'
    print(longestSuffixPrefix(a, b))