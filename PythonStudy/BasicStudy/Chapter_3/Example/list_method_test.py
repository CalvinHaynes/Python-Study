motorcycles = ['honda','yamaha','suzuki','giant']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#末尾添加列表元素
motorcycles.append('ducati')
print(motorcycles)

#空列表+末尾添加列表元素
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#列表插入元素
motorcycles.insert(0,'aima')
print(motorcycles)

#列表删除元素
del motorcycles[0]
print(motorcycles)

#删除并且弹出列表末尾的元素
poped_motocycle = motorcycles.pop()
print(poped_motocycle)
print(motorcycles)

#删除并且弹出列表中任意位置的元素
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)

#方法remove()只删除第一个指定的值。如果要删除的值在列表中出现多次，则需要使用循环来确保每个值被删除