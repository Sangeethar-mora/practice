tax_emp = int(input("entr the income:- "))
tax1 = 10000 * (0/100)
# print(tax1)
tax2 = 10000 * (10/100)
# print(tax2)
tax3 = (tax_emp - 20000) * (20/100)
print("tax payable is:- ",tax3 + tax2 + tax1, end = "$")

