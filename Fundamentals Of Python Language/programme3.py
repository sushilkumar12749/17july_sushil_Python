#Write a Python program to get the Fibonacci series of given range.

num = int(input("Enter Your any Number :"))
n1,n2 = 0,1

sum = 0
if num<=0:
    print('please Enetr number greater tahen 0')
else:
    for i in range(0,num):
        print(sum, end="")
        n1 = n2
        n2 = sum
        sum = n1+n2
