input_string = input("Enter a string: ")

d = []

for i in input_string:
    if i.isdigit():
        d+=i
if d:
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")

