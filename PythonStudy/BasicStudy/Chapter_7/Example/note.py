#创建多行字符串的办法"+=""


prompt = "If you tell us who you are,we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello,{name}!\n")

#input:Read a string from standard input. The trailing newline is stripped.
#input得到的值用于比较时，应先int()一下，变成数字再比较

#函数的注释紧跟在 def 函数名：后面，格式为'''注释'''

#指定默认值的形参一般往后放，防止位置实参顺序的变化
def discribe_pet(pet_name,animal_type = 'dog'):
    print(f'I have a {animal_type}')
    print(f'Its name is {pet_name}\n')


discribe_pet('jiwawa')#不输入——>默认参数
discribe_pet('mimi','cat')#位置实参
discribe_pet(pet_name='wasabi',animal_type='bird')#关键字参数


#让实参变为可选的办法：让可选的形参默认值为空即'',然后将其放于函数形参的末尾，也是为了防止出现位置参数顺序错误的问题
#在条件测试中，None相当于False

#函数应轻量化为主，如果发现功能太多无法在一个函数中实现，先静下心来，拆分执行步骤，建立流程图，每个步骤用一个函数来表示，就可以方便很多

#向函数传递列表的副本，可以保证原列表不被修改，但是会浪费时间和内存创建副本，尽量不用

#传递任意数量的实参
def make_pizza(*toppings):#这里的*让python创建了一个叫做toppings的空元组，并将所有收到的值都装到这个元组中
    print(toppings)

make_pizza('peper')
make_pizza('mushrooms','green peppers','extra cheese','mongo')
print()

#结合使用位置实参和任意数量实参
#必须将任意数量实参放在最后
def make_pizzas(size,*toppings):
    print(f'Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f"- {topping}")

make_pizzas(12,'mushrooms','green peppers','extra cheese')
print()
#通用形参名 *args-->收集任意数量的位置实参

#使用任意数量的关键字实参-->**kwargs
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert','einstein',location = 'princeton',field = 'physics')
print(user_profile)

#函数存储在modules中
#modules 是扩展名为.py的文件
import math

#函数编写指南

# 1、函数名只使用小写字母和下划线
# 2、每个函数都应该有注释（文档字符串格式  """注释"""  ）
# 3、给形参指定默认值的时候，等号两边不要有空格 
# 4、形参列表过多时：
# def function_name(
#         parameter_0,parameter_1,parameter_2,
#         parameter_3,parameter_4,parameter_5):
#     function body...
# 5、所有import语句都应该放在文件开头