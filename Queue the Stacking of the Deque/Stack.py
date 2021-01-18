from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    # initializes deque used for stack
    self.__dq = get_deque(0)

  def __str__(self):
    # returns string version of deque
    return str(self.__dq)

  def __len__(self):
    # returns length through deque returning private string attribute
    return len(self.__dq)

  def push(self, val):
    # pushes to the front of deque to push stack
    self.__dq.push_front(val)

  def pop(self):
    # pops from the front of deque to pop stack, and returns
    return self.__dq.pop_front()

  def peek(self):
    # peeks the front value of the deque and returns
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
