''' Write a Python program to count occurrences of a substring in a string.'''

def count_substring_occurrences(main_string, substring):
    count = main_string.count(substring)
    return count

text = "hello world, hello universe"
sub = "hello"

result = count_substring_occurrences(text, sub)
print(f"The substring '{sub}' occurs {result} times in the string.")
