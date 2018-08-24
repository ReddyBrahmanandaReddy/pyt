def sumOfAP( a, d,n) :
    sum = 0
    i = 0
    while i < n <100000 :
        sum = sum + a
        a = a + d
        i = i + 1
    return sum
n = 3
a = 2
d = 10
print (sumOfAP(a, d, n),end="")
