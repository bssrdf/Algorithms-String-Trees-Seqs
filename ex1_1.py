'''
Determine if string a is a circular rotation of string b. 


'''

from zalgorithm import zarray


def circular(a, b):
    if len(a) != len(b):
        return False
    c = b + "$" + a + a
    z = zarray(c)
    # print(c, z)
    for i in range(len(c)):
        if z[i] == len(a):
            return True
    return False

if __name__ == "__main__":
    a = 'defabc'
    b = 'abcdef'
    print(circular(a,b))
    a = 'defabd'
    b = 'abcdef'
    print(circular(a,b))
    a = 'bacab'
    b = 'cabba'
    print(circular(a,b))


    
