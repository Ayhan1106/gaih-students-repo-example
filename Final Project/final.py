#!/usr/bin/env python
# coding: utf-8

# In[9]:


#company management system
class employees:
    def __init__(self, first_name, last_name,work, age, language):
        self.name = first_name
        self.lname = last_name
        self.job = work
        self.age = age
        self.language = language

    def showName(self):
        print (self.name + " " + self.lname)

    def showlanguage(self):
        print(self.name + " " + self.lname +" "+ self.job,"can speak:", self.language)

class company_managers(employees):
    pass

a  = company_managers("Ayhan","Aysoy","Manager","18","Spanish and English")
a.showlanguage()

