# n=int(input("Enter the number of terms : "))
# n1,n2=0,1
# if(n<=0):
#     print("Enter positive number")
# elif(n==1):
#     print(f"Fibonacci series is {n}")
# else:
#     print(n1)
#     print(n2)
#     for i in range(0,n-1):
#         n=n1 + n2
#         n1=n2
#         n2=n
#         print(n)



# number = int(input("Enter any number: "))

# # prime number is always greater than 1
# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             print(number, "is not a prime number")
#             break
#     else:
#         print(number, "is a prime number")

# # if the entered number is less than or equal to 1
# # then it is not prime number
# else:
#     print(number, "is not a prime number")   



# def swap(x,y):
#     temp = x
#     x = y
#     y = temp

#     print(f"after wapping num1={x} and num2={y}")

# n1=int(input("Enter num1\n"))
# n2=int(input("Enter num2\n"))
# swap(n1,n2)



# n=int(input("enter hte length of array :"))
# arr=[]
# print("Enter your array elements :")
# for i in range(n):
#     a=int(input())
#     arr.append(a)        #to add another element
# for i in range(n):
#     print(arr)
#     break
     
# max=arr[0]
# for i in arr:
#     if(i>max):
#         max=i
# print(f"max array :{max}")




# n = int(input("Enter number of names you want to enter: "))
# names = []
# print("Enter names")
# for i in range(n):
#     nme = input()
#     names.append(nme)
# names.sort()
# print(f"Sorted names list {names}")






# def arraySum(arr):
#     sum= 0
#     for i in arr:
#         sum = sum + i
#     return sum
# n = int(input("Enter no. of elements: "))
# arr = []
# print("Enter numbers: ")
# for i in range(n):
#     arr.append(int(input()))
# sum= arraySum(arr)
# print("Sum of entire array:",sum)

  



# num = int(input("Enter a number: "))

# # initialize sum
# sum = 0

# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10

# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")






# n = int(input("Enter a number: "))

# for i in range(n):
#     i=i+1
#     print(2**(i))


# value= input("Enter data")

# try:
#     num=int(value)
# except:
#     print("Wrong data entered ")
#     num=-1
# print(num)



# import os
# fhand=open("hi.txt","r")
# print(fhand.read())
# count=0
# for line in fhand:
#     count=count+1
# print("line count",count)
# fhand.close()
# os.rename('hi.txt','bye.txt')

n=input("Enter n : ")

for i in range(0,n):
    for j in range(0,n):
        if(i==1 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ")
    print(end="/n")
