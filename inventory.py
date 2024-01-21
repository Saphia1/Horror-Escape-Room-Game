import Pygame as py
from Screens import Screens
from Inventoryscreen import displayinventory

class inventory ():
    def __init__(self):
        self._inventory=[""]
    def add(self,obj):
        self._inventory.append(obj)
    def drop(self,obj):
        for i in range (0,len(self._inventory)):
            if self._inventory == obj:
                self._inventory.remove(i)
    def open(self):
        displayinventory(inventory)
    def finditem(self,item):
        for i in range (0,len(self._inventory)):
            if self._inventory == item:
                present=True
                return present
            else:
                present=False
                return present
    def getinventory(self):
        return self._inventory
