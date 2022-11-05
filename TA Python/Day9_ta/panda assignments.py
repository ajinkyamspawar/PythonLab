#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[8]:


s=pd.Series([10,20,30])
print(s)


# In[10]:


s1=pd.Series([40,50,60])
print(s1)


# In[11]:


s+s1


# In[12]:


s1-s


# In[13]:


s1%s


# In[14]:


s1/s


# In[15]:


s1//s


# In[20]:


d={1:2,2:4,3:6}
s= pd.Series(d)
print(s)


# In[25]:


a=np.arange(1,10)
print(a)


# In[26]:


s=pd.Series(a)
print(s)


# In[31]:


print(s.loc['0':'3'])


# In[33]:


s.head(6)


# In[74]:


mydict={'Prod_ID':[101,102,103,104,105,106,107],'Prod_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],'City':['Delhi','Mumbai','Chennai','Kolkatta','Delhi','Chennai','Bengalore']}
print(mydict)
s= pd.Series(labels)


# In[75]:


df=pd.DataFrame(mydict)
df


# In[78]:


df.index=('a','b','c','d','e','f','g')
df


# In[79]:


df.info()
df.describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


S

