"""电动汽车类"""

from car import Car


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
