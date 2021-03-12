#类中的函数-->方法

#可通过实例来访问的变量（方法中的形参）-->属性


class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):#self是指向实例本身的引用，使得实例可以访问类中的属性和方法
        """初始化属性name和age"""
        self.name = name
        self.age  = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")

    
my_dog = Dog('jack',2)

#执行部分
#访问属性
print(f"{my_dog.name} is my dog's name.\n")
print(f" He is {my_dog.age} years old.")
print()

#调用方法
my_dog.sit()
print()
my_dog.roll_over()
print()


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,modle,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.modle}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer} on it.")

    def update_odometer(self,mileage):
        """将里程表改值，但是不能调回"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("warning:You can't rool back an odometer!")
        
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        if miles >= 0:
            self.odometer += miles
        else:
            print("warning:You can't rool back an odometer!")

    def full_gas_tank(self):
        """给车加满油的操作"""
        print("Now the gas tank is full!")

#执行部分
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


#将实例用作属性（类中东西过于多，所以进行二次分类）
class Battery:
    """一次模拟汽车电瓶的简单尝试"""

    def __init__(self,battery_size=75):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    

#继承
#父类-->子类
#父类也称作超类，所以创建子类的时候，super()即是父类
#创建父类Car的子类ElectricCar
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,modle,year):
        """
        初始化父类的属性。
        再初始化子类的特殊属性。
        """
        super().__init__(make,modle,year)
        self.battery = Battery()#将实例用作属性

    #重写父类方法
    def full_gas_tank(self):
        """电动汽车没有油箱"""
        print("Electric car doesn't need a gas tank!")

#执行部分
my_tesla = ElectricCar('tesla','modle s','2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




# 注意事项：
# 1、父类（superclass）和子类一定要在同一个文件中，且子类一定在父类后面
# 2、定义子类时一定要在括号内指定父类的名称
# 3、super()是一个特殊的函数，可以调用父类的方法。
# 4、类的编码风格：驼峰命名法
#    函数（方法）命名：下划线命名法
# 5、模块头也要写文档字符串，描述模块概述，单行分隔方法，双行分隔类
# 6、要将导入的模块和主逻辑文件放在一个目录下