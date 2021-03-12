"""一个可用于表示汽车的类"""


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