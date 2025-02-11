 #### 1 Understanding how to create and access elements in a list.

 Ans: 
 **Elements in a list can be accessed using indexing. Python indexes start at 0, so a[0] will access the first element, while negative indexing allows us to access elements from the end of the list. Like index -1 represents the last elements of list.**

 #### 2.  Indexing in lists (positive and negative indexing).

 Ans: 
 **Positive Indexing: Starts from 0 and goes up to n-1 (where n is the length of the sequence). Negative Indexing: Starts from -1 for the last element and goes up to -n for the first element.**

 #### 3. Slicing a list: accessing a range of elements.

Ans:-
**To access a range of elements in a list, you must slice it. One method is to utilize the simple slicing operator, i.e. colon : With this operator, one can define where to begin slicing, and where to terminate slicing, and the step. List slicing creates a new list from an old one.**

#### 4. Understanding list methods like append(), insert(), remove(), pop().

Ans: 
**insert(): Inserts an element at a specified position. pop(): Removes and returns the element at the specified position (or the last element if no index is specified). remove(): Removes the first occurrence of a specified element. reverse(): Reverses the order of the elements in the list.**

#### 5. Iterating over a list using loops.

Ans: 
**Python provides several ways to iterate over list. The simplest and the most common way to iterate over a list is to use a for loop. This method allows us to access each element in the list directly.**

#### 6.  Sorting and reversing a list using sort(), sorted(), and reverse().

Ans: 
**The sort() method arranges the elements of a list in ascending order. For strings, ASCII values are used and uppercase characters come before lowercase characters, leading to unexpected results. ...
The reverse() method reverses the elements in a list.**

#### 7. Basic list manipulations: addition, deletion, updating, and slicing.

Ans:-
**append(): Adds an element to the end of the list.
copy(): Returns a shallow copy of the list.
clear(): Removes all elements from the list.
count(): Returns the number of times a specified element appears in the list.
extend(): Adds elements from another list to the end of the current list.
index(): Returns the index of the first occurrence of a specified element.
insert(): Inserts an element at a specified position.
pop(): Removes and returns the element at the specified position (or the last element if no index is specified).
remove(): Removes the first occurrence of a specified element.
reverse(): Reverses the order of the elements in the list.
sort(): Sorts the list in ascending order (by default).**

#### 8. Introduction to tuples, immutability.

Ans:-
**Immutability: One of the key differences between tuples and other Python data structures is that tuples are immutable. Once a tuple is created, its contents cannot be changed. In contrast, lists and dictionaries are mutable, meaning that their contents can be modified after they are created.**

#### 9. Creating and accessing elements in a tuple

Ans:
**We can access elements in a tuple in the same way as we do in lists and strings. Hence, we can access elements simply by indexing and slicing. Furthermore, the indexing is simple as in lists, starting from the index zero.**

#### 10. Basic operations with tuples: concatenation, repetition, membership.

Ans:
**You can combine two tuples using the + operator. Repetition: You can repeat a tuple using the * operator. Membership Testing: You can check if an element exists in a tuple using the in keyword.**

#### 11. Accessing tuple elements using positive and negative indexing.

Ans:
**To access individual elements within a tuple, you can use indexing. Indexing starts at 0, so the first element of a tuple is at index 0, the second element is at index 1, and so on. You can also use negative indexing to access elements from the end of the tuple.**

#### 12. Slicing a tuple to access ranges of elements.

Ans:
**you can also use slicing to access a range of items in a tuple. The syntax for slicing is tuple[start:stop:step]. start is the index at which the slice starts (inclusive). stop is the index at which the slice ends (exclusive).**

#### 13. Introduction to dictionaries: key-value pairs
Ans:
**A dictionary in Python is created with key-value pairs, where each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces {}. An empty dictionary without any items is written with just two curly braces, like this: {}.**

#### 14. Accessing, adding, updating, and deleting dictionary elements.

Ans: 
**This is the most common method to remove items from a dictionary. pop() takes a key as an input and deletes the corresponding item/element from the Python dictionary. It returns the value associated with the input key.**

#### 15. Dictionary methods like keys(), values(), and items().

Ans:
**clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary**

#### 16. Iterating over a dictionary using loops

Ans:
**Iterate through Python dictionary using build. keys()
Iterate key-value pair using items()
Iterate through all values using . ...
Looping through a dictionary using for loop.
Access a key in Python using zip()
Access key using map() and dict. ...
Access key Using Unpacking of dictionary.**

#### 17. Merging two lists into a dictionary using loops or zip().

Ans:
**zip(a, b) pairs each element from list a with the corresponding element from list b, creating tuples of key-value pairs.
dict() function is used to convert the zipped pairs into a dictionary where elements from a become the keys and elements from b become values.**

#### 18. Counting occurrences of characters in a string using dictionaries.
Ans: 
**Prompt the user to enter a string.
Create an empty dictionary called “dic”.
Iterate through each character in the given string using a for loop.
Check if the character already exists in the “dic” dictionary. ...
If the character is not yet in the dictionary, add it as a new key with a value of 1.**

#### 19. Defining functions in Python.
Ans:
**A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.**
 
 ```def my_function():
  print("Hello from a function")
  ```

#### 20.  Different types of functions: with/without parameters, with/without return values.
Ans:

**Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.**

**Python Function Declaration**

**The syntax to declare a function is:**
![alt text](images/52.png)

**We can define a function in Python, using the def keyword. We can add any type of functionalities and properties to it as we require. By the following example, we can understand how to write a function in Python. In this way we can create Python function definition by using def keyword.**




