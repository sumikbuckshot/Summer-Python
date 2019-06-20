#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


df=pd.read_csv("com.csv")
#df1=pd.read_csv('http://13.234.66.67/summer19/datasets/info.csv')


# In[3]:


df.info()


# In[10]:


#df1.info()


# In[11]:


#to print all the data
df


# In[12]:


#top two rows
df.head(3)


# In[14]:


df.tail(2)


# In[21]:


#one particular column
df['Name'],df['Department']


# In[22]:


#for selecting rows and columns
df.iloc[0:,0]


# In[23]:


df.iloc[0:,[1,3]]


# In[27]:


df['Salary'].max()


# df['salary'].min()

# In[28]:


df['Salary'].mean()


# In[30]:


df['Salary'].sum()


# In[31]:


df.values


# In[38]:


df.values[3][1]


# In[ ]:





# In[ ]:




