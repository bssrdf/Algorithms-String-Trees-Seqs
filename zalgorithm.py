def zarray(s):
    n = len(s)
    z = [0]*n
    # [L,R] make a window which matches
    # with prefix of s
    left, right, k = 0, 0, 0
    for i in range(1, n):        
        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > right:
            left, right = i, i
            # R-L = 0 in starting, so it will start
            # checking from 0'th index.
            while right < n and s[right - left] == s[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - left
            # if Z[k] is less than remaining interval
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                # else start from R and check manually
                left = i
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[i] = right - left
                right -= 1
    return z