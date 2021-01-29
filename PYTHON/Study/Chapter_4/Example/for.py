magicians = ['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")


for i in range(1,6):
    print(i)

for j in range(6):
    print(j)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)


print(max(squares))
print(min(squares))
print(sum(numbers))

#列表解析的使用
squares = [value ** 2 for value in range(1,11)]
print(squares)