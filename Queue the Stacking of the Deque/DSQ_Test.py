import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    # creates starting class attributes for testing
    self.__deque = get_deque(0)
    self.__stack = Stack()
    self.__queue = Queue()

  # prints empty deque
  def test_print_empty_deque(self):
    self.assertEqual('[ ]', str(self.__deque))

  # pops front value off empty deque - doesn't error
  def test_popfront_empty_deque(self):
    self.assertEqual(None, self.__deque.pop_front())

  # pops back value off empty deque - doesn't error
  def test_popback_empty_deque(self):
    self.assertEqual(None, self.__deque.pop_back())

  # peeks front value off empty deque - doesn't error
  def test_peekfront_empty_deque(self):
    self.assertEqual(None, self.__deque.peek_front())

  # peeks back value off empty deque - doesn't error
  def test_peekback_empty_deque(self):
    self.assertEqual(None, self.__deque.peek_back())

  # tests length function on empty deque
  def test_len_empty_deque(self):
    self.assertEqual(0, len(self.__deque))

  # adds variety of values on back and front of deque and tests correct string
  def test_add_front_and_back_deque(self):
    self.__deque.push_front(37)
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back(12)
    self.assertEqual('[ 13, 37, Holla, 12 ]', str(self.__deque))

  # tests length function after several front and back pushes
  def test_len_full_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.assertEqual(5, len(self.__deque))

  # tests front peek of deque after several pushes
  def test_peekfront_full_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.assertEqual(13, self.__deque.peek_front())

  # tests back peek of deque after several pushes
  def test_peekback_full_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.assertEqual('Beast', self.__deque.peek_back())

  # tests front pop return value of deque after several pushes
  def test_popfront_full_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.assertEqual(13, self.__deque.pop_front())

  # tests back pop return value of deque after several pushes
  def test_popback_full_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.assertEqual('Beast', self.__deque.pop_back())

  # tests if deque stores and stringifyies the correct data
  # after several push and pop calls
  # includes popping off empty deque
  def test_pop_and_push_deque(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.peek_front()
    self.__deque.peek_back()
    self.__deque.push_front('Worked Out!')
    self.assertEqual('[ Worked Out! ]', str(self.__deque))

  # tests if full deque has correct length
  # after several push and pop calls
  # includes popping off empty deque
  def test_len_deque_after_push_and_pop(self):
    self.__deque.push_front(13)
    self.__deque.push_back('Holla')
    self.__deque.push_back('Beast')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.__deque.peek_back()
    self.__deque.peek_front()
    self.__deque.push_front('Worked Out!')
    self.__deque.push_back(12)
    self.assertEqual(2, len(self.__deque))

  # STACK TESTING BEGINS

  # prints empty stack
  def test_print_empty_stack(self):
    self.assertEqual('[ ]', str(self.__stack))

  # tests length of empty stack
  def test_len_empty_stack(self):
    self.assertEqual(0, len(self.__stack))

  # returns None when attempting to pop off empty stack
  def test_pop_empty_stack(self):
    self.assertEqual(None, self.__stack.pop())

  # returns None when attempting to peek empty stack
  def test_peek_empty_stack(self):
    self.assertEqual(None, self.__stack.peek())

  # pushes several values on stack, checks for correct string
  def test_push_stack(self):
    self.__stack.push('Yowza')
    self.__stack.push(96)
    self.__stack.push('Ferrari')
    self.assertEqual('[ Ferrari, 96, Yowza ]', str(self.__stack))

  # tests for correct length after several pushes on stack
  def test_len_full_stack(self):
    self.__stack.push('Yowza')
    self.__stack.push(96)
    self.__stack.push('Ferrari')
    self.__stack.push(53)
    self.__stack.push('Cool')
    self.assertEqual(5, len(self.__stack))

  # tests pop returns correct value off stack
  def test_pop_return_stack(self):
    self.__stack.push('Ferrari')
    self.__stack.push(53)
    self.__stack.push('Cool')
    self.__stack.pop()
    self.assertEqual(53, self.__stack.pop())

  # test peek returns correct value off stack
  def test_peek_return_stack(self):
    self.__stack.push('Ferrari')
    self.__stack.push(53)
    self.__stack.push('Cool')
    self.__stack.pop()
    self.assertEqual(53, self.__stack.peek())

  # tests for correct stack value after several pushes, pops and peeks
  # including several pops off empty stack
  def test_pushs_pops_stack(self):
    self.__stack.push('Yowza')
    self.__stack.push(96)
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.peek()
    self.__stack.peek()
    self.__stack.push('Ferrari')
    self.__stack.push(53)
    self.__stack.push('Cool')
    self.__stack.pop()
    self.assertEqual('[ 53, Ferrari ]', str(self.__stack))

  # tests for correct stack length after several pushes, pops and peeks
  # including several pops off empty stack
  def test_length_pushs_pops_stack(self):
    self.__stack.push('Yowza')
    self.__stack.push(96)
    self.__stack.pop()
    self.__stack.peek()
    self.__stack.pop()
    self.__stack.pop()
    self.__stack.push('Ferrari')
    self.__stack.push(53)
    self.__stack.push('Cool')
    self.__stack.pop()
    self.assertEqual(2, len(self.__stack))


  # QUEUE TESTING BEGINS

  # prints empty queue
  def test_print_empty_queue(self):
    self.assertEqual('[ ]', str(self.__queue))

  # returns correct length of empty queue
  def test_len_empty_queue(self):
    self.assertEqual(0, len(self.__queue))

  # pops off empty queue, returns None
  def test_pop_empty_queue(self):
    self.assertEqual(None, self.__queue.dequeue())

  # peeks empty queue, returns None
  def test_peek_empty_queue(self):
    self.assertEqual(None, self.__queue.peek())

  # enqueues several values on queue, tests for correct contents
  def test_enqueue_queue(self):
    self.__queue.enqueue('Yowza')
    self.__queue.enqueue(96)
    self.__queue.enqueue('Ferrari')
    self.assertEqual('[ Yowza, 96, Ferrari ]', str(self.__queue))

  # enqueues several values, checks queue for correct length
  def test_len_full_queue(self):
    self.__queue.enqueue('Yowza')
    self.__queue.enqueue(96)
    self.__queue.enqueue('Ferrari')
    self.__queue.enqueue(53)
    self.__queue.enqueue('Cool')
    self.assertEqual(5, len(self.__queue))

  # tests queue returns correct value when dequeues
  def test_dequeue_return_queue(self):
    self.__queue.enqueue('Ferrari')
    self.__queue.enqueue(53)
    self.__queue.enqueue('Cool')
    self.__queue.dequeue()
    self.assertEqual(53, self.__queue.dequeue())

  # tests queue returns correct value when peeks
  def test_peek_return_queue(self):
    self.__queue.enqueue('Ferrari')
    self.__queue.enqueue(53)
    self.__queue.enqueue('Cool')
    self.__queue.dequeue()
    self.assertEqual(53, self.__queue.peek())

  # enqueues, peeks and dequeues several values, checks for correct contents
  # includes several dequeues of empty queue
  def test_enqueue_dequeue_queue(self):
    self.__queue.enqueue('Yowza')
    self.__queue.enqueue(96)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.peek()
    self.__queue.peek()
    self.__queue.dequeue()
    self.__queue.enqueue('Ferrari')
    self.__queue.enqueue(53)
    self.__queue.enqueue('Cool')
    self.__queue.dequeue()
    self.assertEqual('[ 53, Cool ]', str(self.__queue))

  # enqueues, peeks and dequeues several values, checks for correct length
  # includes several dequeues of empty queue
  def test_length_enqueue_dequeue_queue(self):
    self.__queue.enqueue('Yowza')
    self.__queue.enqueue(96)
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.__queue.peek()
    self.__queue.dequeue()
    self.__queue.enqueue('Ferrari')
    self.__queue.enqueue(53)
    self.__queue.enqueue('Cool')
    self.__queue.dequeue()
    self.assertEqual(2, len(self.__queue))



if __name__ == '__main__':
  unittest.main()

