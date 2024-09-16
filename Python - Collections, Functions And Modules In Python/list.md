### 1. What is List? How will you reverse a list?
ANS:-
A list is a collection of items (also called elements) in a specific order. You can store different types of data in a list, like numbers, strings, or even other lists. In Python, a list is written with square brackets [] and the items are separated by commas.

```
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) 
```

### 2. How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?  
 
 ANS:-
 To remove the last object from a list, you can use the pop() method. This method removes and returns the last item from the list.

```
list1 = [2, 33, 222, 14, 25]
list1.pop(4)  # This will remove the last item (25) from the list
print(list1) 
```
### 3. Differentiate between append () and extend () methods?

Ans:-
---In Python, both append() and extend() are used to add elements to a list, but they work in different ways.

**``1. append() Method:``**
What it does: Adds a single element to the end of the list.
How it works: If you append a list or any other data type, it is added as a single item (the whole list is treated as one element).

```
list1 = [1, 2, 3]
list1.append(4)  # Adds the number 4 as a single element
print(list1)  # Output: [1, 2, 3, 4]

list1.append([5, 6])  # Adds the list [5, 6] as a single element
print(list1)  # Output: [1, 2, 3, 4, [5, 6]]
```

**``2. extend() Method:``**
What it does: Adds each element of an iterable (like a list or a string) to the end of the list, extending the list.
How it works: If you extend a list with another list, the elements of the second list are added individually to the first list.

```
list1 = [1, 2, 3]
list1.extend([4, 5])  # Adds each element of the list [4, 5] to list1
print(list1)  # Output: [1, 2, 3, 4, 5]
```

### 4.  Write a Python function to get the largest number, smallest num and sum
of all from a list.
Ans:-
```
numbers = [3, 8, 1, 10, 5]

largest, smallest, total_sum = list_statistics(numbers)

print("Largest number:", largest)      # Output: 10
print("Smallest number:", smallest)    # Output: 1
print("Sum of all numbers:", total_sum) # Output: 27
```
### 5. How will you compare two lists? 
Ans:-
**``1. Compare if Two Lists Are Equal:``**
If you want to check if two lists have the same elements in the same order, you can use the equality operator ==.
```
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2)  # Output: True (because both lists have the same elements in the same order)
print(list1 == list3)  # Output: False (because the order of elements is different)

```

### 6. Write a Python program to remove duplicates from a list.

Ans:-
```
def remove_duplicates(input_list):
    return list(set(input_list))

# Example usage:
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)

```
The function remove_duplicates(input_list) takes a list as input.
It converts the list into a set using set(input_list), which automatically removes duplicates because sets do not allow duplicate values.
The set is then converted back to a list using list().
The function returns this list of unique elements.

### 7. Write a Python program to check a list is empty or not.

Ans:-
```
def check_list_empty(my_list):
    if not my_list:
        return "The list is empty."
    else:
        return "The list is not empty."
```





