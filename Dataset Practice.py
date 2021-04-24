#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import lux


# In[4]:


sbdata = pd.read_csv('/Users/joshuapyle/Downloads/superbowl.csv')


# In[ ]:


sbdata


# In[ ]:


print(sbdata['Winner Pts'].dtypes)


# In[ ]:


print(sbdata['SB'].dtypes)


# In[ ]:


sbdata[:2]['SB']


# In[ ]:


sbdata.loc[[2,4,6],:]


# In[ ]:


sbdata.iloc[1,2:8]


# In[ ]:


sbdata['Margin of Victory'] = sbdata['Winner Pts'] - sbdata['Loser Pts']


# In[ ]:


avgmargin = sbdata['Margin of Victory'].mean()
print(avgmargin)
print(sbdata['Margin of Victory'].dtypes)


# In[ ]:


sbdata[sbdata['Margin of Victory'] > avgmargin]


# In[ ]:


sbdata.groupby('State').size().nlargest(8)


# In[ ]:


sbdata


# In[2]:


netflixdata = pd.read_csv('/Users/joshuapyle/Downloads/netflix_titles.csv')


# In[3]:


netflixdata


# In[ ]:




