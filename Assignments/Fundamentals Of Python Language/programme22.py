'''Write a Python function to insert a string in the middle of a string. '''

def insert_string_middle(main_str, insert_str):
    middle_index = len(main_str) // 2
    return main_str[:middle_index] + insert_str + main_str[middle_index:]

# Example usage:
print(insert_string_middle("hello", "world"))  
print(insert_string_middle("abcd", "xy"))      
