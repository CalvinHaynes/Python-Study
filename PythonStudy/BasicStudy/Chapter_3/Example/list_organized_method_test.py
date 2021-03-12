#sort()方法是永久性的改变list排列
#字母正排
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#字母反排
cars.sort(reverse=True)
print(cars)

#sorted()函数是对列表临时排序，不改变列表原本顺序
print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

#list倒置->reverse()方法->永久修改
cars.reverse()
print("\nHere is the reversed list:")
print(cars)

print("\nThe list cars' length is:")
print(len(cars))


#空list访问最后一个元素会报错
# motorcycles = []
# print(motorcycles[-1])