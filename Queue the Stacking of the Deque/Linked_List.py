class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the public attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.value = val
      self.next = None
      self.prev = None
      #Node object is originated with value, and no neighbours

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    #initializes sentinal nodes with value of None
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    #returns attribute maintained in other methods
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    #appends element through using trailer pointer as reference
    #increases size
    newNode = Linked_List.__Node(val)
    previousLastNode = self.__trailer.prev #tail Node
    newNode.next = self.__trailer
    newNode.prev = previousLastNode
    previousLastNode.next = newNode
    self.__trailer.prev = newNode
    self.__size += 1

  def __frontWalk(self, index):
    # walks to an index from the head
    # returns Node at the index
    # helper function used by insert and remove
    curNode = self.__header
    # iterates to correct index
    for currentIndex in range(0, index+1):
      curNode = curNode.next
    return curNode

  def __backWalk(self, index):
    # walks backwards to an index from the tail
    # returns Node at the index
    # helper function used by insert and remove
    curNode = self.__trailer
    # iterates to correct index
    for currentIndex in range(0, self.__size-index):
      curNode = curNode.prev
    return curNode

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    #raises Error if index is invalid for insertion
    #either less than 0, or >= list length
    if (index >= self.__size) or (index < 0):
      raise IndexError
    else:
      #otherwise
      #creates new Node
      newNode = Linked_List.__Node(val)
      # locates index at which to add
      # either starts at front or back
      if index <= self.__size/2:
        curNode = self.__frontWalk(index)
      else:
        curNode = self.__backWalk(index)
      #uses current node at index reference to insert Node
      newNode.prev = curNode.prev
      newNode.next = curNode
      curNode.prev.next = newNode
      curNode.prev = newNode
      #increases length of list
      self.__size += 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    # raises error if index is invalid
    if (index >= self.__size) or (index < 0):
      raise IndexError
    else:
      # locates node from closer side - head or tail
      # curNode is node at index
      if index <= self.__size/2:
        curNode = self.__frontWalk(index)
      else:
        curNode = self.__backWalk(index)
      # removes element through changing pointers
      # of neighbouring Nodes
      curNode.prev.next = curNode.next
      curNode.next.prev = curNode.prev
      #decreases length attribute of list
      self.__size  -= 1
      #returns value of removed element
      return curNode.value

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    # raises error if index is invalid
    if (index >= self.__size) or (index < 0):
      raise IndexError
    else:
      curNode = self.__header
      #iterates to correct location from closer side
      if index <= self.__size/2:
        curNode = self.__frontWalk(index)
      else:
        curNode = self.__backWalk(index)
      #returns value of element
      return curNode.value

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    #try statement will prevent removing from empty list
    #prevents method from erroring out in case of failure
    if self.__size > 1:
      # rotation is needed
      lastNode = self.__trailer.prev
      firstNode = self.__header.next
      # rotates through changing pointers
      self.__header.next = firstNode.next
      firstNode.next.prev = self.__header
      lastNode.next = firstNode
      self.__trailer.prev = firstNode
      firstNode.prev = lastNode
      firstNode.next = self.__trailer

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    # list of values of correct size
    valueList = [None] * self.__size
    #iterates through Linked List storing Node values
    curNode = self.__header
    for index in range(0, self.__size):
      curNode = curNode.next
      valueList[index] = str(curNode.value)
    #returns correct spacing for empty list
    if len(valueList) == 0:
      return "[ ]"
    else:
      #attaches proper spacing to edge of list
      return "[ " + ", ".join(valueList) + " ]"

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    #creates attribute used for iteration
    self.__iterAttribute = self.__header
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    # checks if at last node
    if self.__iterAttribute.next is self.__trailer:
      raise StopIteration
    else:
      # moves to next node
      self.__iterAttribute = self.__iterAttribute.next
      return self.__iterAttribute.value

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests

  LinkedListTest = Linked_List()
  print("Empty List: " +str(LinkedListTest))
  print("Length of List: " + str(len(LinkedListTest)))

  try:
    LinkedListTest.get_element_at(0)   # IndexError
  except:
    print("Correctly caught getting element of empty list.")
  try:
    LinkedListTest.remove_element_at(-5)  # IndexError
  except:
    print("Correctly caught removing element at negative index.")

  try:
    #should not crash
    print('Variety of correct insertions and appends:')
    LinkedListTest.append_element(17)
    LinkedListTest.append_element(46)
    LinkedListTest.insert_element_at(12, 1)
    LinkedListTest.insert_element_at(56, 0)
    LinkedListTest.append_element(-200)
    print("List: " + str(LinkedListTest))
    print("Length of List: " + str(len(LinkedListTest)))
  except:
    print('Unexpected error!')

  try:
    print(LinkedListTest.get_element_at(5)) # IndexError
  except:
    print("Correctly caught getting element of out of bounds index")

  try:
    print(LinkedListTest.get_element_at(-2)) #IndexError
  except:
    print("Correctly caught getting element of out of negative index")

  try:
    print("Fourth Element = " + str(LinkedListTest.get_element_at(3)))
  except:
    print('Unexpected error!')

  try:
    print("List after two rotate left calls:")
    LinkedListTest.rotate_left()
    LinkedListTest.rotate_left()
    print(LinkedListTest)
  except:
    print('Unexpected error!')

  try:
    print("Iteration Through List:")
    for val in LinkedListTest:
      print(val)
  except:
    print('Unexpected error!')

  try:
    print("Removed element from index 2: " +
      str(LinkedListTest.remove_element_at(2)))
    print("List: " + str(LinkedListTest))
    print("Length of List: " + str(len(LinkedListTest)))
  except:
    print('Unexpected error!')

  try:
    LinkedListTest.insert_element_at(68, 4)
  except:
    print("Error after attempting to insert element at index len(list)")

  try:
    LinkedListTest.insert_element_at(68, -1)
  except:
    print("Error after attempting to insert element at negative index")

  print("List: " + str(LinkedListTest))
  print("Length of List: " + str(len(LinkedListTest)))

  try:
    print("Remove all elements in a loop:")
    for index in range(len(LinkedListTest)):
      print(LinkedListTest.remove_element_at(0))
  except:
    print("Unexpected error")

  print("List: " + str(LinkedListTest))
  print("Length of List: " + str(len(LinkedListTest)))

  try:
    print("Rotates empty list")
    LinkedListTest.rotate_left()
  except:
    print("Correctly had error rotating empty list")

  try:
    for val in (LinkedListTest):
      print(val)
    print("Succesful Iteration through empty Linked List!")
  except:
    print("Unexpected error")

