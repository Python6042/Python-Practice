#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The following program defines about the class,constructor,class attributes,instance attributes,objects


# In[2]:


#Syntax of the class as below:


# In[7]:


'''class instance name/class name
    Doc string: Description about the class
    def __init__(self): '''


# In[10]:


class person: # person class 
    count=0 #class a ttribute
    def __init__(self): #constructor
        self.name="Fayaz" #instance attribute
        self.age=30 #instance attribute
    def displayInfo(self): #method
        print(self.name, self.age)
p1=person()
p1.name


# In[11]:


p1.age


# In[ ]:




