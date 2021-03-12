def make_pizza(*toppings):#这里的*让python创建了一个叫做toppings的空元组，并将所有收到的值都装到这个元组中
    print(toppings)


def make_pizzas(size,*toppings):
    print(f'Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")

