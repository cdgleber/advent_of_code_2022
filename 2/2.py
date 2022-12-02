#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
f = '2.txt'
f_file = open(f, encoding='utf-8-sig')
puzzle_input = f_file.read()
values = puzzle_input.split('\n')


# In[3]:


games = []
for value in values:
    games.append(value.split(' '))


# In[11]:


results = []
for game in games:
    if game[0]=='A': #rock
        if game[1]=='X': #rock 1 draw 4
            results.append(4)
        elif game[1]=='Y': #paper 2 win 6
            results.append(8)
        elif game[1]=='Z': #scissors 3 loss 0
            results.append(3)
    elif game[0]=='B': #paper
        if game[1]=='X': #rock 1 loss 0
            results.append(1)
        elif game[1]=='Y': #paper 2 draw 3
            results.append(5)
        elif game[1]=='Z': #scissors 3 win 6
            results.append(9)
    elif game[0]=='C': #scissors
        if game[1]=='X': #rock 1 win 6 
            results.append(7)
        elif game[1]=='Y': #paper 2 loss 0
            results.append(2)
        elif game[1]=='Z': #scissors 3 draw 3
            results.append(6) 


# In[12]:


sum(results)


# In[13]:


results = []
for game in games:
    if game[0]=='A': #rock
        if game[1]=='X': #loss 0 scissors 3
            results.append(3)
        elif game[1]=='Y': #rock 1 draw 3
            results.append(4)
        elif game[1]=='Z': #win 6 paper 2
            results.append(8)
    elif game[0]=='B': #paper
        if game[1]=='X': #loss 0 rock 1
            results.append(1)
        elif game[1]=='Y': #draw 3 paper 2
            results.append(5)
        elif game[1]=='Z': #win 6 scissors 3
            results.append(9)
    elif game[0]=='C': #scissors
        if game[1]=='X': #loss 0 paper 2
            results.append(2)
        elif game[1]=='Y': #draw 3 scissors 3
            results.append(6)
        elif game[1]=='Z': #win 6 rock 1
            results.append(7)
sum(results)


# In[ ]:




