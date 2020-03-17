#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys

def one_to_one(s1,s2):
    if len(s1)<=len(s2):
        d={}
        for k in range (len(s1)):
            if s1[k] not in d:
                d[s1[k]]=s2[k]
                
            if d[s1[k]]!=s2[k]:
                return False
        return True
    return False 


# In[15]:


print(one_to_one("abc","bcd"))
print(one_to_one("foo","bcd"))
print(one_to_one("213","foo"))

