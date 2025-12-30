import unittest
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)
        with self.assertRaises(FileNotFoundError):
            cnt_freq("filenotexistent")
        empty_freq = cnt_freq("empty_file.txt")
        self.assertEqual(empty_freq, [0] * 256)
        single_char_freq = cnt_freq("single_char.txt")
        self.assertEqual(single_char_freq[ord('a')], 5)
        self.assertEqual(sum(single_char_freq), 5)

        
    def test_lt_and_eq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertFalse(HuffmanNode(97, 2) == None)
                    
                    
    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
        empty_freq = cnt_freq("empty_file.txt")
        empty_tree = create_huff_tree(empty_freq)
        self.assertIsNone(empty_tree)
        single_char_tree = create_huff_tree([5] + [0] * 255)
        self.assertEqual(single_char_tree.char, 0)
        self.assertEqual(single_char_tree.freq, 5)
        self.assertIsNone(single_char_tree.left)
        self.assertIsNone(single_char_tree.right)
        
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
        empty_freq = cnt_freq("empty_file.txt")
        single_char_freq = cnt_freq("single_char.txt")
        self.assertEqual(create_header(single_char_freq), "97 5")
        self.assertEqual(create_header(empty_freq), '')

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
        self.assertEqual(codes[ord('z')], '')
        empty_freq = cnt_freq("empty_file.txt")
        empty_tree = create_huff_tree(empty_freq)
        empty_codes = create_code(empty_tree)
        self.assertEqual(empty_codes, [''] * 256)
        single_char_freq = cnt_freq("single_char.txt")
        single_char_tree = create_huff_tree(single_char_freq)
        single_char_codes = create_code(single_char_tree)
        self.assertEqual(single_char_codes[ord('a')], '')

        
    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        self.assertEqual(subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True), 0)
        self.assertEqual(subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell = True), 0)


    def test_empty_file(self):
        huffman_encode("empty_file.txt", "empty_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        self.assertEqual(subprocess.call("diff -wb empty_out.txt empty_file.txt", shell=True), 0)
        self.assertEqual(subprocess.call("diff -wb empty_out_compressed.txt empty_file.txt", shell=True), 0)

    def test_01a_test_file1_parse_header(self):
        f = HuffmanBitReader('file1_compressed_soln.txt')
        header = f.read_str()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_parse_header(self):
        header = "97 3 98 4 99 2"
        freqlist = [0] * 256
        freqlist[97] = 3
        freqlist[98] = 4
        freqlist[99] = 2
        result = parse_header(header)
        self.assertEqual(result, freqlist)

    def test_parse_header_empty(self):
        header = ""
        freqlist = [0] * 256
        result = parse_header(header)
        self.assertEqual(result, freqlist)

    def test_parse_header_single_char(self):
        header = "100 5"
        freqlist = [0] * 256
        freqlist[100] = 5
        result = parse_header(header)
        self.assertEqual(result, freqlist)

    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_empty_file_decode(self):
        huffman_decode("empty_file.txt", "empty_file_decoded.txt")
        err = subprocess.call("diff -wb empty_file.txt empty_file_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_no_file_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("nofile.txt", "decoded.txt")

    def test_one_char_file_decode(self):
        huffman_decode("single_char_compressed_soln.txt", "single_char_decoded.txt")
        err = subprocess.call("diff -wb single_char.txt single_char_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)



if __name__ == '__main__': 
   unittest.main()
