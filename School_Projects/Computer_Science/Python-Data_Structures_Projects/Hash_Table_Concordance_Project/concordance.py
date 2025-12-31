from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        ''' Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError'''
        self.stop_table = HashTable(191)
        try:
            with open(filename, 'r') as f:
                n = 1
                for line in f:
                    self.stop_table.insert(line.strip().lower(), n)
                    n += 1
        except FileNotFoundError:
            raise FileNotFoundError


    def load_concordance(self, filename):
        ''' Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        (The stop words hash table could possibly be None.)
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError'''
        self.concordance_table = HashTable(191)
        try:
            with open(filename, 'r') as f:
                line_number = 1
                for line in f:
                    words_final = []
                    line = line.replace("'", "")
                    line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
                    tokens = line.split()
                    for word in tokens:
                        if word.isalpha():
                            words_final.append(word)
                    visted_words = set()
                    for word in words_final:
                        word = word.lower()
                        if self.stop_table.in_table(word) is False:
                            lines = self.concordance_table.get_value(word)
                            if lines is not None:
                                if word not in visted_words:
                                    lines.append(line_number)
                                    self.concordance_table.insert(word, lines)
                            else:
                                self.concordance_table.insert(word, [line_number])
                            visted_words.add(word)
                    line_number += 1

        except FileNotFoundError:
            raise FileNotFoundError

    def write_concordance(self, filename):
        ''' Write the concordance entries to the output file(filename)
        See sample output files for format.'''
        with open(filename, 'w') as out_f:
            words = self.concordance_table.get_all_keys()
            words_sorted = sorted(words)
            for word in words_sorted:
                lines = self.concordance_table.get_value(word)
                line_numbers = " ".join(map(str, lines))
                out_f.write(f"{word}: {line_numbers}\n")