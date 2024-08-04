import random

list_of_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

number_1 = random.choice(list_of_numbers)
print('число:', number_1)

n = number_1

code1 = list(range(1, n))
code2 = list(range(1, n))
result = ''

for i in code1:
    for j in code2:
        n1 = i
        n2 = j
        if n1 >= n2:
            continue
        else:
            b = n % (n1 + n2)
            if b == 0:
                result = result + str(n1) + str(n2)

print('подбор кода:', result)
