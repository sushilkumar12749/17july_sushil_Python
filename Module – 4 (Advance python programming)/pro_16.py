Can one block of except statements handle multiple exception? 

Ans-> Yes, you can handle multiple execution in a single except block in python.

try:
    result=10/0
except(zerodivisionError, ValueError) as e:
    print("An error occured:",e)