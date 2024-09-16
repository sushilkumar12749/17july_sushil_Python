'''Write a Python function that takes a list of words and returns the length
of the longest one.'''

def longest_word_length(words):
  """Finds the length of the longest word in a list of words.

  Args:
    words: A list of words.

  Returns:
    The length of the longest word in the list.
  """

  longest = 0
  for word in words:
    if len(word) > longest:
      longest = len(word)
  return longest

# Example usage:
word_list = ["hello", "world", "programming"]
result = longest_word_length(word_list)
print(result)  



