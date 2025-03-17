


my_string = "pynative"

c=1

for i in my_string:
    if c % 2!=0:
        print(i)
    c=c+1

len_string = len(my_string)

for i in range(len_string):
    if i%2 == 0:
        print(my_string[i])
