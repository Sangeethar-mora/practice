str_x = "Emma is good developer. Emma is a writer"
str_lis = []
wrd = ""
for i in str_x:
    if i == " ":
        str_lis.append(wrd)
        wrd = ""
    if i != ".":
        wrd = wrd+i
    str_lis.append(wrd)
     print(str_lis)
