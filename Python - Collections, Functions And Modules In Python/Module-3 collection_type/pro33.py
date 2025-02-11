# Write a Python script to concatenate following dictionaries to create a new one.
dict1={'name':'sushil','l_name':'kumar','city':'rajkot'}
dict2={'std':7,'rno.':31}
dict3={ }
for i in (dict1,dict2):
    dict3.update(i)
print(dict3)
