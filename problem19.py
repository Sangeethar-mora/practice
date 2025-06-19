
prime_num = []

for i in range(2, 20):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)
# print(prime_num)

print("Altarnate prime numbers 1 to 20:")
print(prime_num[::2])


