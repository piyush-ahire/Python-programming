# Guido van Rossum invented in netherlands 1991 interpreted and open source lang, scalable, object oriented 



# no need to declare data type, it will depends on the content in it
# name = "hello"

# A = 10
# a = 5.5

# print(name)
# print(A)
# print(a)

# # to check data type
# print(type(name))



# name = 10.5

# print(type(name)) # <class 'float'>

# #single line string
# a = 'asdsad sadasadas'

# #multiline string
# b = "asada ssadsa\
#     fdfdsfdsfdsfds\
#         dfdsfdsfdsfds"

# # withot \ multiline string
# c='''ffdfdd dfdsfd 
# dfdsfd
# dfdfdsf'''


# # four literals
# #string, numeric, boolean, none

# # string : formed by enclosing a text in it

# s = 4
# d = 6
# print(s<d)



#changing data type from one to another

# a = 10.7
# print(type(a))   # <class 'int'>

# # b = input("Enter: ") # always string *IMP
# # b = int(input("Enter: ")) # always int *IMP
# # print(type(b))

# result = int(a) # type cast
# print(type(result))
# print("Result is: ",result)

# c = 4
# f = 6
# print("Addition is:", c+f)





#if-else maintain indentation

# age = 17
# b = 5

# if age>=18:
#     print("You are eligible for voting")
# else:
#     print("Not eligible")


#relational operator

# a = 4
# b = 4

# print(a == b)


# creation of function
# def abc():
#     print("hello")

# abc()


#logical operator
#and , or , not
# a = 5
# b = a>4 and a>2

# print(b)

# #not
# c = 4
# d = not(c>7)
# print(d)
# print(a!=c)



#in membership operator

# a = ["suresh", "Ramesh"]
# print('Ramesh' in a)


#for loop indentation mandatory
# a = ["suresh", "Ramesh",10]

# for i in a:
#     print(i)


# slicing

# a = "Hello world"
# print(a[2:5])


#python collectors

# List, tuple, dictionary, set

#list - mutable- can change
# list_var = [1,3,6,8,9, "a"]
# print(type(list_var))
# print((list_var))

# #can change using indexing
# list_var[0] = 2
# list_var.append("c")
# print((list_var))

# #tuple
# tup_var = (1,3,6,8,9,"b")
# print(type(tup_var))
# print((tup_var))

#immutable - can't change
# tup_var[0] = 1
# print(tup_var)
# tuple object does not support item assignment, append, edit and update




#set - not ordered, not support item assignment
# stu_marks = {78, 94, 67,1 ,2,4}
# print(type(stu_marks))
# print( (stu_marks))


# #immutable
# # stu_marks[0] = 1
# # print(stu_marks)

# #to add
# stu_marks.add("asd")


#dictionary
# dic_var = {"name":"John", "age":30, "city":"New York"}
# print(type(dic_var))
# print((dic_var))


# # making tuple mutable
# std = ('asd',1,2,3,4)
# print(type(std))
# print("This is tuple",(std))


# a = list(std)
# print(type(a))
# print("This is list",(a))
# a[0] = "sdsf"

# std = tuple(a)
# print(type(std))
# print("This is tuple",(std))

# b = ("asdf",)

# #adding new tuple
# std += b
# print("new tuple :", std)

#unpacking in tuple

# xyz = ("aaer", 1,2,4)

# (a,b,c,*d) = xyz

# print(a)
# print(b)
# print(c)
# print(d)































