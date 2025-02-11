# Write a Python program to remove an empty tuple(s) from a list of tuples.
list=[('Ram','Sita'),(),('Sushil','Sunil'),(12),(3,6,9,7)]
list.remove(())
print(list)