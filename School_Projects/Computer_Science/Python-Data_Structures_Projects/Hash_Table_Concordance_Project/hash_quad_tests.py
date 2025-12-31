import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0) 
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash        
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)
        ht.insert("cat", 10)
        self.assertEqual(ht.get_value("cat"), 10)
        self.assertEqual(ht.get_num_items(), 1)

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("dog", 7)
        self.assertFalse(ht.in_table("mouse"))
        self.assertIsNone(ht.get_value("mouse"))

    def test_05(self):
        ht = HashTable(3)
        keys = ["a", "b", "c"]
        values = [1, 2, 3]
        for k, v in zip(keys, values):
            ht.insert(k, v)
        self.assertGreater(ht.get_table_size(), 3)
        for k, v in zip(keys, values):
            self.assertTrue(ht.in_table(k))
            self.assertEqual(ht.get_value(k), v)

    def test_06(self):
        ht = HashTable(7)
        self.assertFalse(ht.in_table("cat"))
        self.assertIsNone(ht.get_value("cat"))
        self.assertEqual(ht.get_num_items(), 0)
        self.assertEqual(ht.get_all_keys(), [])

    def test_07(self):
        ht = HashTable(7)
        ht.insert("a", 1)
        ht.insert("h", 2)
        ht.insert("o", 3)
        self.assertEqual(ht.get_value("a"), 1)
        self.assertEqual(ht.get_value("h"), 2)
        self.assertEqual(ht.get_value("o"), 3)

    def test_08(self):
        ht = HashTable(0)
        self.assertEqual(ht.get_table_size(), 2)
        ht = HashTable(-5)
        self.assertEqual(ht.get_table_size(), 2)

    def test_09(self):
        ht = HashTable(7)
        self.assertEqual(ht.next_prime(4), 5)
        ht = HashTable(7)
        self.assertEqual(ht.next_prime(9), 11)
        ht = HashTable(7)
        # self.assertEqual(ht.next_prime(11), 11)
        # ht = HashTable(7)
        self.assertEqual(ht.next_prime(8), 11)
        ht = HashTable(7)
        self.assertEqual(ht.next_prime(25), 29)

    def test_10(self):
        ht = HashTable(7)
        ht.insert("apple", "fruit")
        ht.insert("pleap", "fruit")
        self.assertTrue(ht.in_table("apple"))
        self.assertTrue(ht.in_table("pleap"))

    def test_11(self):
        ht = HashTable(5)
        ht.insert("key1", "value1")
        ht.insert("key2", "value2")
        ht.insert("key3", "value3")
        ht.insert("key4", "value4")
        self.assertTrue(ht.in_table("key1"))
        self.assertTrue(ht.in_table("key2"))
        self.assertTrue(ht.in_table("key3"))
        self.assertTrue(ht.in_table("key4"))

    def test_12(self):
        ht = HashTable(7)
        ht.insert("apple", "fruit")
        result = ht.get_index("banana")
        self.assertIsNone(result)

    def test_13(self):
        ht = HashTable(5)
        ht.insert("apple", "fruit")
        ht.insert("pleap", "fruit")
        result = ht.get_index("orange")
        self.assertIsNone(result)

    def test_14(self):
        ht = HashTable(7)
        ht.insert("theawesomeman", "fruit")
        ht.insert("theawesomeapple", "fruit")
        self.assertTrue(ht.in_table("theawesomeman"))
        self.assertTrue(ht.in_table("theawesomeapple"))


if __name__ == '__main__':
   unittest.main()
