'''

Similar to Exercise 1, give a linear-time algorithm to determine whether a linear 
string α is a substring of a circular string β. A circular string of length n is 
a string in which character n is considered to precede character 1 (see Figure 1.6). 
Another way to think about this problem is the following. Let  be the linear 
string obtained from β starting at character 1 and ending at character n. Then α 
is a substring of circular string β if and only if α is a substring of some 
circular rotation of .

'''

from zalgorithm import zarray


def isSubCircular(a, b):
    c = a + "$" + b + b
    z = zarray(c)
    for i in range(len(c)):
        if z[i] == len(a):
            return True
    return False
    

if __name__ == "__main__":
    a = 'cacc'
    b = 'accatggc'
    print(isSubCircular(a, b))
    a = 'cdcc'
    b = 'accatggc'
    print(isSubCircular(a, b))


