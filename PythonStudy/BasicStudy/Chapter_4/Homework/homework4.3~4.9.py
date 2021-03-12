#练习4-3
for i in range(1,21):
    print(i)


#练习4-4,4-5
numbers = [i for i in range(1,1_000_001)]
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#练习4-6
for i in range(1,21,2):
    print(i)

#练习4-7
number_3 = [value for value in range(3,31) if value % 3 == 0]
print(number_3)

#练习4-8,4-9
numbers_square_3 = [value ** 3 for value in range(1,11)]
for i in range(len(numbers_square_3)):
    print(numbers_square_3[i])