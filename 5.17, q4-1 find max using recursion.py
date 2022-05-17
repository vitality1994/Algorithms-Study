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

# +
# find maximum number using recursion.

# For recursion, 'end' condition is required.

def find_max(a, n):
    if n == 1:
        return a[0] # one element? just return that.
    
    max_n_1 = find_max(a, n-1) 
    # maximum element among the first ~ n-1 th
    # In the most inside loop, max_n_1 = a[0],
    # and max_n_1 = a[0] will be compared with
    # a[1] when n == 2;
    if max_n_1 > a[n-1]:
        return max_n_1
    else:
        return a[n-1]
# -



# +
s = [1, 3, 5, 3, 1, 23, 12, 3, -1]

find_max(s, len(s))
