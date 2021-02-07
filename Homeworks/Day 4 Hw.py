#!/usr/bin/env python
# coding: utf-8

# In[49]:


def primeNumber(i):
    for num in range(2,101):
        prime = True 
        for i in range(2,num):
            if (num%i==0):
                prime = False
        if prime:
            print (num,"is a prime number")
primeNumber(100)

