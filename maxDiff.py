def maxDifference(a):
    minE = sys.maxint
    maxE = -sys.maxint
    minIndex = -1
    maxIndex = -1
    i = 0
    for e in a:
        if e < minE:
            minE = e
            minIndex = i
        if e > maxE:
            maxE = e
            maxIndex = i

    print maxE
    print minE

    if minIndex == 0 and maxIndex == (len(a) - 1):
        return -1
    
    md1MinE = sys.maxint
    for i in xrange(maxIndex):
        if a[i] < md1MinE:
            md1MinE = a[i]

    md2MaxE = -sys.maxint
    for i in xrange(minIndex, len(a)):
        if a[i] > md2MaxE:
            md2MaxE = a[i]

    md1 = maxE - md1MinE
    md2 = md2MaxE - minE

    if md1 > md2:
        return md1
    else:
        return md2
    
