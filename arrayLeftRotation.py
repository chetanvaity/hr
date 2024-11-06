def array_left_rotation(a, n, k):
    b = [None] * n
    for i in xrange(n):
        j = n - k + i
        if (j >= n):
            j = j - n
            pass
        #print "i=%d, j=%d" % (i, j)
        b[j] = a[i]
    return b

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
