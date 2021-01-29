#练习4-10
pizzas = ['chicken pizza','onion pizza','beef pizza','durian pizza','mongo pizza','vegetable pizza']
print('The first three items in the list are:')
print(pizzas[0:3])

print('\nThree items from the middle of the list are:')
print(pizzas[2:4])

print('The last three items in the list are:')
print(pizzas[-3:])

#练习4-11
friend_pizzas = pizzas[:]
pizzas.append('turkey pizza')
friend_pizzas.append('sausage pizza')
print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza) 

#练习4-12
#就这？

#练习4-13
pizzas = ('chicken pizza','onion pizza','beef pizza','durian pizza','mongo pizza','vegetable pizza')
for pizza in pizzas:
    print(pizza)

# pizzas[0] = 'shit pizza'

pizzas = ('chicken pizza','fish pizza','seastyle pizza','durian pizza','mongo pizza','vegetable pizza')
for pizza in pizzas:
    print(pizza)