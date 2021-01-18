from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)

  # DO NOT CHANGE ANYTHING ABOVE THIS LINE

  def push_front(self, val):
    # if deque is empty appends to linked list
    if len(self.__list) == 0:
      self.__list.append_element(val)
    # otherwise inserts into the first index
    else:
      self.__list.insert_element_at(val, 0)

  def pop_front(self):
    # if deque isn't empty
    # removes and returns first element
    if len(self.__list) > 0:
      return self.__list.remove_element_at(0)
    # otherwise - returns None
    else:
      return None

  def peek_front(self):
    # if deque isn't empty
    # returns value of first element
    if len(self.__list) > 0:
      return self.__list.get_element_at(0)
    # if deque is empty - returns None
    else:
      return None

  def push_back(self, val):
    # appends an element to the end of the deque
    self.__list.append_element(val)


  def pop_back(self):
    # if deque isn't empty
    # removes last element and returns its value
    if len(self.__list) > 0:
      lastvalpopped = self.__list.remove_element_at(len(self.__list)-1)
      return lastvalpopped
    # if deque is empty - returns None
    else:
      return None

  def peek_back(self):
    # if deque isn't empty
    # returns value of last element
    if len(self.__list) > 0:
      lastval = self.__list.get_element_at(len(self.__list) - 1)
      return lastval
    # if deque is empty - returns None
    else:
      return None

# Unit tests make the main section unneccessary.
# if __name__ == '__main__':
#  pass