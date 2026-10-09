def replace_character(s: str, oldChar: str, newChar: str) -> str:
    """
    Replaces all occurrences of oldChar with newChar in the input string s.
    """
    return s.replace(oldChar, newChar)

# --- Example Usage ---
print(replace_character("banana", 'a', 'x'))       # Output: "bxnxnx"
print(replace_character("hello", 'l', 'p'))        # Output: "heppo"
print(replace_character("programming", 'm', 'x'))  # Output: "prograxxing"