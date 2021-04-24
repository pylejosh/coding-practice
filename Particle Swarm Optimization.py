#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
search_party = ['j1','s1','j2','a1']
color = ['w','b','w','g']
angles = random.sample(range(0,360),4)
coordinates = np.random.randint(10, size=(4,2))
df = pd.DataFrame(coordinates, columns = ['xpos', 'ypos'])
df['xpos'] = df['xpos'].astype(float)
df['ypos'] = df['ypos'].astype(float)
df['direction'] = pd.Series(angles,index=df.index)
df['explorer'] = pd.Series(search_party,index=df.index)
df['color'] = pd.Series(color,index=df.index)
df['time'] = pd.Series(0,index=df.index)
df['altitude'] = pd.Series(0.0,index=df.index)
df = df[['explorer', 'color','xpos', 'ypos', 'direction','time','altitude']]
print(df)
plt.scatter(df['xpos'],df['ypos'])
plt.show()


# In[2]:


def ydistance(angle):
    vertmove = round(math.sin(math.radians(angle)),6)
    return vertmove;

def xdistance(angle):
    horizmove = round(math.cos(math.radians(angle)),6)
    return horizmove;


# In[3]:


def evaluate(x, y):
    altitude = math.sin(5-y)+(x/20)**2+math.cos(4+x)+(y/12)**2
    return altitude;


# In[4]:


for i in range(0,len(df['time'])):
    df['time'][i]=df['time'][i]+1
    df['altitude'][i]=evaluate(df['xpos'][i],df['ypos'][i])
print(df)


# In[ ]:





# In[ ]:





# In[ ]:




