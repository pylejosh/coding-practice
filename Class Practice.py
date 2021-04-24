#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Creation of Search Party Class
class SearchParty:
    
    def __init__(self, name, type, age, color):
        self.name = name
        self.type = type
        self.age = age
        self.color = color
        
    def move(self, steps):
        print(self.name, 'is moving forward', steps, 'steps.')
        
j1 = SearchParty('Josh', 'adult', '35', 'white')
j1.move(3)
s = SearchParty('Shweta', 'adult', '36', 'brown')
s.move(3)
j2 = SearchParty('Jadon', 'baby', '1', 'white')
j2.move(1)
a = SearchParty('Aspen', 'puppy', '0.25', 'golden')
a.move(12)

print(a.name,'is a', a.color, a.type + '.')

    


# In[33]:


print(a.name,'is a', a.color, a.type + '.')


# In[ ]:




