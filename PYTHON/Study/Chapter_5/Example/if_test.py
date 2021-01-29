#python在检查是否相等时是区分大小写的

#如果比较过程中大小写无关紧要应先都转换为小写再比较

print('True and True is: ',True and True)

print('True and False is: ',True and False)

print('False and False is: ',False and False)

print('True or True is: ',True or True)

print('True or False is: ',True or False)

print('False or False is: ',False or False)

pizzas = ['chicken pizza','onion pizza','beef pizza','durian pizza']
print('chicken pizza' in pizzas)
print('chicken pizza' not in pizzas)
print('\n')


#如果只想执行一个代码块，就if-elif-elsi
#如果执行多个代码块，就使用一系列的if独立语句

#if语句处理列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"sorry,we don't have {requested_topping}.")

print('\nFinished making your dinner!')