import re

class TokenValidator:
    # Define sets for keywords, operators, and delimiters
    keywords = {"int", "float", "struct", "if", "else", "while", "cin", "cout"}
    operators = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="}
    delimiters = {";", ",", "{", "}", "(", ")"}

    # Regular expressions for identifiers and numbers
    identifier_pattern = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
    number_pattern = re.compile(r"^\d+$")

    @classmethod
    def is_valid_token(cls, token):
        # Check if token is a keyword
        if token in cls.keywords:
            print(f"{token} is a valid keyword.")
            return True

        # Check if token is an operator
        if token in cls.operators:
            print(f"{token} is a valid operator.")
            return True

        # Check if token is a delimiter
        if token in cls.delimiters:
            print(f"{token} is a valid delimiter.")
            return True

        # Check if token is an identifier
        if cls.identifier_pattern.match(token):
            print(f"{token} is a valid identifier.")
            return True

        # Check if token is a number
        if cls.number_pattern.match(token):
            print(f"{token} is a valid number.")
            return True

        # If none of the above, token is invalid
        print(f"{token} is not a valid token.")
        return False

# Example usage
token = input("Enter a token to verify: ")
TokenValidator.is_valid_token(token)