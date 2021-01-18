from Binary_Search_Tree import Binary_Search_Tree

class Fraction:

  def __init__(self, numerator, denominator):
    # use caution here... In most languages, it is not a good idea to
    # raise an exception from a constructor. Python is a bit different
    # and it shouldn't cause a problem here.
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    # returns True if self fraction is less than other and
    # False otherwise.
    # uses cross multiplication properties to calculate
    first_product = self.__n * other.__d
    second_product = self.__d * other.__n
    if first_product < second_product:
      # fraction is less than other
      return True
    # else
    return False

  def __gt__(self, other):
    # returning True if self is greater than other and
    # False otherwise.
    # uses cross multiplication properties to calculate
    first_product = self.__n * other.__d
    second_product = self.__d * other.__n
    if first_product > second_product:
      # fraction is greater than other
      return True
    # else
    return False

  def __eq__(self, other):
    # returning True if self equal to other and
    # False otherwise. Note that fractions are
    # stored in reduced form.
    # uses cross multiplication properties
    first_product = self.__n * other.__d
    second_product = self.__d * other.__n
    if first_product == second_product:
      # fractions are equal
      return True
    # else
    return False

  def to_float(self):
    #this is safe because we don't allow a
    #zero denominator
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  # the __repr__ method is similar to __str__, but is called
  # when Python wants to display these objects in a container like
  # a Python list.
  def __repr__(self):
    return str(self)

if __name__ == '__main__':
  # creates a bunch of fraction objects and stores them in an array.
  # Then inserts each item from the array into a balanced BST.
  # Then gets the in-order array representation of the BST using
  # the to_list() method
  # prints the original and in-order traversal arrays to show that
  # the fractions have been sorted.

  originialFractionArray = []
  originialFractionArray.append(Fraction(3, 4))
  originialFractionArray.append(Fraction(1, 3))
  originialFractionArray.append(Fraction(2, 7))
  originialFractionArray.append(Fraction(4, 3))
  originialFractionArray.append(Fraction(100, 9))
  originialFractionArray.append(Fraction(5, 6))
  originialFractionArray.append(Fraction(2, 9))
  originialFractionArray.append(Fraction(10, 11))
  originialFractionArray.append(Fraction(6, 5))
  originialFractionArray.append(Fraction(1, 2))

  print("Unsorted Fraction Array:")
  print(originialFractionArray)
  bal_BST = Binary_Search_Tree()
  for fraction in originialFractionArray:
    bal_BST.insert_element(fraction)
  sortedList = bal_BST.to_list()
  print("Fraction Array after BST Sorting:")
  print(sortedList)