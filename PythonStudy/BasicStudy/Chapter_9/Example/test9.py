#导入方式1：从ElectricCar模块导入两个类
from electric_car import Car,ElectricCar

#导入方式2:分别从car模块导入Car类，从ElectricCar模块导入ElectricCar类
# from car import Car
# from ElctricCar import ElectricCar

#导入方式3：先把所有类都集成到一个car模块内，即整合car.py和ElctricCar.py，再导入整个car模块
# import car

#导入方式4：导入模块中所有的类（不建议）--->通配符导入（wildcard import）
#不建议的原因：事实证明，在某些情况下，它可能导致与其他模块和/或名称空间中的变量发生冲突。
# from car import *
# from ElctricCar import *

'''报错：Unused import Battery from wildcard importpylint(unused-wildcard-import)
---->原因：Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准
（Pylint 默认使用的代码风格是 PEP 8，具体信息，请参阅参考资料）和有潜在问题的代码。'''



my_car = Car('subaru','outback','2015')
print(my_car.get_descriptive_name())
print()

my_car.read_odometer()
print()

my_car.update_odometer(23_500)
my_car.read_odometer()
print()

my_car.increment_odometer(100)
my_car.read_odometer()
print()


my_tesla = ElectricCar('tesla','modle s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

