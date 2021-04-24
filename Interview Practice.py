#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Implement division of two positive integers without 
# using the division, multiplication, or modulus operators. 
# Return the quotient as an integer, ignoring the remainder.

def remainder(x, y):
    c = 0
    d = y - x
    while d >= 0:
        d = d - x
        c += 1
    return c;

samplenum = remainder(3,9)
print(samplenum)


# In[7]:


# Given an integer n and a list of integers l, 
# write a function that randomly generates a number 
# from 0 to n-1 that isn't in l (uniform)

import numpy as np

l = [0,2,4,5,7,8,9]

def numgen(n, x):
    r = np.random.randint(n-1)
    c = 0
    while r in x:
        r = np.random.randint(n-1)
        c += 1
    print("It took " + str(c) +" draws before we found a number not in our list, but finally we drew " + str(r) + "!")
    return c;    

example = numgen(10,l)


# In[68]:


# Problem 1
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

l = [1,7,8,9]
pair_sum_match = False

def addup(l,k):
    pair_sum_match = False
    for i in range(0, len(l)):
        if pair_sum_match == False: 
            print("Index ",i," Results:\n")
            first_num = l[i]
            for j in range(i+1, len(l)):
                second_num = l[j]
                pair_sum_match = first_num + second_num == k
                print(first_num)
                print(second_num)
                print(pair_sum_match)

    if pair_sum_match == True:
        match_result = str('We did find a match!  Numbers ' + str(first_num) + ' & ' + str(second_num) + ' sum to ' + str(k) + '!')
    else: 
        match_result = str('We did not find a match; sorry!') 
        
    return match_result;
    
problem1 = addup(l,12) 
print(problem1)


# In[97]:


# Problem 2
# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

l = [1,2,3,4,5]
j=[]
    
def list_product(l):
    for i1 in range(len(l)):
        k=l.copy()
        k[i1]=1
        cumulative_product=1
        for i2 in range(len(l)):
            cumulative_product = cumulative_product * k[i2]
        j.append(cumulative_product)
    return j;

problem_2 = list_product(l)
print(problem_2)


# In[98]:


# Problem 3
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

print('This question makes absolutely no sense!')


# In[4]:


# Problem 4
# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

l = [0, 2, 1, 3, 4, 18]

def list_check(l):
    i = 1
    check = True
    l_revised = sorted(l)
    while check == True:
        if i in l_revised:
            check = True
            i += 1
        else:
            return print("The first positive integer not in the array is", str(i));

problem_4 = list_check(l)


# In[6]:


# Problem 118
# Given a sorted list of integers, square the elements and give the output in sorted order.
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

import numpy as np

def squareandreturn (x):
    squares = np.square(x)
    sortedsquares = np.sort(squares)
    return print(sortedsquares)

squareandreturn([2,-4,5,1,50])


# In[7]:


# Problem 394

'''
This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def path_exists(node, k):
    if node is None:
        return False

    if node.left is None and node.right is None:
        return node.val == k

    return path_exists(node.left, k - node.val) or path_exists(node.right, k - node.val)


# In[8]:


# Problem 386
'''
This problem was asked by Twitter.

Given a string, sort it in decreasing order based on the frequency of characters. If there are multiple possible solutions, return any of them.

For example, given the string tweet, return tteew. eettw would also be acceptable.
'''


# In[75]:


# Problem 451
'''This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.'''

import time

starttime = time.time()

def fib(n):
    sequence = [0,1]
    index = 1
    while index < n:
        nextdigit = sequence[0] + sequence[1]
        sequence.append(nextdigit)
        sequence.pop(0)
        index += 1
    return sequence[1]

print(fib(1000))

endtime = time.time()
taskduration = round(endtime - starttime,4)

print('This process took ' + str(taskduration) + ' seconds.')


# In[20]:


functions = []
for i in range(10):
    x = lambda i : i + 1
    functions.append(x(i))

for f in functions:
    print(f)


# In[ ]:




