# Evaluating Expressions Using Stacks (Data Structures Project)

This project implements an expression evaluator that works across **prefix, infix, and postfix**
representations by converting everything into postfix (Reverse Polish Notation) and evaluating it
using a Stack Abstract Data Type.

This mimics what real-world compilers and interpreters do like converting expressions into a form
that is easier for machines to execute.

## Data Structures & Concepts Used

- Stack ADT (custom implementation)
- Algorithmic parsing
- Operator precedence
- Exception handling
- Unit testing with unittest
- Modular program design


---

## Error Handling & Custom Exceptions

The evaluator detects invalid expressions and raises descriptive errors:

- `Empty input`
- `Invalid token`
- `Insufficient operands`
- `Too many operands`
- `Illegal bit shift operand`
- division by zero → `ValueError`

---

## Testing

All major functions are fully unit-tested to ensure:

- correct outputs
- correct exceptions
- branch/edge case coverage

---

## Skills Demonstrated

- Abstract Data Types
- Stack implementation
- Expression parsing algorithms
- Shunting-yard algorithm
- Prefix / Postfix conversion
- Python exception handling
- Writing meaningful unit tests
- Reading and extending specifications
