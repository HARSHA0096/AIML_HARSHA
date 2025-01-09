#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter+1
        


# In[2]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)

    if l%2 == 0:
        median = (num_list[int(1/2)] + num_list[int((1/2))-1])/2
    else:
        median = num_list[int(1/20)]
    return median                  


# In[5]:


median_value(23,5,9,8,7,9,4,8,8,6,4,6,5)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




