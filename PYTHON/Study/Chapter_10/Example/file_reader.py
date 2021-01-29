
# with open('pi_digits.txt') as file_object:
'''[Errno 2] No such file or directory: 'pi_digits.txt'-->由于我用的文本编辑器是Vscode，所以会出现这种bug，原因是Vscode会把.vscode文件夹所在目录
算作默认位置，即.vscode所在目录是工作区，所以当你把路径改为绝对路径时（我的电脑是D:/PYTHON/Study/Chapter_10/Example/pi_digits.txt），基于我的文件结
构才不会出问题'''

#with关键字在不再访问文件时将其关闭
file_path = 'D:/PYTHON/Study/Chapter_10/Example/pi_digits.txt'
#read方法
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)
print()

#for循环打印文件每行
with open(file_path) as file_object:
    for line in file_object:
        print(line)
print()

#readlines方法创建一个包含各行内容的列表+for循环打印
with open(file_path) as file_object:
    lines = file_object.readlines()

print(lines)
print()
for line in lines:
    print(line)

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(float(pi_string))

filename = 'D:/PYTHON/Study/Chapter_10/Example/programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games!\n")

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#将可能引发错误的代码放在try-except代码块中，提高代码抵御错误的能力（例子：用户输入无效数据，防止崩溃显示Traceback）
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divid by zero!")


#除法计算器(try-except-else结构)
print("please give me two numbers,and I will divide them.\n")
print("Enter 'q' to quit.")

while True:
    first_number = input('First number:')
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divid by zero!")
    else:#仅在try后代码执行成功时才需要运行的代码
        print(answer)


#静默失败--->except语句后写pass即可