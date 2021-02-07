#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Animals:
    def __init__(self, name, pedigree, legs_number):
        self.name = name
        self.species = pedigree
        self.legs = legs_number

    def print_name(self):
        print(self.name)

    def print_species(self):
        print(self.name + " is " +  self.species)

    def print_legs(self):
        print(self.name + " has got " + self.legs + " legs. "  )

    def showInfo(self):
        print(self.name + " is " + self.species +" .It has "+self.legs + " legs. ")

class Dogs(Animals):
    pass
class Cats(Animals):
    pass


# In[24]:


cat= Cats("Kitty","siamese cat","4",)
dog= Dogs("Max","German shepher","4")
cat.showInfo()
dog.showInfo()

