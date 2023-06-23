"""unit test for the linked_list module"""
import unittest
from linked_list import create_linked_list


class TestLinkedList(unittest.TestCase):
    """test all the functions of the linked_list.py"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.linked_list = None

    def setUp(self):
        self.linked_list = create_linked_list()

    def test_head_1(self):
        """tests if the head is None if empty"""
        self.assertIsNone(self.linked_list["get_head"]())

    def test_head_2(self):
        """tests if the head is not None if filled"""
        self.linked_list["append"]("Erstens")
        self.assertIsNotNone(self.linked_list["get_head"]())

    def test_append_1(self):
        """tests in a linked list with one node if append and get_head works"""
        test_value = "Erstens"
        self.linked_list["append"](test_value)
        self.assertEqual(test_value, self.linked_list["get_head"]().value)

    def test_append_2(self):
        """tests in a linked list with two nodes if append and get_head work"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.assertEqual(test_value_1, self.linked_list["get_head"]().value)

    def test_prepend_1(self):
        """tests in a linked list with one node if prepend works"""
        test_value = "Erstens"
        self.linked_list["prepend"](test_value)
        self.assertEqual(test_value, self.linked_list["get_head"]().value)

    def test_prepend_2(self):
        """tests in a linked list with two nodes i prepend works"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"

        self.linked_list["prepend"](test_value_1)
        self.linked_list["prepend"](test_value_2)
        self.assertEqual(test_value_2, self.linked_list["get_head"]().value)

    def test_get_tail_1(self):
        """test get_tail with an empty list"""
        self.assertIsNone(self.linked_list["get_tail"]())

    def test_get_tail_2(self):
        """test get_tail with an list with one node"""
        test_value = "Erstens"
        self.linked_list["append"](test_value)
        self.assertEqual(test_value, self.linked_list["get_tail"]().value)

    def test_get_tail_3(self):
        """test get_tail with an list with two nodes"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.assertEqual(test_value_2, self.linked_list["get_tail"]().value)

    def test_get_size_1(self):
        """test get_size with an empty list"""
        self.assertEqual(0, self.linked_list["get_size"]())

    def test_get_size_2(self):
        """test get_size with an list with two nodes"""
        self.linked_list["append"]("Erstens")
        self.assertEqual(1, self.linked_list["get_size"]())

    def test_get_size_3(self):
        """test get_size with an list with two nodes"""
        self.linked_list["append"]("Erstens")
        self.linked_list["append"]("Zweitens")
        self.assertEqual(2, self.linked_list["get_size"]())

    def test_at_index_1(self):
        """test at_index with an empty list"""
        self.assertIsNone(self.linked_list["at_index"]("Erstens"))

    def test_at_index_2(self):
        """test at_index with an list containing one node"""
        test_value_1 = "Erstens"

        self.linked_list["append"](test_value_1)
        self.assertEqual(test_value_1, self.linked_list["at_index"](0).value)

    def test_at_index_3(self):
        """test at_index with an list containing three node"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"
        test_value_3 = "Drittens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.linked_list["append"](test_value_3)

        self.assertEqual(test_value_1, self.linked_list["at_index"](0).value)
        self.assertEqual(test_value_2, self.linked_list["at_index"](1).value)
        self.assertEqual(test_value_3, self.linked_list["at_index"](2).value)

    def test_pop_1(self):
        """test pop with an list containing three node"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"
        test_value_3 = "Drittens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.linked_list["append"](test_value_3)

        self.assertEqual(test_value_3, self.linked_list["pop"]().value)
        self.assertEqual(test_value_2, self.linked_list["pop"]().value)
        self.assertEqual(test_value_1, self.linked_list["pop"]().value)
        self.assertIsNone(self.linked_list["pop"]())

    def test_contains_1(self):
        """test contains with an list containing three node"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"
        test_value_3 = "Drittens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.linked_list["append"](test_value_3)

        self.assertTrue(self.linked_list["contains"](test_value_1))
        self.assertTrue(self.linked_list["contains"](test_value_2))
        self.assertTrue(self.linked_list["contains"](test_value_3))
        self.assertFalse(self.linked_list["contains"]("Not in List"))

    def test_find_1(self):
        """test find with an list containing three node"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"
        test_value_3 = "Drittens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.linked_list["append"](test_value_3)

        self.assertEqual(0, self.linked_list["find"](test_value_1))
        self.assertEqual(1, self.linked_list["find"](test_value_2))
        self.assertEqual(2, self.linked_list["find"](test_value_3))
        self.assertIsNone(self.linked_list["find"]("Not in List"))

    def test_to_string_1(self):
        """test to_string with an list containing three node"""
        test_value_1 = "Erstens"
        test_value_2 = "Zweitens"
        test_value_3 = "Drittens"

        self.linked_list["append"](test_value_1)
        self.linked_list["append"](test_value_2)
        self.linked_list["append"](test_value_3)

        self.assertEqual(f"head -> ({test_value_1}) -> ({test_value_2}) -> ({test_value_3}) -> null", self.linked_list["to_string"]())
    
    def test_to_string_2(self):
        """test to_string with an list containing three node"""

        self.assertEqual("head -> null", self.linked_list["to_string"]())

if __name__ == "__main__":
    unittest.main()
