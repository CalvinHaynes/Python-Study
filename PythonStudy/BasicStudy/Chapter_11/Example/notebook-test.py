#本章主要是学习如何测试代码，看代码是否在各种操作下不会发生崩掉的稳定性，主要用到了模块-->unittest（在模块中可以看使用示例，go to definition一下即可）

'''The method of assert in module unittest(unittest模块中的断言方法)

   assertEqual(a,b)                        核实a == b
   assertNotEqual(a,b)                     核实a != b
   assertTrue(x)                           核实x为True
   assertFalse(x)                          核实x为False
   assertIn(item,list)                     核实item在list中
   assertNotIn(item,list)                  核实item不在list中

'''
#在unittest模块的TeseCase类继承的子类内编写测试的代码
# example:
# class NamesTestCase(unittest.TestCase):
#    pass

#方法SetUp()
#在unittest.TestCase类中包含了此方法，继承子类之后可以调用此方法
'''此方法的作用：如果定义了此方法，python会先运行其中的代码，再运行其他自己写的测试的代码，相当于C语言中的全局变量，或者说是这一个类中要用到的局部变量，把公共
的要使用的部分都放在这里初始化一下，减少冗余代码'''

