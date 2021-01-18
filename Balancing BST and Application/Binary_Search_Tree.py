class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.height = 1
      self.rightNode = None
      self.leftNode = None

  def __init__(self):
    # initializes pointer of empty tree
    self.__root = None

  # private balancing method that treats the current node as a tree root
  # and balances tree if necessary, through calls to helper methods
  def __balance(self, subtreeRootNode):
    # no need to balance if node is empty
    if subtreeRootNode is None:
      return subtreeRootNode
    # calculates balance of current node = right-child-height - left-child-height
    nodeBalance = self.__nodeBalance(subtreeRootNode)
    # if root node is left heavy by 2, requires rotation
    if nodeBalance == -2:
      # calculates balance of left child node
      leftChild_balance = self.__nodeBalance(subtreeRootNode.leftNode)
      # if left child is left heavy or even
      if leftChild_balance <= 0: # -1 or 0
        # call helper method that rotates nodes right, and balances tree
        subtreeRootNode = self.__singleRightRotation(subtreeRootNode)
      # if left child is right heavy
      if leftChild_balance == 1:
        # call helper method that rotates nodes twice, and balances tree
        subtreeRootNode = self.__doubleRightRotation(subtreeRootNode)
    # if root node is right heavy by 2, requires rotation
    if nodeBalance == 2:
      # calculates balance of right child node
      rightChild_balance = self.__nodeBalance(subtreeRootNode.rightNode)
      # if right child is right heavy or even
      if rightChild_balance >= 0:  # 1 or 0
        # call helper method that rotates nodes left, and balances tree
        subtreeRootNode = self.__singleLeftRotation(subtreeRootNode)
      # if left child is left heavy
      if rightChild_balance == -1:
        # call helper method that rotates nodes twice, and balances tree
        subtreeRootNode = self.__doubleLeftRotation(subtreeRootNode)
    # returns the balanced tree node, with heights updated in the helper methods
    return subtreeRootNode

  # helper method that balances tree through doing one right rotation of nodes
  def __singleRightRotation(self, node):
    # updates pointers to rotate nodes
    # updates heights of nodes whose heights may have changed
    newRoot = node.leftNode
    node.leftNode = newRoot.rightNode
    node.height = self.__updated_height(node)
    newRoot.rightNode = node
    newRoot.height = self.__updated_height(newRoot)
    # returns the new root, post-rotation
    return newRoot

  # helper method that balances tree through two rotations
  def __doubleRightRotation(self, node):
    # first left rotation
    node.leftNode = self.__singleLeftRotation(node.leftNode)
    # then right rotation
    newRoot = self.__singleRightRotation(node)
    # returns new root with updated heights
    return newRoot

  # helper method that balances tree through doing one left rotation of nodes
  def __singleLeftRotation(self, node):
    # updates pointers to rotate nodes
    # updates heights of nodes whose heights may have changed
    newRoot = node.rightNode
    node.rightNode = newRoot.leftNode
    node.height = self.__updated_height(node)
    newRoot.leftNode = node
    newRoot.height = self.__updated_height(newRoot)
    # returns the new root, post-rotation
    return newRoot

  # helper method that balances tree through two rotations
  def __doubleLeftRotation(self, node):
    # first right rotation
    node.rightNode = self.__singleRightRotation(node.rightNode)
    # then left rotation
    newRoot = self.__singleLeftRotation(node)
    # returns new root with updated heights
    return newRoot

  # private helper method that calculates the balance of the parameter node
  def __nodeBalance(self, node):
    # a node's balance is the height of its right child - height of its left child
    nodeBalance = 0
    # handles for possible lack of children
    if node.rightNode is not None:
      nodeBalance += node.rightNode.height
    if node.leftNode is not None:
      nodeBalance -= node.leftNode.height
    # returns computed balance for the node
    return nodeBalance

  # recursive helper method for inserting elements into tree
  def __recursive_insert_element(self, newVal, currentNode):
    # in case of adding to empty tree
    # or adding to the last level of a tree
    if currentNode is None:
      return Binary_Search_Tree.__BST_Node(newVal)
    else:
      # if attempting to insert existing value - raise error
      if currentNode.value == newVal:
        raise ValueError
      # if value should go to the left of current Node
      if currentNode.value > newVal:
        # set left to result of recursive call
        currentNode.leftNode = self.__recursive_insert_element(newVal, currentNode.leftNode)
        # updates height if necessary
        if currentNode.leftNode.height == currentNode.height:
          currentNode.height = currentNode.height + 1
      # if value should go to the right of current Node
      if currentNode.value < newVal:
        # sets right node to result of recursive call
        currentNode.rightNode = self.__recursive_insert_element(newVal, currentNode.rightNode)
        # updates height if necessary
        if currentNode.rightNode.height == currentNode.height:
          currentNode.height = currentNode.height + 1
      # returns current balanced Node
      return self.__balance(currentNode)

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.

    # sets root to tree with added element
    self.__root = self.__recursive_insert_element(value, self.__root)

  # helper method that updates the height of parameter node
  def __updated_height(self, node):
    # if node has 2 children
    if node.leftNode is not None and node.rightNode is not None:
      # set height to maximum of childrens' heights + 1
      return max(node.leftNode.height, node.rightNode.height) + 1
    # has only left child
    elif node.leftNode is not None:
      return node.leftNode.height + 1
    # has only right child
    elif node.rightNode is not None:
      return node.rightNode.height + 1
    # node has no children
    else:
      return 1

  # recursive helper method to remove element, accepts value to remove and current Node
  def __recursive_remove_element(self, val, currentNode):
    # element is not in tree
    if currentNode is None:
      raise ValueError
    else:
      # if the value should be to the left of current Node
      if currentNode.value > val:
        # updates left Node to result of remove method calls
        currentNode.leftNode = self.__recursive_remove_element(val, currentNode.leftNode)

      # if the value should be to the right of current Node
      if currentNode.value < val:
        # updates right Node to result of remove method calls
        currentNode.rightNode = self.__recursive_remove_element(val, currentNode.rightNode)

      # if the current element requires removal
      if currentNode.value == val:
        # if element has two children
        if currentNode.rightNode is not None and currentNode.leftNode is not None:
          # iterateNode finds the minimum value greater than the currentNode
          iterateNode = currentNode.rightNode
          while iterateNode.leftNode is not None:
            iterateNode = iterateNode.leftNode
          newValue = iterateNode.value
          # removes minimum value greater than the currentNode, and corrects right Node
          currentNode.rightNode = self.__recursive_remove_element(newValue, currentNode.rightNode)
          # updates value of removed Node
          currentNode.value = newValue

        # if it doesn't have a left child
        elif currentNode.leftNode is None:
          currentNode = currentNode.rightNode

        # if it doesn't have a right child
        else:
          currentNode = currentNode.leftNode
      # updates height of the current Node if necessary
      if currentNode is not None:
        currentNode.height = self.__updated_height(currentNode)
      # returns current balanced Node
      return self.__balance(currentNode)


  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.

    # sets root of tree to result of recursive remove method call
    self.__root = self.__recursive_remove_element(value, self.__root)

  # private, recursive helper method which conducts an in-order traversal
  # and returns a list version of tree
  def __recursive_listify_helper(self, currentNode):
    # if Node is None returns empty list
    if currentNode is None:
      return []
    # otherwise returns a list of left values, current node value, and right values
    currentList = self.__recursive_listify_helper(currentNode.leftNode)
    currentList.append(currentNode.value)
    currentList += self.__recursive_listify_helper(currentNode.rightNode)
    return currentList

  # public method that calls an in-order traversal and returns a list version of the tree
  def to_list(self):
    # return empty list for empty tree
    if self.__root is None:
      return []
    # otherwise return result of helper function
    else:
      return self.__recursive_listify_helper(self.__root)

  # recursive in-order traversal method
  def __recursive_in_order(self, currentNode):
    finalString = ""
    # if Node is None returns empty string
    if currentNode is None:
      return ""
    # otherwise returns a string of left value, current node value, and right value
    finalString += self.__recursive_in_order(currentNode.leftNode)
    finalString += " " + str(currentNode.value) + ","
    finalString += self.__recursive_in_order(currentNode.rightNode)
    return finalString

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # returns for empty trees
    if self.__root is None:
      return "[ ]"
    else:
      # otherwise returns result of recursive in-order traversal, removing superfluous closing comma
      return "[" + self.__recursive_in_order(self.__root)[:-1] + " ]"

  # recursive pre-order traversal method
  def __recursive_pre_order(self, currentNode):
    finalString = ""
    # if Node is None returns empty string
    if currentNode is None:
      return ""
    # otherwise returns a string of parent value, left child value, right child value
    finalString += " " + str(currentNode.value) + ","
    finalString += self.__recursive_pre_order(currentNode.leftNode)
    finalString += self.__recursive_pre_order(currentNode.rightNode)
    return finalString

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # returns for empty trees
    if self.__root is None:
      return "[ ]"
    else:
      # otherwise returns result of recursive pre-order traversal, removing superfluous closing comma
      return "[" + self.__recursive_pre_order(self.__root)[:-1] + " ]"

  # recursive post-order traversal method
  def __recursive_post_order(self, currentNode):
    finalString = ""
    # if Node is None returns empty string
    if currentNode is None:
      return ""
    # otherwise returns a string of left child value, right child value, and then parent value
    finalString += self.__recursive_pre_order(currentNode.leftNode)
    finalString += self.__recursive_pre_order(currentNode.rightNode)
    finalString += " " + str(currentNode.value) + ","
    return finalString

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # returns for empty trees
    if self.__root is None:
      return "[ ]"
    else:
      # otherwise returns result of recursive post-order traversal, removing superfluous closing comma
      return "[" + self.__recursive_post_order(self.__root)[:-1] + " ]"

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # if tree is empty returns height of 0
    if self.__root is None:
      return 0
    else:
      # otherwise returns height of root Node
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.