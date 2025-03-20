# Exercise 7: Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
#
# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:
#
# Emma appeared 2 times
str_x = "Emma is good developer. Emma is a writer"

str_list = []

wrd = " "

for i  in str_x:
    if i != " ":
        wrd += i
    if i == " ":
        str_list.append(wrd)
        wrd = " "
str_list.append(wrd)

# print(str_list)

unq_val = []

for i in str_list:
    if i not in unq_val:
        unq_val.append(i)

# print(unq_val)
cnts = []
for i in unq_val:
    c = 0
    for j in str_list:
        if i == j:
            c = c+1
    cnts.append(c)
    # print(i, c)
# print(cnts)

max_cnt = 0

max_index = []

for i in cnts:
    if i is max(cnts):
        max_index.append(max_cnt)
    max_cnt += 1

# print(max_index)

for i in max_index:
    print("word ", unq_val[i], "appeared", cnts[i], "times")
