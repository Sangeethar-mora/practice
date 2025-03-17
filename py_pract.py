# print("welcome", end = "")
# print("to ireland")
# print("14","March","2025", sep = "-")
# #python also know as identifier
# price = 100
# tax = 18
# total_price = price + tax
# print(total_price)
#
# x = 10
# y = "red"
# z = 20
# w = z
# w = 30
# print(x)
# print(y)
# print(z)
# print(w)
# # python is Dynamically Typed
#
# x = 10
# print(x)
# x = "geeks"
# print(x)
#
# #name = input("enter the name:-")
# #print("welcome",name)
#
# #Ex_2
# #input() always gives us a string so whenever we need mathmatical expressions we need to convert it from string.
#
# #x = input("Enter First number")
# #y = input("Enter second number")
# #x = int(x)
# #y = int(y)
# #result = x+y
# #print("sum is:-",result)
#
# #type() in python
#
# a = 10
# print(type(a))
# b = 10.5
# print(type(b))
# c = 2+3j
# print(type(c))

# str = "fukka"      #sting is a sequence of char
# print(type(str))
#
# j = [10,20,30]     #items are stored in continous location
# print(type(j))
#
# j = (10,20,30)    #tuple can't be modify once created,these are immutable
# print(type(j))
#
# s = {10,20,30}   #set is a collection of items ,it is like mathematical set
# print(type(s))
#
# d = {10:"fukka",20:"id"} #dictionaries are used to do mappings this is a collection of key:value pairs
# print(type(d))

#type conversions
# # implicit
# a = 10
# b = 1.5
# c = a + b
# print(c)
#
# d =False
# e = a + d
# print(e)
#
# # Explicit
# s = "135"
# i = 1+int(s)
# f = float(s)
# print(i)
# print(f)
#
# s = "geeks"
# print(list(s))
# print(tuple(s))
# print(set(s))
#
# a = 20
# print(bin(a))
# print(hex(a))
# print(oct(a))
cost = 60
dic = 10
percentage = 60 - (cost*dic/100)
print(percentage)



print("10 % discount for employee")
cost = int(input("enter the cost of the product"))
discount = 10
total_price = cost - (cost*discount/100)
print(total_price,end = "€")

