#!/usr/bin/env python
# coding: utf-8

# # Variables and Strings
# 
# 

# In[1]:


# 1.Simple Message: Assign a message to a variable, and then print that message....

msg = " 'Hello Pythonista👋 ,Hope U all r doing well !!👍' "
msg


# In[2]:


# 2.Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following,
# including the quotation marks:


# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

author = "Shakespeare once said,"
quote = " Go Wisely and Slowly ,those who rush Stumble and Fall !!!"
print(author + quote)


# # Calculate Area of a Circle::

# In[9]:


# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Program Console Sample Output 1:
# Input Radius: 0.5
# Area of Circle with radius 0.5 is 0.7853981634

# formula for Area of a Cicle A = pi*(r**2)

pi = 3.14159265359
r = float(input("Enter the value ..."))

Area = pi*r**2
print("Area of Circle is =",Area )


# # Check Number either positive, negative or zero::
# 

# In[14]:


# Write a Python program to check if a number is positive,negative or zero..


n = int(input("Enter the Number : "))

if n == 0:
    print("Zero Entered!")
elif n > 0:
    print("Positive Number Entered!")
else:
    print("Negative Number Entered!")


#  # Vowel Tester

# In[32]:


# Write a Python program to test whether a passed letter is a vowel or not

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


# # BMI Calculator

# In[45]:


# Write a Python program to calculate body mass index Program Console Sample 1:

# Enter Height in Cm: 180

# Enter Weight in Kg: 75

# Your BMI is 23.15

# Formula for the BMI Calculator : BMI = kg/m2.

h = int(input("Enter height in centimetres :"))
h1 = h/100 # To convert height in Metres. 
W = int(input("Enter Weight :"))

BMI = (W / h1**2)
print(BMI)


#  # List:

# In[48]:


# Store the names of a few of your friends in a list called names

# Print each person’s name by accessing each element in the list, one at a time.

Name = ['Neelam','Saba Qamar','Ramma','Simra','Izna','Bharti']
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])
print(Name[5])


# In[50]:


# Start with the list you used in Question 4, but instead of just printing each person’s name,
# print a message to them. The text of each message should be the same, 
# but each message should be personalized with the person’s name.

print(Name)

print(Name[0]," is my loyal friend")
print(Name[1]," is my loyal friend")
print(Name[2]," is my loyal friend")
print(Name[3]," is my loyal friend")
print(Name[4]," is my loyal friend")
print(Name[5]," is my loyal friend")


# In[60]:


# Make a python program that conatains your nine favourite dishes in a list called foods. 
# Print the message, The first three items in the list are:

foods = ['Biryani','BitterGuard','ladyfinger','Beans','Daal','Green peas','Cabbage','Aloo gobi','Curry']
print(foods[0:3])
print(foods[3:6])
print(foods[6:])


# In[64]:


# Start with your program from your last Question8. Make a copy of the list of foods, and call it friend_foods.
# Then, do the following:

print(foods)
# Add a new dish to the original list.

foods.append("Masala Gobi")


# In[66]:


# New List
friend_foods = ['Biryani','BitterGuard','ladyfinger','Beans','Daal','Green peas','Cabbage','Aloo gobi','Curry']

#Add a different dish to the list friend_foods.
friend_foods.append("Dam Aloo")
friend_foods


# In[68]:


# Prove that you have two separate lists
print(foods)
print(friend_foods)


# In[69]:


# Print the message, My favorite pizzas are: and then use a for loop to print the first list.

print('My favorite foods are')
for foods in foods:
    print(foods)


# In[70]:


# Print the message,My friend’s favorite foods are:, and then use a for loop to print the second list.

print('My friend’s favorite foods are:')
for friend_foods in friend_foods:
    print(friend_foods)


# In[ ]:




