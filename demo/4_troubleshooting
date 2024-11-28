def first_non_repeating_char(s: str) -> str:
    """
    Find the first non-repeating character in a given string.

    :param s: The input string.
    :return: The first non-repeating character.
    """
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 2:
            return char
    
    return ""

# Example usage
if __name__ == "__main__":
    test_string = "aabbccdde"
    print(first_non_repeating_char(test_string))  # Expected output: "e"
