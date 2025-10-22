# CPPro
The repo for the course "Compiler Principle Project".

## Project Overview
This repository contains implementations of fundamental compiler components, starting with a lexical analyzer (tokenizer).

## Components

### Tokenizer (Lexical Analyzer)
A simple lexical analyzer that converts source code into tokens. The tokenizer supports:
- **Keywords**: `if`, `else`, `while`, `return`
- **Operators**: `+`, `-`, `*`, `/`, `=`, `==`, `!=`, `<`, `>`
- **Delimiters**: `(`, `)`, `{`, `}`, `;`, `,`
- **Literals**: Numbers and strings
- **Identifiers**: Variable and function names
- **Comments**: Lines starting with `#`

## Usage

### Running the Tokenizer Example
```bash
python3 tokenizer.py
```

### Running Tests
```bash
python3 -m unittest test_tokenizer.py -v
```

## Example
```python
from tokenizer import Tokenizer

code = """
if (x == 10) {
    y = x + 5;
    return y;
}
"""

tokenizer = Tokenizer(code)
tokens = tokenizer.tokenize()
tokenizer.print_tokens()
```

## Requirements
- Python 3.6+
