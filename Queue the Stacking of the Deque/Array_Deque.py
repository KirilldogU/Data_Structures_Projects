from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    # capacity - maximum amount of data in array without growing
    self.__capacity = 1
    # contents of array - data stored and empty locations
    self.__contents = [None] * self.__capacity
    # front index - frontmost data index, None if size == 0
    self.__frontIndex = None
    # back index - backmost data index, None if size == 0
    self.__backIndex = None
    # size - length of deque, quantity data stored in contents
    self.__size = 0

  def __getArrayValues(self):
    # this is a private helper method used by str() and grow() methods
    # it walks the array from frontIndex to backIndex
    # and returns an array with all the data in correct order
    # performs in O(n)
    if self.__size > 0:
      # array of data with correct length
      valuesStored = [None] * self.__size
      walkIndex = self.__frontIndex # index in contents array
      valIndex = 0 # index in valuesStored array
      # walks through array, storing data to valuesStored
      while walkIndex != self.__backIndex:
        valuesStored[valIndex] = self.__contents[walkIndex]
        valIndex += 1
        walkIndex += 1
        # if walks over the edge of array - rap around to index 0
        if walkIndex == self.__capacity:
          walkIndex = 0
      # stores the last data point
      valuesStored[valIndex] = self.__contents[self.__backIndex]
      # returns all data in deque in array form
      return valuesStored
    else:
      # if the deque is empty return empty list
      return []

  def __str__(self):
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__size == 0:
      # if deque is empty
      return "[ ]"
    else:
      # uses helper method to walk array and get ordered data of deque
      valuesStoredInOrder = self.__getArrayValues()
      # returns contents in correct format
      return "[ " + ", ".join(str(val) for val in valuesStoredInOrder) + " ]"

    
  def __len__(self):
    # returns length in constant time
    return self.__size

  def __grow(self):
    # private method grows the array that stores deque data by *2
    # performs in O(n)
    # uses helper method to walk array and get ordered data of deque
    valuesStoredInOrder = self.__getArrayValues()
    # creates new contents array with deque data in the front
    self.__contents = valuesStoredInOrder + [None] * self.__capacity
    # doubles capacity
    self.__capacity = self.__capacity * 2
    # sets front index to first data index - 0
    self.__frontIndex = 0
    # sets back index to last data index - 0
    self.__backIndex = self.__size - 1

  def push_front(self, val):
    # method pushes to front of the deque
    # grows the array if necessary
    if self.__size == self.__capacity:
      self.__grow()
    # if adding first data point to deque
    if self.__size == 0:
      self.__frontIndex = 0
      self.__backIndex = 0
      self.__contents[0] = val
    # if adding further data
    else:
      self.__frontIndex = self.__frontIndex - 1
      # wraps around to back of array if needed
      if self.__frontIndex == -1:
        self.__frontIndex = self.__capacity - 1
      # stores the data
      self.__contents[self.__frontIndex] = val
    # increases size as needed
    self.__size += 1

  def pop_front(self):
    # method pops from front of the deque
    # returns None if wrongfully attempting to remove from empty deque
    if self.__size == 0:
      return None
    # returns value of deque's only datapoint
    # and sets index attributes to None
    elif self.__size == 1:
      val = self.__contents[self.__frontIndex]
      self.__frontIndex = None
      self.__backIndex = None
      self.__size -= 1
      return val
    else:
      # if size > 1
      # returns val of popped element
      # changes front index to ignore popped data
      val = self.__contents[self.__frontIndex]
      self.__frontIndex = self.__frontIndex + 1
      # wraps index around if necessary
      if self.__frontIndex == self.__capacity:
        self.__frontIndex = 0
      self.__size -= 1
      return val
    
  def peek_front(self):
    # returns None if deque is empty
    if self.__size == 0:
      return None
    else:
      # returns first element value
      return self.__contents[self.__frontIndex]

  def push_back(self, val):
    # adds element to back of deque
    # grows array if necessary
    if self.__size == self.__capacity:
      self.__grow()
    # if adding first element, sets indices appropriately
    if self.__size == 0:
      self.__frontIndex = 0
      self.__backIndex = 0
      self.__contents[0] = val
    else:
      # adds value, and increments backIndex
      self.__backIndex += 1
      # wraps index around array if necessary
      if self.__backIndex == self.__capacity:
        self.__backIndex = 0
      self.__contents[self.__backIndex] = val
    # increases size
    self.__size += 1

  def pop_back(self):
    # pops last element off deque and returns value
    # returns none if deque empty
    if self.__size == 0:
      return None
    # if deque only has one element
    # returns value and changes the indices to point to None
    elif self.__size == 1:
      val = self.__contents[self.__frontIndex]
      self.__frontIndex = None
      self.__backIndex = None
      self.__size -= 1
      return val
    # otherwise returns value of last element
    # and shifts backIndex over to previous element
    else:
      val = self.__contents[self.__backIndex]
      self.__backIndex -= 1
      # wraps around if necessary
      if self.__backIndex == -1:
        self.__backIndex = self.__capacity - 1
      # decreases size
      self.__size -= 1
      return val

  def peek_back(self):
    # returns None if deque is empty
    if self.__size == 0:
      return None
    else:
      # returns value of last element in deque
      return self.__contents[self.__backIndex]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
