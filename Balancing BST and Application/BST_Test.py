import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BSTTester(unittest.TestCase):

	def setUp(self):
		# creates starting class attributes for testing
		self.__bst = Binary_Search_Tree()

	def test_print_empty_BST(self):
		self.assertEqual('[ ]', str(self.__bst))

	def test_error_remove_empty_BST(self):
		with self.assertRaises(ValueError):
			self.__bst.remove_element(-12)
		self.assertEqual('[ ]', str(self.__bst))

	def test_print_height_of_empty_BST(self):
		self.assertEqual('0', str(self.__bst.get_height()))

	def test_insert_several_values_BST(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.assertEqual('[ 3, 5, 6, 7 ]', str(self.__bst))

	def test_height_after_insert_several_values_BST(self):
		self.__bst.insert_element(5)
		self.__bst.insert_element(3)
		self.__bst.insert_element(6)
		self.__bst.insert_element(7)
		self.assertEqual('3', str(self.__bst.get_height()))

	def test_height_after_insert_many_values_BST(self):
		self.__bst.insert_element(6)
		self.__bst.insert_element(-9)
		self.__bst.insert_element(0)
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(42)
		self.__bst.insert_element(97)
		self.__bst.insert_element(18)
		self.assertEqual('4', str(self.__bst.get_height()))

	def test_string_after_insert_many_values_BST(self):
		self.__bst.insert_element(6)
		self.__bst.insert_element(-9)
		self.__bst.insert_element(0)
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(42)
		self.__bst.insert_element(97)
		self.__bst.insert_element(18)
		self.assertEqual('[ -9, 0, 2, 6, 13, 18, 42, 97 ]', str(self.__bst))

	def test_error_add_same_value_BST(self):
		self.__bst.insert_element(2)
		self.__bst.insert_element(43)
		self.__bst.insert_element(-6)
		with self.assertRaises(ValueError):
			self.__bst.insert_element(-6)
		self.assertEqual('[ -6, 2, 43 ]', str(self.__bst))

	def test_error_remove_nonexistant_value_BST(self):
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(42)
		self.__bst.insert_element(97)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(-12)
		self.assertEqual('[ 2, 13, 42, 97 ]', str(self.__bst))

	def test_error_remove_too_many_values_(self):
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(42)
		self.__bst.insert_element(97)
		self.__bst.remove_element(97)
		self.__bst.remove_element(2)
		self.__bst.remove_element(42)
		self.__bst.remove_element(13)
		with self.assertRaises(ValueError):
			self.__bst.remove_element(42)
		self.assertEqual('[ ]', str(self.__bst))

	def test_insert_and_remove_several_vals_BST(self):
		self.__bst.insert_element(6)
		self.__bst.insert_element(-9)
		self.__bst.insert_element(0)
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(18)
		self.__bst.insert_element(-2)
		self.__bst.remove_element(6)
		self.__bst.remove_element(2)
		self.__bst.remove_element(-9)
		self.__bst.remove_element(13)
		self.assertEqual('[ -2, 0, 18 ]', str(self.__bst))

	def test_height_after_insert_and_remove_several_vals_BST(self):
		self.__bst.insert_element(6)
		self.__bst.insert_element(-9)
		self.__bst.insert_element(0)
		self.__bst.insert_element(13)
		self.__bst.insert_element(2)
		self.__bst.insert_element(18)
		self.__bst.insert_element(-2)
		self.__bst.remove_element(6)
		self.__bst.remove_element(2)
		self.__bst.remove_element(-9)
		self.__bst.remove_element(13)
		self.assertEqual('2', str(self.__bst.get_height()))

	def test_in_order_traversal_empty_BST(self):
		self.assertEqual('[ ]', str(self.__bst.in_order()))

	def test_post_order_traversal_empty_BST(self):
		self.assertEqual('[ ]', str(self.__bst.post_order()))

	def test_pre_order_traversal_empty_BST(self):
		self.assertEqual('[ ]', str(self.__bst.pre_order()))

	def test_pre_order_traversal_full_BST(self):
		self.__bst.insert_element(42)
		self.__bst.insert_element(17)
		self.__bst.insert_element(63)
		self.__bst.insert_element(13)
		self.__bst.insert_element(52)
		self.__bst.insert_element(87)
		self.assertEqual('[ 42, 17, 13, 63, 52, 87 ]', str(self.__bst.pre_order()))

	def test_post_order_traversal_full_BST(self):
		self.__bst.insert_element(42)
		self.__bst.insert_element(17)
		self.__bst.insert_element(63)
		self.__bst.insert_element(13)
		self.__bst.insert_element(52)
		self.__bst.insert_element(87)
		self.assertEqual('[ 17, 13, 63, 52, 87, 42 ]', str(self.__bst.post_order()))

	def test_in_order_traversal_full_BST(self):
		self.__bst.insert_element(42)
		self.__bst.insert_element(17)
		self.__bst.insert_element(63)
		self.__bst.insert_element(13)
		self.__bst.insert_element(52)
		self.__bst.insert_element(87)
		self.assertEqual('[ 13, 17, 42, 52, 63, 87 ]', str(self.__bst.in_order()))

	def test_print_after_many_inserts_and_removes(self):
		self.__bst.insert_element(97)
		self.__bst.insert_element(102)
		self.__bst.insert_element(-3)
		self.__bst.insert_element(57)
		self.__bst.insert_element(1030)
		self.__bst.insert_element(63)
		self.__bst.remove_element(102)
		self.__bst.remove_element(1030)
		self.__bst.remove_element(63)
		self.__bst.insert_element(-7)
		self.__bst.insert_element(-100)
		self.__bst.insert_element(230)
		self.assertEqual('[ -100, -7, -3, 57, 97, 230 ]', str(self.__bst))

	def test_height_after_many_inserts_and_removes(self):
		self.__bst.insert_element(97)
		self.__bst.insert_element(102)
		self.__bst.insert_element(-3)
		self.__bst.insert_element(57)
		self.__bst.insert_element(1030)
		self.__bst.insert_element(63)
		self.__bst.remove_element(102)
		self.__bst.remove_element(1030)
		self.__bst.remove_element(63)
		self.__bst.insert_element(-7)
		self.__bst.insert_element(-100)
		self.__bst.insert_element(230)
		self.assertEqual('3', str(self.__bst.get_height()))

	def test_post_order_traversal_after_many_inserts_and_removes(self):
		self.__bst.insert_element(97)
		self.__bst.insert_element(102)
		self.__bst.insert_element(-3)
		self.__bst.insert_element(57)
		self.__bst.insert_element(1030)
		self.__bst.insert_element(63)
		self.__bst.remove_element(102)
		self.__bst.remove_element(1030)
		self.__bst.remove_element(63)
		self.__bst.insert_element(-7)
		self.__bst.insert_element(-100)
		self.__bst.insert_element(230)
		self.assertEqual('[ -7, -100, -3, 97, 230, 57 ]', str(self.__bst.post_order()))

	def test_pre_order_traversal_after_many_inserts_and_removes(self):
		self.__bst.insert_element(97)
		self.__bst.insert_element(102)
		self.__bst.insert_element(-3)
		self.__bst.insert_element(57)
		self.__bst.insert_element(1030)
		self.__bst.insert_element(63)
		self.__bst.remove_element(102)
		self.__bst.remove_element(1030)
		self.__bst.remove_element(63)
		self.__bst.insert_element(-7)
		self.__bst.insert_element(-100)
		self.__bst.insert_element(230)
		self.assertEqual('[ 57, -7, -100, -3, 97, 230 ]', str(self.__bst.pre_order()))

	def test_single_Right_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(-4)
		self.__bst.insert_element(-12)
		self.assertEqual('[ -4, -12, 0 ]', str(self.__bst.pre_order()))

	def test_height_single_Right_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(-4)
		self.__bst.insert_element(-12)
		self.assertEqual('2', str(self.__bst.get_height()))

	def test_single_Left_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(46)
		self.__bst.insert_element(-93)
		self.assertEqual('[ 0, -93, 46 ]', str(self.__bst.pre_order()))

	def test_height_single_Left_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(46)
		self.__bst.insert_element(93)
		self.assertEqual('2', str(self.__bst.get_height()))

	def test_double_Right_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(-12)
		self.__bst.insert_element(-3)
		self.assertEqual('[ -3, -12, 0 ]', str(self.__bst.pre_order()))

	def test_height_double_Right_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(-12)
		self.__bst.insert_element(-3)
		self.assertEqual('2', str(self.__bst.get_height()))

	def test_double_Left_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(7)
		self.__bst.insert_element(1)
		self.assertEqual('[ 1, 0, 7 ]', str(self.__bst.pre_order()))

	def test_height_double_Left_Rotation_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(7)
		self.__bst.insert_element(1)
		self.assertEqual('2', str(self.__bst.get_height()))

	def test_to_list_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(7)
		self.__bst.insert_element(1)
		self.assertEqual('[0, 1, 7]', str(self.__bst.to_list()))

	def test_full_to_list_BST(self):
		self.__bst.insert_element(0)
		self.__bst.insert_element(7)
		self.__bst.insert_element(12)
		self.__bst.insert_element(-2)
		self.__bst.insert_element(-67)
		self.__bst.insert_element(1)
		self.assertEqual('[-67, -2, 0, 1, 7, 12]', str(self.__bst.to_list()))

	def test_empty_to_list_BST(self):
		self.assertEqual('[]', str(self.__bst.to_list()))

if __name__ == '__main__':
	unittest.main()
