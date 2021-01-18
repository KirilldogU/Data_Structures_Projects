import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  #  returns True if the delimiters (), [], and {} are balanced and False otherwise.
  # stack that stores delimiters
  delimStack = Stack()
  openingDelimitersList = ['(', '[', '{']
  closingDelimitersList = [')', ']', '}']
  # reads in file and saves string to text var
  f = open(filename, "r")
  text = f.read()
  # reads by characters in text string
  for char in text:
    # pushes opening delimiter onto stack
    if char in openingDelimitersList:
      delimStack.push(char)
    # if closing delimiter
    if char in closingDelimitersList:
      # find matching opening delimiter through arrays
      delimeterIndex = closingDelimitersList.index(char)
      matchingDelimeter = openingDelimitersList[delimeterIndex]
      # if stack doesnt have any delimiters
      if len(delimStack) == 0:
        return False
      # if top delimiter on stack is not the matching one
      if delimStack.peek() != matchingDelimeter:
        return False
      # if matching then remove opening delimiter from  stack
      else:
        delimStack.pop()
  # if stack appropriately empty at end of file then return True
  if len(delimStack) == 0:
    return True
  # if there's extra opening delimiters then return False
  else:
    return False

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


