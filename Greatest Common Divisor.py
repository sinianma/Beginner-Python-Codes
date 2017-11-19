def gcdIter(a,b):
    divisor = ""
    if b > a:
        for i in range (1, b+1):
            if a % i == 0 and b % i == 0:
                divisor = i
        return divisor
    if a > b:
        for i in range (1, a+1):
            if a % i == 0 and b % i == 0:
                divisor = i
        return divisor
    if a==b:
        divisor = a
        return divisor

