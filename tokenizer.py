"""
Simple Lexical Analyzer (Tokenizer) for a basic programming language.
This module demonstrates tokenization, a fundamental component of compiler design.
"""

import re
from enum import Enum, auto
from typing import List, NamedTuple


class TokenType(Enum):
    """Enumeration of token types supported by the tokenizer."""
    # Keywords
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    RETURN = auto()
    
    # Identifiers and literals
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    
    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    ASSIGN = auto()
    EQUALS = auto()
    NOT_EQUALS = auto()
    LESS_THAN = auto()
    GREATER_THAN = auto()
    
    # Delimiters
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    SEMICOLON = auto()
    COMMA = auto()
    
    # Special
    EOF = auto()
    UNKNOWN = auto()


class Token(NamedTuple):
    """Represents a single token with its type, value, line, and column."""
    type: TokenType
    value: str
    line: int
    column: int


class Tokenizer:
    """
    A simple lexical analyzer that converts source code into tokens.
    """
    
    # Keywords mapping
    KEYWORDS = {
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'while': TokenType.WHILE,
        'return': TokenType.RETURN,
    }
    
    # Token patterns (order matters for matching)
    TOKEN_PATTERNS = [
        (r'[ \t]+', None),  # Whitespace (skip)
        (r'#[^\n]*', None),  # Comments (skip)
        (r'\n', None),  # Newline (skip, but track line number)
        (r'\d+', TokenType.NUMBER),
        (r'"[^"]*"', TokenType.STRING),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', TokenType.IDENTIFIER),
        (r'==', TokenType.EQUALS),
        (r'!=', TokenType.NOT_EQUALS),
        (r'=', TokenType.ASSIGN),
        (r'\+', TokenType.PLUS),
        (r'-', TokenType.MINUS),
        (r'\*', TokenType.MULTIPLY),
        (r'/', TokenType.DIVIDE),
        (r'<', TokenType.LESS_THAN),
        (r'>', TokenType.GREATER_THAN),
        (r'\(', TokenType.LPAREN),
        (r'\)', TokenType.RPAREN),
        (r'\{', TokenType.LBRACE),
        (r'\}', TokenType.RBRACE),
        (r';', TokenType.SEMICOLON),
        (r',', TokenType.COMMA),
    ]
    
    def __init__(self, source_code: str):
        """
        Initialize the tokenizer with source code.
        
        Args:
            source_code: The source code string to tokenize
        """
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """
        Tokenize the entire source code and return a list of tokens.
        
        Returns:
            List of Token objects
        """
        while self.position < len(self.source_code):
            matched = False
            
            for pattern, token_type in self.TOKEN_PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.position)
                
                if match:
                    value = match.group(0)
                    
                    # Handle newlines for line tracking
                    if value == '\n':
                        self.line += 1
                        self.column = 1
                    elif token_type is not None:
                        # Check if identifier is actually a keyword
                        if token_type == TokenType.IDENTIFIER:
                            token_type = self.KEYWORDS.get(value, TokenType.IDENTIFIER)
                        
                        token = Token(token_type, value, self.line, self.column)
                        self.tokens.append(token)
                        self.column += len(value)
                    else:
                        # Skip whitespace and comments
                        self.column += len(value)
                    
                    self.position = match.end()
                    matched = True
                    break
            
            if not matched:
                # Unknown character
                char = self.source_code[self.position]
                token = Token(TokenType.UNKNOWN, char, self.line, self.column)
                self.tokens.append(token)
                self.position += 1
                self.column += 1
        
        # Add EOF token
        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens
    
    def print_tokens(self):
        """Print all tokens in a human-readable format."""
        for token in self.tokens:
            print(f"Line {token.line}, Col {token.column}: {token.type.name:15} '{token.value}'")


def main():
    """Example usage of the tokenizer."""
    sample_code = """
    # Simple program example
    if (x == 10) {
        y = x + 5;
        return y;
    } else {
        while (x < 100) {
            x = x * 2;
        }
    }
    """
    
    tokenizer = Tokenizer(sample_code)
    tokens = tokenizer.tokenize()
    
    print("Tokenization Result:")
    print("=" * 60)
    tokenizer.print_tokens()


if __name__ == "__main__":
    main()
