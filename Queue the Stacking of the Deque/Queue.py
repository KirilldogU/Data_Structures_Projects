from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # initializes deque used for queue
    self.__dq = get_deque()

  def __str__(self):
    # returns string version of deque
    return str(self.__dq)

  def __len__(self):
    # returns length through deque returning private string attribute
    return len(self.__dq)

  def enqueue(self, val):
    # pushes to the back of deque to enqueue
    self.__dq.push_back(val)

  def dequeue(self):
    # pops from the front of deque to dequeue, and returns
    return self.__dq.pop_front()

  def peek(self):
    # peeks the front value of the dequeue and returns
    return self.__dq.peek_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass