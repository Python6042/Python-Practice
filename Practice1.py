#!/usr/bin/env python
# coding: utf-8

# In[2]:


# A Simple python programme

First=input("Your first name:")
Second=input("Your second Name:")
print(f"Hollow there{First}{Second}")


# In[3]:


print("Hollow there %(First,Second)")


# In[4]:


print("hollow there"%(First))


# In[6]:


print("Hollow there! %s %s"%(First,Second))


# In[13]:


# The below illustrate the use of Stripping
First="Hanuman       "
Second ="    Ramesh    "
print("The First name is:",First.rstrip())


# In[11]:


# Finding Second name

print("The second name is:",Second)


# In[12]:


print("The second name is:",Second.lstrip())


# In[15]:


# Diffrent ways of printing a variable
# Method1

print("The second name is: %s" %Second)


# In[16]:


# Diffrent ways of printing a variable
# Method2

print(f"The second name is:{Second}")


# In[18]:


# Diffrent ways of printing a variable
# Method3

print("The second name is:",Second.strip())


# In[ ]:




