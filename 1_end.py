#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

f = '1.txt'
f_file = open(f, encoding='utf-8-sig')
puzzle_input = f_file.read()

values = puzzle_input.split('\n')


# In[2]:


values


# In[7]:


elf = []
elves = []
for value in values:
    if len(value)>0:
        elf.append(int(value))
    else:
        elves.append(elf)
        elf = []


# In[8]:


elves


# In[9]:


elf_totals = []
for elf in elves:
    elf_totals.append(sum(elf))


# In[14]:


elf_totals


# In[15]:


max(elf_totals)


# In[26]:


sum(elf_totals[:3])


# In[17]:


elf_totals_sorted


# In[ ]:




