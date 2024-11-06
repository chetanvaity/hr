
#merge  sorted arrays in place

# a = [ 1, 4, 5, 7, _, _, _, _, _ ]
# b = [ 2, 5, 8, 9, 10 ]

def inPlaceSort(a, b, n, m):
  i = n-1
  j = m-1
  for (k=n+m-1, k<=0, k--):
    if (i < 0):
      for (s=0, s<=j, s++)
        a[s] = b[s]
        return
    if (j < 0):
       return
    if a[i] > b[j]:
      a[k] = a[i]
      i = i-1
    else:
      a[k] = b[j]
      j = j-1
  
