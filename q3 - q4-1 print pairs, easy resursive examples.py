# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# q3-1:
#
# If two people will be picked out on 'n' people, make algorithm that will show all of pairs of two people.

def pairs(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            print(s[i], s[j])


# +
list = ["Tom", "Jerry", "Mike"]

pairs(list)


# -

# q4: Factorials with Recursive Algorithm
#
# 1! = 1
#
# 2! = 2*1
#
# 3! = 3*(2*1)   
#
# 4! = 4*(3!)
# ...
#
# n! = n*(n-1)!

def factorial(s):
    if s == 1:
        return s
    else:
        s = s*factorial(s-1)
        return s


factorial(5)


# computation complexity is O(n) for the algorithm above. Because...<br><br>
# If fact(4) is implemented, <br>
# fact(1) = 1 <br>
# fact(2) = 2x1 = 2 <br>
# fact(3) = 3x2 = 6 <br>
# fact(4) = 4x6 = 24 <br>
# total number of multiplication is '3'.

# +
# q 4-1: calculate sum from 1 ~ n using recursion.

def sum_to_end(n):
    if n == 1:
        return 1
    else:
        n = n + sum_to_end(n-1)
    
    return n

sum_to_end(10)
