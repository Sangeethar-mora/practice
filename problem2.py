


print("Current Number 0 Previous Number 0  Sum: 0")
for i in range(11):
    pn = i-1
    sm = (i+(i-1))

    if pn < 0:
        pn, sm = 0,0
        
    print("current number", i, "previous number", pn, "sum:", sm)




