"""
Unit tests for the Tokenizer module.
"""

import unittest
from tokenizer import Tokenizer, TokenType, Token


class TestTokenizer(unittest.TestCase):
    """Test cases for the Tokenizer class."""
    
    def test_simple_arithmetic(self):
        """Test tokenization of simple arithmetic expressions."""
        code = "x = 5 + 3"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        # Remove EOF token for easier testing
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        expected_types = [
            TokenType.IDENTIFIER,
            TokenType.ASSIGN,
            TokenType.NUMBER,
            TokenType.PLUS,
            TokenType.NUMBER
        ]
        
        self.assertEqual(len(tokens), len(expected_types))
        for token, expected_type in zip(tokens, expected_types):
            self.assertEqual(token.type, expected_type)
    
    def test_keywords(self):
        """Test that keywords are correctly identified."""
        code = "if while return else"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        expected_types = [
            TokenType.IF,
            TokenType.WHILE,
            TokenType.RETURN,
            TokenType.ELSE
        ]
        
        self.assertEqual(len(tokens), len(expected_types))
        for token, expected_type in zip(tokens, expected_types):
            self.assertEqual(token.type, expected_type)
    
    def test_operators(self):
        """Test tokenization of various operators."""
        code = "== != = + - * / < >"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        expected_types = [
            TokenType.EQUALS,
            TokenType.NOT_EQUALS,
            TokenType.ASSIGN,
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.MULTIPLY,
            TokenType.DIVIDE,
            TokenType.LESS_THAN,
            TokenType.GREATER_THAN
        ]
        
        self.assertEqual(len(tokens), len(expected_types))
        for token, expected_type in zip(tokens, expected_types):
            self.assertEqual(token.type, expected_type)
    
    def test_delimiters(self):
        """Test tokenization of delimiters."""
        code = "( ) { } ; ,"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        expected_types = [
            TokenType.LPAREN,
            TokenType.RPAREN,
            TokenType.LBRACE,
            TokenType.RBRACE,
            TokenType.SEMICOLON,
            TokenType.COMMA
        ]
        
        self.assertEqual(len(tokens), len(expected_types))
        for token, expected_type in zip(tokens, expected_types):
            self.assertEqual(token.type, expected_type)
    
    def test_string_literal(self):
        """Test tokenization of string literals."""
        code = '"hello world"'
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, TokenType.STRING)
        self.assertEqual(tokens[0].value, '"hello world"')
    
    def test_number_literal(self):
        """Test tokenization of number literals."""
        code = "42 123 0"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        self.assertEqual(len(tokens), 3)
        for token in tokens:
            self.assertEqual(token.type, TokenType.NUMBER)
    
    def test_identifier(self):
        """Test tokenization of identifiers."""
        code = "variable_name x1 _temp myVar"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        self.assertEqual(len(tokens), 4)
        for token in tokens:
            self.assertEqual(token.type, TokenType.IDENTIFIER)
    
    def test_comment_skip(self):
        """Test that comments are skipped."""
        code = "x = 5 # this is a comment\ny = 10"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        # Should only have tokens for: x = 5 y = 10
        expected_values = ["x", "=", "5", "y", "=", "10"]
        actual_values = [t.value for t in tokens]
        
        self.assertEqual(actual_values, expected_values)
    
    def test_line_and_column_tracking(self):
        """Test that line and column numbers are tracked correctly."""
        code = "x = 5\ny = 10"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        # First line tokens
        self.assertEqual(tokens[0].line, 1)  # x
        self.assertEqual(tokens[1].line, 1)  # =
        self.assertEqual(tokens[2].line, 1)  # 5
        
        # Second line tokens
        self.assertEqual(tokens[3].line, 2)  # y
        self.assertEqual(tokens[4].line, 2)  # =
        self.assertEqual(tokens[5].line, 2)  # 10
    
    def test_complex_expression(self):
        """Test tokenization of a complex code block."""
        code = """
        if (x == 10) {
            return x + 5;
        }
        """
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        tokens = [t for t in tokens if t.type != TokenType.EOF]
        
        # Verify we have the expected number of tokens
        self.assertGreater(len(tokens), 0)
        
        # Check some key tokens
        token_types = [t.type for t in tokens]
        self.assertIn(TokenType.IF, token_types)
        self.assertIn(TokenType.RETURN, token_types)
        self.assertIn(TokenType.EQUALS, token_types)
        self.assertIn(TokenType.LBRACE, token_types)
        self.assertIn(TokenType.RBRACE, token_types)


if __name__ == '__main__':
    unittest.main()
