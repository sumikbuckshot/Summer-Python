#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy


# In[2]:


import numpy as np


# In[3]:


a=np.array([2,7,1,99,4])


# In[4]:


type(a)


# In[5]:


b=np.array([12,17,11,199,14])


# In[6]:


a


# In[7]:


b


# In[8]:


a[0]


# In[9]:


b[2]


# In[13]:


b[3]


# In[11]:


b[4]


# In[12]:


a+b


# In[15]:


a+2


# a*2

# In[16]:


a*2


# In[17]:


a**2


# In[20]:


x=np.array([[2,5,8],[3,6,1]])


# In[21]:


x


# In[25]:


x[1]


# In[26]:


x[1][1]


# In[27]:


x[2][1]


# In[28]:


x[1][2]


# In[30]:


y=x+7


# In[31]:


x*2


# In[32]:


x**2


# In[33]:


x**3


# In[34]:


y


# In[35]:


z=np.array([[2,7],[3,8],[2,9],[9,2]])


# In[36]:


z


# In[37]:


x


# In[38]:


x.shape


# In[39]:


z.shape


# In[40]:


z


# In[41]:


z[0:2]


# In[42]:


z[0:,]


# In[43]:


z[0:0,]


# In[44]:


z[0:,0]


# In[45]:


z[0:1,0]


# In[46]:


z[0:0,0]


# In[47]:


z[0:1,1]


# In[48]:


z[0:2,1]


# In[51]:


z[0:,0:1]


# In[52]:


x[0:,[0,2]]


# In[55]:


z[0:,[0,1]]


# In[57]:


z[[0,3],1]


# In[59]:


b=np.array([[1,9,7],[3,2,8],[4,5,6],[2,9,0]])


# In[60]:


b


# In[61]:


b[1,]


# In[62]:


b[,1]


# In[63]:


b[0,1]


# In[65]:


b[0:,1]


# In[66]:


b[0:,0:1]


# In[67]:


b[1:2,1]


# In[68]:


b[1:3,1]


# In[69]:


b[1:3,1:2]


# In[70]:


b[1:4,2:1]


# In[71]:


b[1:4,2:2]


# In[72]:


b[1:4,2]


# In[74]:


b[1:4,[0,2]]


# In[75]:


x


# In[77]:


x1=x.reshape(3,2)


# In[78]:


x1


# In[79]:


x.transpose


# In[80]:


x


# In[81]:


np.zeros((3,6))


# In[83]:


np.zeros((3,6),dtype=int)


# In[84]:


np.full((4,5),9)


# In[86]:


for i in dir(np):
    if 'zer' in i:
        print(i)


# In[87]:


[i for i in dir(np) if 'zer' in i]


# In[88]:


i for i in dir("mango") if 'mang' in i


# In[ ]:




