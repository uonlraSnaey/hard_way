class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Cat(Animal): #定义Cat类，它继承自Animal类

    def __init__(self, name): # 定义了一个带有构造函数方法的类，带有一个名为name的参数
        self.name = name

class person(object): #定义一个person类

    def __init__(self, name):
        self.name = name #person类的属性name

        self.pet = None #person类的属性pet

class Employee(person): #定义Employee类

    def __init__(self, name, salary): #定义了一个名为'init'的方法(构造函数),接受name和salary参数
        # 调用了父类"person"的构造函数并传递了"name"参数。
        super(Employee, self).__init__(name) #使用了super()函数来调用父类的构造函数，确保父类进行初始化

        self.salary = salary #定义了一个名为‘salary’的实例变量

class Fish(object):
    pass

class Salmon(Fish):#定义了一个Salmon类继承自Fish类
    pass

class Halibut(Fish):
    pass

rever = Dog("Rover") #定义了一个名为 Rover 的 Dog 类的实例

satan = Cat("satan")

mary = person("Mary")

mary.pet = satan

frank = Employee("Frank", 12000)

flipper = Fish()

crouse = Salmon()

harry = Halibut()