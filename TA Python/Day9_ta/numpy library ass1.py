#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


l1=[1 2 3]
print(l1)


# In[3]:


print(l1)


# In[6]:


a=np.arange(1,11)
print(a)


# In[9]:


b=np.arange(0,10).reshape(2,5)
print(b)


# In[14]:


c=np.arange(0,45).reshape(3,5,3)
print(c)


# In[17]:


print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)


# In[18]:


print(b.dtype)
print(b.ndim)
print(b.shape)
print(b.size)


# In[20]:


print(c.dtype)
print(c.ndim)
print(c.shape)
print(c.size)


# In[26]:


d=np.empty((3,5))
print(d)


# In[29]:


d=np.zeros((3,5))
print(d)


# In[6]:


d=np.full((3,5),1)
print(d)


# In[4]:


import numpy as np


# In[5]:


e=np.ones(4)
print(e)


# In[8]:


e=np.ones((5,2,3))
print(e)


# In[14]:


f=np.arange(0,10).reshape(2,5)
print(f)


# In[15]:


g=np.arange(14,41).reshape(3,3,3)
print(g)


# In[17]:


h=np.arange(1,41).reshape(8,5)
print(h)


# In[27]:


i=h.reshape(4,10)
print(i)


# In[28]:


j=h.reshape(4,10)
print (j)


# In[33]:


print(j[0:3,0:4])
print(j)


# In[41]:


print(j[0:3,5])


# In[47]:


print(j[2:4,9])


# In[49]:


print(j[0:,3:6])


# In[50]:


print(j)


# In[64]:


#a=print([j%2==1])
#print(a)
print(j[j%2==1])
print(j)


# In[72]:


a=j[j%2==0]
a=-1
print(a)


# In[77]:


a=j
a[a%2==0]=-1
print(a)


# In[78]:


k=np.arange(1,10)
l=np.arange(11,20)
print(k)
print(l)


# In[79]:


m=np.append(k,l)
print(m)


# In[87]:


z=np.arange(1,17)
print(z)


# In[91]:


z.resize(2,8)
print(z)


# In[8]:


import numpy as np
z=np.random.randint(15,29,10)
print(z)


# In[13]:


m=np.sort(z)
m


# In[14]:


print(m[::-1])


# In[19]:


a=np.arange(1,16).reshape(5,3)
print(a)


# In[24]:



a+4


# In[25]:


a*2


# In[26]:


a-2


# In[29]:


a/2


# In[4]:


import numpy as np


# In[ ]:





# In[6]:


a=np.arange(1,10).reshape(3,3)
b=np.arange(11,20).reshape(3,3)


# In[7]:


a


# In[8]:


b


# In[9]:


a+b


# In[10]:


a-b


# In[11]:


a%b


# In[12]:


a/b


# In[13]:


a.dot(b)


# In[14]:


a 
b


# In[15]:


a


# In[18]:


b//a


# In[19]:


b/a


# In[20]:


a.min()


# In[21]:


a.max()


# In[22]:


a.sum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




