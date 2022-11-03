#!/usr/bin/env python
# coding: utf-8

# # Identity Operators
# 
# 
# 
# 

# ## Q1

# ◯ An identity can be changed once created.
# 
# ◯ Two strings with same value point to different locations.
# 
# ⦿ id(object) is unique and Constant for an object during its lifetime.

# ## Q2

# In[ ]:


x=int(input("Enter an integer: "))
y=int(input("Enter the same integer: "))
print("x is y",x is y)
print("x is not y",x is not y)
a=float(input("Enter a Float Number: "))
b=float(input("Enter the same Number: "))
print("x is y",a is b)
print("x is not y",a is not b)


# ## Q3

# In[ ]:


x=int(input("x: "))
y=int(input("y: "))
print("{} is {}".format(x,y),x is y)


# ## Q4

# In[ ]:


x=int(input("x: "))
y=int(input("y: "))
print("{} is {}".format(x,y),x is not y)


# # Operators Precedence
# 

# ## Q1

# ✅ Operator precedence is performed based on priority of an operator.
# 
# ✅ Associativity is used when two operators of same precedence are in the same expression.
# 
# ◻ Associativity is only from Left to Right .
# 
# ◻ The operator precedence is only used on Arithmetic operators.

# ## Q2
No Any Question.
# ## Q3

# In[ ]:


a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("{} + {} * 5 =".format(a,b),a+b*5)
print("{} + {} * 6 / 2 =".format(a,b),a+b*6/2)


# ## Q4

# In[ ]:


a=int(input("Enter an integer value: "))
b=int(input("Enter an integer value: "))
print("{} + {} * 5 =".format(a,b),a+b*5)
print("{} + {} * 5 * 10 / 2 =".format(a,b),a+b*5*10/2)


# ## Q5

# In[ ]:


a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print("a and b or c".format(a,b,c),a and b or c)
print("a or b and c".format(a,b,c),a or b and c)


# ## Q6

# In[ ]:


a=int(input("Enter an integer value: "))
b=int(input("Enter an integer value: "))
c=int(input("Enter an integer value: "))
print("{} and {} and {} or {} is".format(a,b,c,a),a and b and c or a)
print("{} or {} and {} and {} is".format(a,b,c,a),a or b and c and a)

