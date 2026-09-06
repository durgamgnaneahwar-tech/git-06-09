# -------------------------------------------------------------------------------------------------------------------------------------------------

# Interview-Style Programming Questions: Loops, Strings, and Number Operations
# 1. Print Numbers from 1 to n
# Question: Write a program to print numbers from 1 to n. Explanation:
#  Use a loop starting from 1 to n and print each number. - Input: n = 5 - Output: 1 2 3 4 5

# n=5
# for i in range(1,n+1,1):
#     print(i)


# m=100
# n=159
# for i in range(m,n+1):
#     if i%4==0:
#         print(i)

# n=5
# res=0
# for i in range(1,n+1):
#         res+=1
#         print(res)

# 2. Print Numbers from m to n
# Question: Write a program to print numbers from m to n. Explanation: 
# Loop from m to n and print values. - Input: m = 3, n = 7 - Output: 3 4 5 6 7

# m=3
# n=7
# for i in range(m,n+1,1):
#     print(i)


# 3. Print Numbers from n to 1 in Reverse
# Question: Write a program to print numbers in reverse from n to 1. Explanation: 
# Use a loop starting from n and decrement to 1. - Input: n = 5 - Output: 5 4 3 2 1

# n=5
# for i in range(n,1-1,-1):
#     print(i)


# 4. Print Numbers from n to m in Reverse
# Question: Write a program to print numbers from n to m in reverse. Explanation: 
# Start from n and go down to m. - Input: n = 10, m = 6 - Output: 10 9 8 7 6

# n=10
# m=6
# for i in range(n,m-1,-1):
#     print(i)


# 5. Sum of n Natural Numbers
# Question: Write a program to calculate the sum of first n natural numbers. Explanation:
#  Use formula or loop to sum from 1 to n. - Input: n = 5 - Output: 15

# n=5
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(sum)

# 6. Factorial of a Number
# Question: Write a program to find the factorial of a number. 
# Explanation: Multiply all numbers from 1 to n. - Input: n = 5 - Output: 120

# n=5
# factorial=1
# for i in range(1,n+1):
#     factorial=factorial*i
# print(factorial)

# n=15
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# 7. Sum of m to n Numbers
# Question: Write a program to find the sum of all numbers from m to n. Explanation: 
# Loop from m to n and add values. - Input: m = 3, n = 6 - Output: 18

# m=3
# n=6
# total=0
# for i in range(m,n+1):
#     total+=i
# print(total)

# n=65
# total=0
# for i in range(1,n+1):
#     total+=i
# print(total)

# n=15
# sum=0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# 8. Product of m to n Numbers
# Question: Write a program to find the product of numbers from m to n. Explanation: 
# Loop from m to n and multiply values. - Input: m = 2, n = 4 - Output: 24

# m=2
# n=4
# product=1
# for i in range(m,n+1):
#     product*=i
# print(product)


# 9. Print Factors of a Number
# Question: Write a program to print all factors of a given number. 
# Explanation: Check divisibility of number from 1 to n. - Input: n = 6 - Output: 1 2 3 6

# n=6
# fact=0
# for i in range(1,n+1):
#     if n%i==0:
#      fact+=1
#      print(i)
# print(fact)


# 10. Count of Factors
# Question: Write a program to count how many factors a number has. Explanation: 
# Increment count when divisible. - Input: n = 6 - Output: 4

# n=6
# count=0
# for i in range(1,n+1):
#    if n%i==0:
#       count+=1
# print(count)



# 11. Prime Number Check
# Question: Check if a number is prime. Explanation: 
# A number is prime if it has exactly 2 factors. - Input: n = 7 - Output: Prime

# n=7
# prime=0
# for i in range(1,n+1):
#     if n%i!=2 or n%i!=3:
#         prime+=1
# print(i)


# n=7
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime num")
# else:
#     print("not prime")


# # n=100
# for i in range(1,100):
#     count=0
#     for j in range(1,n+1):
#         if i%j==0 :
#             count+=1
#     if count==2:
#         print(i)



# 12. Even Numbers from m to n
# Question: Print all even numbers between m and n. Explanation: 
# Use loop and check if divisible by 2. - Input: m = 3, n = 10 - Output: 4 6 8 10

# m=3
# n=10
# for i in range(m,n+1):
#     if i%2==0:
#         print(i)


# 13. Odd Numbers from m to n
# Question: Print all odd numbers between m and n. Explanation: 
# Check if number % 2 != 0. - Input: m = 3, n = 10 - Output: 3 5 7 9

# m=3
# n=10
# for i in range(m,n+1):
#     if i%2!=0:
#         print(i)

# 14. Count of Even and Odd Numbers
# Question: Count how many even and odd numbers are in the range m to n. Explanation:
# Use counters for even and odd. - Input: m = 3, n = 7 - Output: Even = 2, Odd = 3

# m=3
# n=7
# count=1
# for i in range(m,n+1):
#     if i%2==0:
#         count+=1
#         if i%2!=0:
#                 count+=1
#                 print(count,"odd")
#         print(count,"even")


# m=3
# n=7
# even_count=0
# odd_count=0
# for i in range()



# 15. Reverse a String
# Question: Reverse a given string. Explanation: 
# Use slicing or loop. - Input: “hello” - Output: “olleh”

# s="hello"
# for i in s:
#     i=s[::-1]
# print(i)
   

# 16. Check for Palindrome String
# Question: Check if a string is a palindrome. Explanation: 
# Compare string with its reverse. - Input: “madam” - Output: Palindrome

# s="madam"
# for i in s:
#    if s == s[::-1]:
#       res="palindrom"
# print(res)
      
# s="malayalam"
# for i in s:
#     if s==s[::-1] :
#         res="palindrome"
#     else:
#         res="not palindrome"
#     print(res)   



# 17. Sum of Digits
# Question: Calculate the sum of digits of a number. Explanation: 
# Use loop and % 10 to extract digits. - Input: 123 - Output: 6

# n=123
# st=str(n)
# sum=0
# for i in st:
#     sum+=int(i)
# print(sum)


# n=123
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit
#     temp=temp//10
# print(sum)



# ________________________________________
# 18. Product of Digits
# Question: Calculate the product of digits. Explanation: 
# Multiply digits extracted from number. - Input: 123 - Output: 6

# n=123
# st=str(n)
# product=1
# for i in n:
#     product=product*i
#     print(product)


# n=123
# st=str(n)
# product=1
# for i in st:
#     product*=int(i)
# print(product)

# n=123
# temp=n
# product=1
# while temp>0:
#     digit=temp%10
#     product*=digit
#     temp=temp//10
# print(product)

# ________________________________________
# 19. Armstrong Number Check
# Question: Check if a number is an Armstrong number. Explanation: 
# Sum of cube of digits equals the number. - Input: 153 - Output: Armstrong number

# n = 153
# st = str(n)
# l = len(st)
# sum = 0
# for i in st:
#     sum += int(i) ** l
# if n == sum:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")



# n=153
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp=temp//10
# if sum==n:
#     print("armstrong")
# else:
#     print("not")        



# ________________________________________
# 20. Reverse a Number
# Question: Reverse the digits of a number. Explanation: 
# Use loop with % and // to reverse. - Input: 123 - Output: 321


# n=123
# temp=n
# reverse=0
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# print(reverse)




# ________________________________________
# 21. Palindrome Number Check
# Question: Check if a number is a palindrome. Explanation: 
# Compare number with its reverse. - Input: 121 - Output: Palindrome

# n=121
# n=str(n)
# for i in n:
#     if n[::-1]==n:
#        res="palindrome"
# print(res)

# n=121
# temp=n
# reverse=0
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# print(reverse)
# if n==reverse:
#     print("palindrome")
# else:
#     print("not palindrome")


# ________________________________________
# 22. Count Vowels in String
# Question: Count number of vowels in a string. Explanation: 
# Loop and check for a, e, i, o, u. - Input: “apple” - Output: 2

# w="apple"
# count=0
# for i in w:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)

# string="apple"
# count=0
# vowels="aeiouAEIOU"
# i=0
# while string<0:


# ________________________________________
# 23. Count Consonants in String
# Question: Count consonants in a string. Explanation: 
# Check for alphabetic characters not vowels. - Input: “apple” - Output: 3

# word="apple"
# count=0
# for i in word:
#     if i not in "aeiouAEOIU":
#         count+=1
# print(count)

# w="apple"
# count = 0
# i = 0
# while i < len(w):
#     if w[i] not in "aeiouAEIOU":
#         count += 1
#     i += 1
# print(count)

# ________________________________________
# 24. Count Vowels and Consonants
# Question: Count vowels and consonants in input string. Explanation: 
# Maintain two counters. - Input: “apple” - Output: Vowels = 2, Consonants = 3

# word="apple"
# v_count=0
# c_count=0
# for i in word:
#     if i in "aeiouAEIOU":
#         v_count+=1
#     else:
#         c_count+=1
# print(v_count)
# print(c_count)

# ________________________________________
# 25. Perfect Number Check
# Question: Check if a number is perfect. Explanation: 
# Sum of proper divisors equals the number. - Input: 28 - Output: Perfect number

# num=28
# count=0
# sum=0
# for i in range(1,28):
#     if num%i==0:
#         sum+=i
# if num==sum:
#     print("perfect num")
# else:
#     print("not perfect")

# ________________________________________
# 26. Neon Number Check
# Question: Check if a number is a neon number. Explanation:
# Square the number, sum digits, match original. - Input: 9 - Output: Neon number




    

# ________________________________________
# 27. Strong Number Check
# Question: Check if a number is a strong number. Explanation:
# Sum of factorial of digits equals the number. - Input: 145 - Output: Strong number

# num = 145
# sum = 0
# for i in str(num):
#     digit = int(i)
#     fact = 1
#     for j in range(1, digit + 1):
#         fact *= j
#     sum += fact
# if sum == num:
#     print("Strong number")
# else:
#     print("Not a Strong number")


# ________________________________________
# 28. Harshad Number Check
# Question: Check if a number is divisible by the sum of its digits. 
# Explanation: Calculate digit sum and check divisibility. - Input: 18 - Output: Harshad number

# n=int(input("enter a number: "))
# sum=0
# original=n
# while(n>0):
#     c=n%10
#     sum+=c
#     n=n//10
#     if original%sum==0:
#         print(f"{original} is an harshad number")

# n=10
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum+=digit
#     temp=temp//10
# if n%sum==0:
#     print("harshad number")
# else:
#     print("not")


# ________________________________________
# 29. Fibonacci Series
# Question: Print the Fibonacci series up to n terms. Explanation:
# Start with 0, 1 and continue with sum of last two. - Input: n = 5 - Output: 0 1 1 2 3

# n=5
# a=0
# b=1
# a,b=b,a+b
# for i in range(0,n):
#     a,b=b,a+b
#     print(a,b)



# ________________________________________
# 30. Check for Neon Number (Repeated)
# Question: Again, check for a neon number (example). Explanation:
# Square number and sum digits. - Input: 9 - Output: Neon number




# n=123
# st=str(n)
# sum=0
# product=1
# for i in st:
#     sum+=int(i)
#     product*=int(i)
# print(product)
# print(sum)
# if sum==product:
#     print("spy")


# n=100
# for i in range(0,n+1):
#     if n%2==0 and n%3==0:
#      print(i)

