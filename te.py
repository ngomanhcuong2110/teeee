#!/bin/python3

# Write your code here
    import string
    symbols_low = string.ascii_lowercase
    symbols_up = string.ascii_uppercase
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
        else:
            res.append(c)
                       
    return "".join(map(str, res))
    

def missingNumbers(arr, brr):
    # Write your code here
    from collections import Counter
    c1=Counter(arr)
    c2=Counter(brr)
    c=c2-c1
    
    newlist = list()
    for i in c.keys():
        newlist.append(i)
    return(sorted(newlist))

def stack
    l1=sum(h1)
    l2=sum(h2)
    l3=sum(h3)
    while l1 !=0 and l2 != 0 and l3 != 0 and (l1!=l2 or l2!=l3):
        if max(l1, l2, l3) == l1:
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            l3 = l3 - h3[0]
            h3.pop(0)
    else:
        if l1==l2 and l2==l3:
            return l1
        else:
            return 0


    sum=0
    prev_sum = 0
def substrinh
    for i, d in enumerate(n):
        temp_sum = prev_sum * 10 + (i + 1) * int(d)
        
        sum += temp_sum
        prev_sum = temp_sum
    return sum % (10 ** 9 + 7)
