import random

def process_string(s: str) -> dict:
    s_list = list(s)
    random.shuffle(s_list)
    shuffled_string = ''.join(s_list)
    
    non_whitespace_count = sum(1 for char in shuffled_string if not char.isspace())
    
    unique_char_count = len(set(shuffled_string))
    
    return {
        "shuffled_string": shuffled_string,
        "non_whitespace_count": non_whitespace_count,
        "unique_char_count": unique_char_count
    }

# Example usage
if __name__ == "__main__":
    test_string = "Hello World"
    result = process_string(test_string)
    print(f"Shuffled String: {result['shuffled_string']}")
    print(f"Non-whitespace Characters Count: {result['non_whitespace_count']}")
    print(f"Unique Characters Count: {result['unique_char_count']}")
