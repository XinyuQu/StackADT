#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:09:45 2017

@author: shikhar
"""
class ArrayStack():
  def __init__(self):
    self.items = []
    self.size = 0
    
  def top(self):
    return self.size-1
    
  def push(self, element):
    print("Size of stack", self.size)
    self.items.append(element)
    self.size += 1
    
  def pop(self):
    #print("ITEMS IN STACK", self.items, 'len', len(self.items), 'size', self.size, 
     #     'top', self.top())
    popped_item = self.items[self.top()]
    del self.items[self.top()]
    self.size -= 1
    return popped_item
  
  def __len__(self):
    return self.size


  
class ArrayDeque():
  def __init__(self, maxsize = 10):
    self.right = (maxsize//2)
    self.left = (maxsize//2) - 1
    self.left_count = 0
    self.right_count = 0
    self.maxsize = maxsize
    self.size = 0
    self.items = [None] * self.maxsize
    
  def pushright(self, element):
    if self.size == self.maxsize:
      self._resize()
    self.items[self.right] = element
    self.size += 1
    self.right = (self.right + 1) % self.maxsize
    print("RIGHT", self.right)
    self.right_count += 1
    
  def popright(self):
    if self.size == 0:
      raise ValueError
    self.right = (self.right - 1) % self.maxsize
    self.size -= 1
    self.right_count -= 1
    element = self.items[self.right]
    self.items[self.right] = None
    return element
  
  def pushleft(self, element):
    if self.size == self.maxsize:
      self._resize()
    self.items[self.left] = element
    self.size += 1
    self.left = (self.left - 1) % self.maxsize
    self.left_count += 1
    
  def popleft(self):
    if self.size == 0:
      raise ValueError
    self.left = (self.left + 1) % self.maxsize
    self.size -= 1
    self.left_count -= 1
    element = self.items[self.left]
    self.items[self.left] = None
    return element

  def __len__(self):
    return self.size
  
  def _resize(self):
    original_right = self.maxsize // 2
    original_left = (self.maxsize // 2) - 1
    original_maxsize = self.maxsize
    self.maxsize *= 2
    new_items = [None] * self.maxsize
    new_right = self.maxsize // 2
    new_left = (self.maxsize // 2) - 1
    #Copying left half
    while (original_left % original_maxsize) != self.left:
      print(new_items)
      new_items[new_left] = self.items[original_left % original_maxsize]
      new_left -= 1
      original_left -= 1
    self.left = new_left

    #Copying right half
    while (original_right % original_maxsize) != self.right:
      print(new_items)
      new_items[new_right] = self.items[original_right % original_maxsize]
      new_right += 1
      original_right += 1
    self.right = new_right
      
    self.items = new_items[:]
    self.right
      

class MidStackADT():
  def __init__(self):
    self.Stack = ArrayStack()    
    self.Deque = ArrayDeque()
    self.size = self.Stack.size + self.Deque.size
    
  def top(self):
    print(self.Deque.items[self.right-1])
    return(self.Deque.items[self.right - 1])
  
  def _balance_stack_deque(self):
    while self.Stack.size < self.Deque.size:
      self.Stack.push(self.Deque.popleft())
  
  def push(self, element):
    if self.size == 0:
      self.Stack.push(element)
    else:
      self.Deque.pushright(element)
    self._balance_stack_deque()      
    self.size += 1
    
  def mid_push(self, element):
    self._balance_stack_deque()
    self.Deque.pushleft(element)
    self._balance_stack_deque()
    
  def pop(self):
    if self.Deque.right_count > 0:
      print(self.Deque.popright())
    elif self.Deque.left_count > 0:
      print(self.Deque.popleft)
    else:
      print(self.Stack.pop())
#==============================================================================
#     
#   def __str__(self):
#     a = []
#     for element in self.Stack.items:
#       a.append(element)
#     for element in self.Deque.items:
#       if element != None:
#         a.append(element)
#     return str(a)
#==============================================================================
        
    
  
if __name__ == "__main__":
  MyStack = MidStackADT()
  for i in range(5):
    MyStack.push(i)
    print("ADT",MyStack)    
    print("Stack", MyStack.Stack.items)
    print("Deque", MyStack.Deque.items)
    
  for i in range(-5, -1):  
    MyStack.mid_push(i)
    print("ADT",MyStack)    
    print("Stack", MyStack.Stack.items)
    print("Deque", MyStack.Deque.items)  
    
#==============================================================================
#     
#   for i in range(5, 10):
#     MyStack.push(i)
#     print("ADT",MyStack)    
#     print("Stack", MyStack.Stack.items)
#     print("Deque", MyStack.Deque.items)
#==============================================================================
    
  while True:
    try:
      MyStack.pop()
    except IndexError:
      print("No more elements")
      break
    
    
    
  


#==============================================================================
# Deque = ArrayDeque()
# for i in range(5):
#   Deque.pushright(10)
#   print(Deque.items)
#     
# for i in range(5):
#   Deque.pushleft(-1)
#   print(Deque.items)
#   
# Deque.pushleft(-1)
# print(Deque.items)
#   
# Deque.pushright(10)
# print(Deque.items)
# 
# 
# for i in range(5):
#   Deque.pushleft(-1)
#   print(Deque.items)
#   
# Deque.popleft()
# print(Deque.items)
# 
# Deque.popright()
# print(Deque.items)
#   
# Deque.popright()
# print(Deque.items)
#   
# 
# Deque.popleft()
# print(Deque.items)
#==============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
