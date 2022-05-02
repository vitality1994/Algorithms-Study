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

# Set function: set()
#
# The difference between 'set' & 'list' is...
# - no same elements in the set
# - order does not matter
#
# functions for 'set'
# - len(s)    ... parameter is 'set'.
# - s.add(x)
# - s.discard(x)
# - s.clear()
# - x in s    ... return boolean type (yes or no)

# +
# Goal: Find people who have same name!
# input is list. output is set.

def find_same_name(s): # s is the parameter for list.
    result = set()
    for i in range(len(s)):
        name_1=s[i] 
        for j in range(i+1, len(s)):
            name_2 = s[j]
            if name_1 == name_2:
                result.add(name_1)
    return result


# -

# Test
s = ['Tom', 'David', 'Jerry', 'Paul', 'Tom', 'Paul']
find_same_name(s)

# Computational complexity for this algorithm is...
# if n = 4 (if there are four names), 
# number of times for comparing is n-1, n-2, ... 2, 1
# sum of terms above is 1+2+3+...+(n-2)+(n-1) =
#
# $$\frac{(n-1)(n-1+1)}{2} = \frac{1}{2}n^2-\frac{1}{2}n$$
#
# So, Big O notation is $O(n^2)$. 
#
# $O(n^2)$ means that if input n increased, computation time increased dramatically.
