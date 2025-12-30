from ordered_list import *
from huffman_bit_reader import *
from huffman_bit_writer import *
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __eq__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if not isinstance(other, HuffmanNode):
            return False
        return (self.char == other.char) and (self.freq == other.freq)
    def __lt__(self, other):
        '''Needed in order to be inserted into OrderedList'''
        if self.freq == other.freq:
            return self.char < other.char
        else:
            return self.freq < other.freq

def cnt_freq(filename):
    '''Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file'''
    freq_list = [0] * 256
    try:
        with open(filename, 'r') as f:
            for line in f:
                for char in line:
                    freq_list[ord(char)] += 1
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    return freq_list
def create_huff_tree(char_freq):
    '''Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree'''
    lst = OrderedList()
    empty_freq = [0] * 256
    if char_freq == empty_freq:
        return None
    for i in range(len(char_freq)):
        freq = char_freq[i]
        if freq != 0:
            hnode = HuffmanNode(i, freq)
            lst.add(hnode)
    if lst.size() == 1:
        return lst.remove_by_index(0)
    while lst.size() > 1:
        left = lst.remove_by_index(0)
        right = lst.remove_by_index(0)

        char = min(left.char, right.char)
        new_node = HuffmanNode(char, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        lst.add(new_node)
    return lst.remove_by_index(0)



def create_code(node):
    '''Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location'''
    lst = [''] * 256
    if node is None:
        return lst
    create_code_helper(node, "", lst)
    return lst
def create_code_helper(node, current_code, lst):
    if node.left is None and node.right is None:
        lst[node.char] = current_code
    else:
        if node.left is not None:
            create_code_helper(node.left, current_code + "0", lst)
        if node.right is not None:
            create_code_helper(node.right, current_code + "1", lst)


def create_header(freqs):
    '''Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” '''
    empty_freq = [0] * 256
    header = ""
    if freqs == empty_freq:
        return ''
    for i in range(len(freqs)):
        freq = freqs[i]
        if freq != 0:
            header += str(i) + ' ' + str(freqs[i]) + ' '
    return header[:-1]


def huffman_encode(in_file, out_file):
    '''Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character'''
    with open(in_file, 'r') as inpfile:
        cont = inpfile.read()
        if not cont:
            open(out_file, 'w').close()
            comp_file = out_file.replace('.txt', '_compressed.txt')
            open(comp_file, 'wb').close()
            return
    freq = cnt_freq(in_file)
    huffroot = create_huff_tree(freq)
    codes = create_code(huffroot)
    header = create_header(freq) + '\n'

    with open(out_file, 'w') as outputf:
        outputf.write(header)

        enc = ''.join(codes[ord(char)] for char in cont)
        outputf.write(enc)

    comp_file = out_file.replace('.txt', '_compressed.txt')
    bit_writer = HuffmanBitWriter(comp_file)
    bit_writer.write_str(header)

    for bit in enc:
        bit_writer.write_code(bit)
    bit_writer.close()




def parse_header(header_string):
    freq_list = [0] * 256
    header_list = [int(num) for num in header_string.split()]
    ascii_value = 0
    for i in range(len(header_list)):
        if i % 2 == 0:
            ascii_value = header_list[i]
        elif i % 2 != 0:
            freq_list[ascii_value] = header_list[i]
    return freq_list


def huffman_decode(encoded_file, decode_file):
    try:
        bitread = HuffmanBitReader(encoded_file)
        header = bitread.read_str().strip()
        freq_list = parse_header(header)
        root = create_huff_tree(freq_list)
        with open(decode_file, 'w') as output_file:
            current = root
            count = sum(freq_list)
            for i in range(count):
                while current.right or current.left:
                    bit = bitread.read_bit()
                    if bit is True:
                        current = current.right
                    if bit is False:
                        current = current.left
                output_file.write(chr(current.char))
                current = root
        bitread.close()
    except FileNotFoundError:
        raise FileNotFoundError()

