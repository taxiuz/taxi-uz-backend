# Object Oriented Programming

# b = 7
# print(type(b))  # qaysi class da ekanligini biladigon

# Konstruktor va Destruktor

# class Student:

#     def __init__(self, name):
#         print("Inside Constructor")

#         self.name = name

#         print("All variables initialized")

#     def show(self):
#         print("Hello, my name is", self.name)


# s1 = Student("Emma")
#
# s1.show()

# __new__() - bu Xotirada yangi obyekt yaratish.

# __init__() - bu Yaratilgan obyektga boshlang'ich qiymatlar berish.



# class Student:

#     university = "TATU"
#     is_active = True

#     def __init__(self, name):
#         self.name = name

# s1 = Student("Eshmat")
# s2 = Student("Toshmat")

# print(s1.university)
# print(s2.university)

# bu yerda s1 va s2 javobi TATU

# class Student:
#     def __new__(cls, name):
#         print("1. __new__ ishladi: Xotiradan joy ochildi va bo'sh obyekt yaratildi.")

#         return super().__new__(cls)

#     def __init__(self, name):
#         self.name = name
#         print(f"2. __init__ ishladi: Yaratilgan obyekt ichiga name='{self.name}' yuklandi.")


# s = Student("Emma")  # Obyektni chaqiramiz

# __new__ = yaratadi

# __init__ = boshlang‘ich qiymat beradi

# __init__ yakka o'zi hamma ishni qilmaydi, u __new__ ochib bergan xonaga jihozlarni joylashtiruvchi usta


# konstruktor turlari 3ta  Standart konstruktor,Parametrsiz konstruktor,Parametrli konstruktor

# Default Constructor - standart konstruktor

# class Student:
#     pass

# s1 = Student()

# print(s1)

# Non-Parametrized Constructor- parametrsiz konstrukor

# class Student:
#     pass  # __init__ yozilmadi
#
# s1 = Student()  # Muammosiz yaratiladi
#
# print(s1)

# Parametrized Constructor -- Parametrli konstruktor

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Emma", 14)

# print(s1.name)
# print(s1.age)

# -Method 2 turga bo‘linar ekan -Class Method - Instance Method

#self method

# class Student:
#     def show(self):
#         print("Instance method")

# s1 = Student()
# s1.show()

#Class Method

# class Student:
#     school = "Komiljon ustoz Talim"
#
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
#
#
# Student.show_school()

# Standart qiymatli konstruktor

# class Student:
#     def __init__(self, name="Unknown", age=0):
#         self.name = name
#         self.age = age

# s1 = Student()
# s2 = Student("Emma", 14)
#
# print(s1.name, s1.age)
# print(s2.name, s2.age)


# misol **

# class Student:
#     def __init__(self, name="Unknown", age=0):
#         self.name = name
#         self.age = age

# s3 = Student("Ali")

# print(s3.name, s3.age)

# constructor yordamida nechta obyekt yaratilganini bilish

# class Employee:
#     count = 0
#
#     def __init__(self):
#         Employee.count = Employee.count + 1
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Employee()
#
# print("The number of Employee:", Employee.count)

# class Taxi:
#     count = 10

#     def __init__(self):
#         Taxi.count = Taxi.count + 2

# t1 = Taxi()
# t2 = Taxi()
# t3 = Taxi()
#
# print(Taxi.count)

# Boshlanish: count = 10

# t1 = Taxi()  → 10 + 2 = 12
# t2 = Taxi()  → 12 + 2 = 14
# t3 = Taxi()  → 14 + 2 = 16 Natija 16 chiqadi

# Destructor - __del__

# class Student:
#
#     def __new__(cls, name, age):
#         print("1. __new__ ishladi")
#
#         obj = super().__new__(cls)
#
#         return obj
#
#     def __init__(self, name, age):
#         print("2. __init__ ishladi")
#
#         self.name = name
#         self.age = age
#
#     def __del__(self):
#         print("3. __del__ ishladi")
#
# stud = Student("Emma", 14)
#
# print("4. Obyekt ishlayapti")
#
# del stud

# constructor va destructor

# class Student:

#     # constructor
#     def __init__(self, name):
#         print('Inside Constructor')
#         self.name = name
#         print('Object initialized')

#     def show(self):
#         print('Hello, my name is', self.name)

#     # destructor
#     def __del__(self):
#         print('Inside destructor')
#         print('Object destroyed')


# # create object
# s1 = Student('Emma')
#
# s1.show()
#
# # delete object
# del s1



# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} yaratildi")
#
#     def __del__(self):
#         print(f"{self.name} yo'q qilindi")

# first_r = Student("Emma")
# second_r = first_r
#
# print("--- first_r o'chadi ---")
# del first_r
#
# print("--- second_r hali mavjud ---")
# print(second_r.name)
#
# print("--- second_r o'chadi ---")
# del second_r

# Garbage Collector

# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         print(f" {self.name} yaratildi")
#
#     def show(self):
#         print(f"Salom, men {self.name}")
#
#     def __del__(self):
#         print(f" {self.name} o'chirildi")
#
#
# print("=== 1-qadam ===")
# first_r = Student("Emma")
#
# print("\n=== 2-qadam ===")
# second_r = first_r
#
# print("\n=== 3-qadam ===")
# print("first_r o'chirilmoqda...")
# del first_r
#
# print("\n=== 4-qadam ===")
# print("second_r hali ham ishlayapti:")
# second_r.show()
#
# print("\n=== 5-qadam ===")
# print("second_r endi yangi obyektga ishora qiladi")
# second_r = Student("Ali")
#
# print("\n=== 6-qadam ===")
# second_r.show()
#
# print("\n=== Dastur tugadi ===")

# bu yerda Yangi Ali obyektini yaratadi.
# second_r ni eski Emma obyektidan uzib, yangi Ali obyektiga boglaydi...***

# import gc
#
# class A:
#     def __init__(self):
#         print("A yaratildi")
#
#     def __del__(self):
#         print("A o'chirildi")
#
#
# class B:
#     def __init__(self):
#         print("B yaratildi")
#
#     def __del__(self):
#         print("B o'chirildi")
#
#
# a = A()
# b = B()
#
# a.b = b
# b.a = a
#
# print("Tashqi reference lar o'chirilmoqda...")
# del a
# del b
#
# print("GC ishga tushmoqda...")
# gc.collect()
#
# print("Dastur tugadi.")

# vorislik va class atributi ishlatilgan

# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#
# class Jangchi(Odam):
#     energiya = 100          # Class atributi
#     jang_qiyinligi = 30     # Class atributi
#
#     def jang_qil(self):
#         if self.energiya >= self.jang_qiyinligi:
#             self.energiya -= self.jang_qiyinligi
#             print(f"Jangda {self.jang_qiyinligi} energiya yo'qotildi.")
#             print(f"Qolgan energiya: {self.energiya}")
#         else:
#             print("Jang uchun energiya yetarli emas.")
#
#
# Botir = Jangchi("Botir")
#
# Botir.jang_qil()
# Botir.jang_qil()
# Botir.jang_qil()
# Botir.jang_qil()
# Botir.jang_qil()

# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#
# class Jangchi(Odam):
#     energiya = 100          # Class atributi
#     jang_qiyinligi = 30     # Class atributi
#
#     def jang_qil(self):
#         if self.energiya >= self.jang_qiyinligi:
#             self.energiya -= self.jang_qiyinligi
#             print(f"Jangda {self.jang_qiyinligi} energiya yo'qotildi.")
#             print(f"Qolgan energiya: {self.energiya}")
#         else:
#             print("Jang uchun energiya yetarli emas.")
#
#
# class Odam:
#     def __init__(self, ism):
#         self.ism = ism
#
#
# class Shifokor(Odam):
#     dorilar = ["Trimol", "Suv"]
#
#     def davola(self):
#         if len(self.dorilar) > 0:
#             dori = self.dorilar.pop()
#             print(f"{dori} yordamida davolandi!")
#         else:
#             print("Dori qolmadi!")
#
#
# Doniyor = Shifokor("Doniyor")
#
# Doniyor.davola()
# Doniyor.davola()

# Diamond Problem нима?

# class Base:
#     def show(self):
#         print("Base")
#
#
# class Left(Base):
#     def show(self):
#         print("Left")
#
#
# class Right(Base):
#     def show(self):
#         print("Right")
#
#
# class Child(Left, Right):
#     pass
#
#
# obj = Child()
# obj.show()
#
# print(Child.mro())

# Polymorphism - NIMA bu kim nima ish qilishi

# class Driver:
#     def work(self):
#         print("Mijozni olib boradi")
#
#
# class Operator:
#     def work(self):
#         print("Qo'ng'iroqqa javob beradi")
#
#
# class Manager:
#     def work(self):
#         print("Jamoani boshqaradi")
#
#
# employees = [
#     Driver(),
#     Operator(),
#     Manager()
# ]
#
# for employee in employees:
#     employee.work()


# oz misolimda

# class Customer:
#     def notification(self):
#         pass
#
#
# class VIPCustomer(Customer):
#     def notification(self):
#         print("VIP xizmat taklif qilindi")
#
#
# class LostCustomer(Customer):
#     def notification(self):
#         print("Qaytarish taklifi yuborildi")
#
#
# class NewCustomer(Customer):
#     def notification(self):
#         print("Birinchi safar yordami yuborildi")

# yana bir misol


# from abc import ABC, abstractmethod
#
#
# class Customer(ABC):
#     def __init__(self, name: str, is_permitted: bool = False):
#         self.name = name
#         self.is_permitted = is_permitted  # Permission-based Personal AI
#
#     @abstractmethod
#     def notification(self):
#         """Ҳар бир мижоз тури ўз билдиришномасини ёзиши шарт"""
#         pass
#
#
# class VIPCustomer(Customer):
#     def notification(self):
#         if self.is_permitted:
#             print(f" LUX VIP | {self.name}, сиз учун махсус Comfort+ машина тайёр.")
#         else:
#             print(f" {self.name} билдиришномаларга рухсат бермаган (Ишонч сақланди).")
#
#
# class LostCustomer(Customer):
#     def __init__(self, name: str, last_active_days: int, is_permitted: bool = False):
#         super().__init__(name, is_permitted)
#         self.last_active_days = last_active_days
#
#     def notification(self):
#         # Бу ерда шунчаки спам скидка эмас, контекст ишламоқда (10-банд)
#         print(
#             f" RECOVERY | {self.name} охирги {self.last_active_days} кун ичида сафар қилмади. Муаммога мос ечим юборилди.")
#
#
# class NewCustomer(Customer):
#     def notification(self):
#         print(f" WELCOME | {self.name}, LUX тизимига хуш келибсиз! Биринчи сафар қулайлиги бўйича қўлланма юборилди.")
#
#
# # --- СИСТЕМАНЫ ТЕШКИРИБ КЎРАМИЗ (Simulation) ---
# if __name__ == "__main__":
#     # Мижозлар оқими (Бизнес базасидан келди)
#     active_users = [
#         VIPCustomer(name="Alisher", is_permitted=True),
#         VIPCustomer(name="Bobur", is_permitted=False),  # Рухсат бермаган
#         LostCustomer(name="Ali", last_active_days=21, is_permitted=True),
#         NewCustomer(name="Madina", is_permitted=True)
#     ]
#
#     print(" LUX LIFE AI — Notification Engine ишга тушди:\n" + "-" * 50)
#     for customer in active_users:
#         customer.notification()

# Polymorphism with Inheritance va Method Overriding

# class Vehicle:
#     def speed(self):
#         print("Max speed 150")
#
#     def change_gear(self):
#         print("5 gear")
#
#     def show(self):
#         print("Display Vehicle")
#
#
# class Car(Vehicle):
#     def speed(self):
#         print("Max speed 240")
#
#     def change_gear(self):
#         print("6 gear")
#
#
# class Truck(Vehicle):
#     def speed(self):
#         print("Max speed 200")
#
#     def change_gear(self):
#         print("8 gear")
#
#
# truck = Truck()
#
# truck.show()
# truck.speed()
# truck.change_gear()

# ---------Vazifa-------------

# 1-VAZIFA: Texnika rightarrow LUX Hardware Fleet (Tizim Qurilmalari)

# class Hardware:  # Parent class
#     def __init__(self, brand: str, model: str, type: str):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(
#             f" Qurilma: {self.brand} {self.model} "
#             f"| Turi: {self.type}"
#         )
#
#
# class DispatcherPC(Hardware):  # Child class
#     def __init__(
#         self,
#         brand: str,
#         model: str,
#         type: str,
#         video_card: str,
#         ram: int,
#         display: str
#     ):
#         super().__init__(brand, model, type)
#
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         print(
#             f" Dispatcher PC: {self.brand} {self.model} "
#             f"({self.type}) | Video: {self.video_card} "
#             f"| RAM: {self.ram}GB | Ekran: {self.display}"
#         )
#
#
# class DriverTablet(Hardware):  # Child class
#     def __init__(
#         self,
#         brand: str,
#         model: str,
#         type: str,
#         size: float,
#         sim_count: int
#     ):
#         super().__init__(brand, model, type)
#
#         self.size = size
#         self.sim_count = sim_count
#
#     def more_info(self):
#         print(
#             f' Haydovchi plansheti: {self.brand} {self.model} '
#             f'({self.type}) | Ekran: {self.size}" '
#             f'| SIM-kartalar: {self.sim_count}'
#         )
#
#
# pc = DispatcherPC(
#     "HP",
#     "ProDesk",
#     "Computer",
#     "NVIDIA GTX",
#     16,
#     "24 inch"
# )
#
# tablet = DriverTablet(
#     "Samsung",
#     "Galaxy Tab",
#     "Tablet",
#     10.5,
#     2
# )
#
#
# pc.info()
# pc.more_info()
#
# tablet.info()
# tablet.more_info()


# 2- vazifa --VAZIFA: Transport

# class Transport:
#     def __init__(self, brand: str, model: str, type: str):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#     def info(self):
#         print(
#             f" Mashina: {self.brand} {self.model} "
#             f"| Tarif: {self.type}"
#         )
#
#
# class ElectricEco(Transport):
#     def __init__(
#         self,
#         brand: str,
#         model: str,
#         type: str,
#         battery_life: int,
#         charging_time: int
#     ):
#         super().__init__(brand, model, type)
#         self.battery_life = battery_life
#         self.charging_time = charging_time
#
#     def more_info(self):
#         print(
#             f"⚡ LUX Eco-Green: {self.brand} {self.model} "
#             f"({self.type}) | Zaryad: {self.battery_life} km "
#             f"| Quvvatlanish: {self.charging_time} min"
#         )
#
#
# class LuxSport(Transport):
#     def __init__(
#         self,
#         brand: str,
#         model: str,
#         type: str,
#         motor: str,
#         color: str
#     ):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(
#             f" LUX Premium Sport: {self.brand} {self.model} "
#             f"({self.type}) | Motor: {self.motor} "
#             f"| Rangi: {self.color}"
#         )
#
#
# class LuxCargo(Transport):
#     def __init__(
#         self,
#         brand: str,
#         model: str,
#         type: str,
#         motor: str,
#         height: float,
#         length: float,
#         weight: float
#     ):
#         super().__init__(brand, model, type)
#         self.motor = motor
#         self.height = height
#         self.length = length
#         self.weight = weight
#
#     def more_info(self):
#         print(
#             f" LUX Cargo: {self.brand} {self.model} "
#             f"({self.type}) | Motor: {self.motor} "
#             f"| Sig'imi: {self.weight} tonna "
#             f"| O'lchami: {self.length}x{self.height} m"
#         )
#
#
# # OBYEKTLAR YARATAMIZ
#
# eco = ElectricEco(
#     "BYD",
#     "E2",
#     "Eco",
#     405,
#     40
# )
#
# sport = LuxSport(
#     "BMW",
#     "M5",
#     "Premium",
#     "V8",
#     "Black"
# )
#
# cargo = LuxCargo(
#     "Isuzu",
#     "NPR",
#     "Cargo",
#     "Diesel",
#     2.5,
#     6.0,
#     5.0
# )
#
#
# # METODLARNI CHAQIRAMIZ
#
# eco.info()
# eco.more_info()
#
# sport.info()
# sport.more_info()
#
# cargo.info()
# cargo.more_info()


# 3-  VAZIFA: University - Staff

# class LuxEcosystem:  # Parent class
#     def __init__(self, business_name: str):
#         self.business_name = business_name
#
#     def info(self):
#         print(f" Tizim: {self.business_name}")
#
#
# class EcosystemMember(LuxEcosystem):
#     def __init__(
#         self,
#         business_name: str,
#         first_name: str,
#         last_name: str,
#         age: int
#     ):
#         super().__init__(business_name)
#
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def member_info(self):
#         print(
#             f" {self.business_name} a'zosi: "
#             f"{self.first_name} {self.last_name} "
#             f"| Yoshi: {self.age}"
#         )
#
#
# class Driver(EcosystemMember):
#     def __init__(
#         self,
#         business_name: str,
#         first_name: str,
#         last_name: str,
#         age: int,
#         group: str
#     ):
#         super().__init__(
#             business_name,
#             first_name,
#             last_name,
#             age
#         )
#
#         self.group = group
#
#     def more_info(self):
#         print(
#             f" Haydovchi: {self.first_name} {self.last_name} "
#             f"| Guruh/Kogorta: {self.group} "
#             f"| Tizim: {self.business_name}"
#         )
#
#
# class SupportOperator(EcosystemMember):
#     def __init__(
#         self,
#         business_name: str,
#         first_name: str,
#         last_name: str,
#         age: int,
#         position: str,
#         subject: str
#     ):
#         super().__init__(
#             business_name,
#             first_name,
#             last_name,
#             age
#         )
#
#         self.position = position
#         self.subject = subject
#
#     def more_info(self):
#         print(
#             f" Operator: {self.first_name} {self.last_name} "
#             f"| Lavozim: {self.position} "
#             f"| Yo'nalish: {self.subject}"
#         )
#
#
# # OBYEKTLAR
#
# driver = Driver(
#     "LUX Taxi",
#     "Alisher",
#     "Yoqubov",
#     35,
#     "Premium Drivers"
# )
#
# operator = SupportOperator(
#     "LUX Taxi",
#     "Dilnoza",
#     "Aliyeva",
#     27,
#     "Senior Operator",
#     "VIP mijozlar"
# )
#
#
# # METHODLARNI CHAQIRAMIZ
#
# driver.info()
# driver.member_info()
# driver.more_info()
#
# print("-" * 50)
#
# operator.info()
# operator.member_info()
# operator.more_info()

# 3- VAZIFA: Object - Inventory

# class LuxEcosystem:
#     def __init__(self, company_name):
#         self.company_name = company_name
#
#     def info(self):
#         print(f" Компания: {self.company_name}")
#
#
# class Asset(LuxEcosystem):
#     def __init__(self, company_name, asset_name):
#         super().__init__(company_name)
#         self.asset_name = asset_name
#
#     def asset_info(self):
#         print(f" {self.company_name} | Актвит номи: {self.asset_name}")
#
#
# class ServerHardware(Asset):
#     def __init__(self, company_name, asset_name, soni, tizimi, holati):
#         super().__init__(company_name, asset_name)
#         self.soni = soni
#         self.tizimi = tizimi
#         self.holati = holati
#
#     def asset_more_info(self):
#         print(
#             f" {self.company_name} -> {self.asset_name} | "
#             f"Сони: {self.soni} та | Тизим: {self.tizimi} | Ҳолати: {self.holati}"
#         )
#
#
# class StationFurniture(Asset):
#     def __init__(self, company_name, asset_name, soni, turi, holati):
#         super().__init__(company_name, asset_name)
#         self.soni = soni
#         self.turi = turi
#         self.holati = holati
#
#     def asset_more_info(self):
#         print(
#             f" {self.company_name} -> {self.asset_name} | "
#             f"Сони: {self.soni} та | Тўплам тури: {self.turi} | Ҳолати: {self.holati}"
#         )
#
#
#
# if __name__ == "__main__":
#
#     fever_server = ServerHardware("LUX LIFE AI", "Business Fever Main Server", 2, "Ubuntu Server 24.04", "Active")
#
#     operator_chair = StationFurniture("LUX LIFE AI", "Ergonomic Dispatcher Chair", 12, "Ortopedik стул", "Yangi")
#
#     print(" LUX Инвентаризация тизими ишга тушди:\n" + "-" * 60)
#     fever_server.asset_more_info()
#     operator_chair.asset_more_info()

# 4- Method Overriding

# class Customer:
#     def calculate_fare(self, distance):
#         return distance * 3000
#
#
# class VIPCustomer(Customer):
#     def calculate_fare(self, distance):
#         return (distance * 4500) + 10000
#
#
# customer = Customer()
# vip = VIPCustomer()
#
# print(customer.calculate_fare(10))
# print(vip.calculate_fare(10))

# -----Test savollari---------

# 1- savol Klass atributlari va metodlarini obyektdan tashqarida bevosita ozgartirilishini cheklash, faqat metod orqali ularga kirish imkonini berish qaysi tamoyilga tegishli?
# javob:Ma'lumotlarni yashirish va ularni faqat maxsus metodlar (getter/setter) orqali boshqarish aynan kapsulatsiya tamoyilining vazifasidir

# class Customer:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def get_balance(self):
#         return self.__balance
#
#     def add_balance(self, amount):
#         if amount > 0:
#             self.__balance += amount
#
#
# customer = Customer(50000)
#
# print(customer.get_balance())
#
# customer.add_balance(20000)
#
# print(customer.get_balance())

# 2- savol Bir klass boshqa klassning xususiyatlari va metodlarini meros qilib olishi qaysi tamoyilga tegishli?
# javob :Yuqorida biz ham aynan shu tamoyilni, ya'ni parent klassdan child klassga xususiyatlarning o‘tishini muhokama qilayotgan edik.

# class Transport:
#     def info(self):
#         print("LUX Taxi transporti")
#
#
# class ElectricCar(Transport):
#     pass
#
#
# car = ElectricCar()
# car.info()

# 3- savol turli klasslarda bir xil nomdagi metodlar har xil xatti-harakatni bajarishi qaysi tamoyilga tegishli?
# javop:Polymorphism

# class StandardTariff:
#     def calculate_fare(self, distance):
#         return distance * 3000
#
#
# class VIPTariff:
#     def calculate_fare(self, distance):
#         return distance * 4500 + 10000
#
#
# tariffs = [
#     StandardTariff(),
#     VIPTariff()
# ]
#
# for tariff in tariffs:
#     print(tariff.calculate_fare(10))

# 4- savol klassning ichki murakkabligi yashirilib, faqat kerakli interfeyslar orqali foydalanish imkonini beruvchi tamoyil qaysi?
# javob: Abstraction

# class LuxTaxi:
#     def order(self):
#         self.find_driver()
#         self.calculate_price()
#         self.build_route()
#
#         print(" Taxi buyurtma qilindi")
#
#     def find_driver(self):
#         print("Haydovchi topildi")
#
#     def calculate_price(self):
#         print("Narx hisoblandi")
#
#     def build_route(self):
#         print("Marshrut qurildi")
#
#
# taxi = LuxTaxi()
# taxi.order()

# 5- savol ushbu kodga natija nima boladi

# class StandardTaxi:
#     def service(self):
#         print("Oddiy xizmat")
#
#
# class LuxTaxi:
#     def service(self):
#         print("Premium xizmat")
#
#
# taxis = [
#     StandardTaxi(),
#     LuxTaxi()
# ]
#
# for taxi in taxis:
#     taxi.service()

# 6- savol -Ota class bu
# Boshqa klasslar (child / subclass) tomonidan xususiyatlari va metodlari meros qilib olinadigan klass

# class Transport:
#     def info(self):
#         print("LUX Taxi transporti")
#
# class ElectricCar(Transport):
#     pass
#
# class LuxCar(Transport):
#     # Ота классдаги методни фарзанд ичида қайта белгилаймиз (Override)
#     def info(self):
#         print(" LUX Premium — Олий даражадаги VIP транспорт")
#
# electric = ElectricCar()
# lux = LuxCar()
#
# electric.info()
# lux.info()

# 7- savol --bola class (Child / Subclass) bu
# javob:Ota (parent) class’dan xususiyatlari va metodlarini meros qilib olgan klass

# class Transport:
#     def info(self):
#         print("LUX Taxi transporti")
#
#
# class LuxCar(Transport):
#     def vip_service(self):
#         print("VIP xizmat mavjud")
#
#
# car = LuxCar()
#
# car.info()
# car.vip_service()

# 8-savol-- Method Resolution Order (MRO) bu
# Multiple Inheritance da bitta metod bir nechta parent class’larda topilsa, qaysi birini ishlatishni aniqlab beradi

# class Taxi:
#     def service(self):
#         print("Oddiy Taxi xizmati")
#
#
# class Premium:
#     def service(self):
#         print("Premium xizmat")
#
#
# class LuxTaxi(Taxi, Premium):
#     pass
#
#
# car = LuxTaxi()
# car.service()
#
# print(LuxTaxi.mro())
