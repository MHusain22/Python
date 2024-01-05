#wap to find largest element in the array

n = int(input("Enter length of array: ")) 
arr = [] 
print("Enter your array elements: ") 

for i in range(n):     
   a = int(input())   
   arr.append(a) 
   max = arr[0] 

for i in arr:     
     if i>max:          
           max = i 
print(f"Maximum in the array is {max}") 
