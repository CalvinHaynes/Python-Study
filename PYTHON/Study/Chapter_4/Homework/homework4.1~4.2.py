
#练习4-1
pizzas = ['chicken pizza','onion pizza','beef pizza','durian pizza']

for pizza in pizzas:
    print(f'I like {pizza}.\n')

print('I really love pizza!\n')

#练习4-2
animals = ['magpie','sparrow','crow','dodo']
for animal in animals:
    print(f'A {animal} would make a great pet.\n')

print('Any of these animals would make a great pet!')


print(pizzas[:3])
print(pizzas[-3:])
print(pizzas[1:3])
print(pizzas[1:3])
print(pizzas[:-3])
print(pizzas[:])

#复制列表操作
friend_pizzas = pizzas[:]
pizzas.append('vegetable pizza')
friend_pizzas.append('mongo pizza')
print(pizzas)
print(friend_pizzas)