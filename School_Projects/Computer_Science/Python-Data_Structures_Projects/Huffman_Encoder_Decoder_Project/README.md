# Huffman Encoder & Decoder (Lossless Text Compression)

This project implements full Huffman Coding which is a lossless compression algorithm
used in real systems such as ZIP files, GIF images, and networking protocols.

The project was completed in two parts:

1. build the encoder  
2. build the decoder and reconstruct compressed files

Everything was implemented from scratch, including tree construction,
bit-level writing/reading, and full unit testing.


## Features Implemented

### Character frequency counting
- Reads file
- Builds frequency table of all 256 ASCII characters

### Huffman Tree construction
- Custom binary tree of HuffmanNode objects
- Nodes ordered by:
  1. frequency
  2. ASCII value (tie-break)

### Code generation
- Traverses the tree recursively
- Generates 0/1 string encoding for each character

### Encoding pipeline
- Builds header
- Encodes file
- Writes compressed output at the **bit level**

### Decoding pipeline
- Reads header
- Reconstructs Huffm
- an tree
- Reads encoded bits
- Walks tree to reconstruct text

---

## Testing

Two full testing suites:

- `huffman_tests.py` — required public tests
- `huffman_helper_tests.py` — complete internal test coverage

Includes edge cases:

✔ empty files  
✔ single-character files  
✔ missing file → raises FileNotFoundError  
✔ newline handling  
✔ compression + decompression match original

---

## Concepts Demonstrated

- Binary Trees
- Priority ordering & comparison overrides
- Recursion
- File I/O
- Bit-level writing/reading
- Algorithms & time complexity
- Exception handling
- Test-driven development (TDD)
