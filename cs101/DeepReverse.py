# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

#my way
def deep_reverse(p):
    n = 0
    p = p[::-1]
    while n < len(p):
        if is_list(p[n]):
            p[n] = deep_reverse(p[n])
        n = n + 1
    return

#another way
def deep_reverse(p):
    if is_list(p):
        return map(deep_reverse, p[::-1])
    else:
        return p

#above way can be simplify as:
def deep_reverse(p):
     return map(deep_reverse, p[::-1]) if is_list(p) else p


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]


q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]






