#oop  obekt /

# class Mashina:
#     def __init__(self, narxi, tezligi, rangi):
#         self.narxi = narxi
#         self.rangi = rangi
#         self.tezligi = tezligi
#
#     def signal(self, tovush="Beep!"):
#         print(tovush)
#
# m = Mashina(narxi=3000, tezligi=220, rangi="oq")
# m.nomi = "Tesla"

# class Mashina:
#     def __init__(self, nomi, narxi, tezligi, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.tezligi = tezligi
#         self.rangi = rangi
#
# m = Mashina("Tesla", 3000, 220, "oq")


# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, word):
#         print(f"{self.name} aytadi: {word}")
#
# Doe = Person(name="Doe", age=20, gender="male")
# Anna = Person(name="Anna", age=18, gender="female")
#
# Doe.speak("Salom Anna")
# Anna.speak("Salom Doe, yaxshimisiz?")

# class Person:
#     arms = 2
#     legs = 2
#     country = "Uzbekiston"
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, word):
#         print(f"{self.name} aytadi: {word}")
#
# Doe = Person(name="Doe", age=20, gender="male")
# Anna = Person(name="Anna", age=18, gender="female")
#
# Doe.speak("Salom Anna")
# Anna.speak("Salom Doe, yaxshimisiz?")
# print(Doe.arms)


# class Oson1:
#     a = 4
#
#     def print_a(cls):
#         print(cls.a)
#
# Oson1.print_a(Oson1)


# class Oson1:
#     a = 4
#
#     @classmethod
#     def print_a(cls):
#         print(cls.a)
#
# Oson1.print_a()

# class Person:
#     arms = 2
#     legs = 2
#     country = "Uzbekiston"
#
#     def __init__(obj, name, age, gender):
#         obj.name = name
#         obj.age = age
#         obj.gender = gender
#
#     def speak(self, word):
#         print(f"{self.name} aytadi: {word}")
#
#     def change_country(self, new_country):
#         self.country = new_country

# numbers = [1,2,3,4]
#
# result = []
#
# for i in numbers:
#     result.append(i*2)
#
# print(result)

# def add(a, b):
#     return a + b
#
# print(add(5, 4))


# for i in range(5):
#     if i % 2 == 0:
#         print(i)

# class Car:
#
#     def __init__(self, color):
#         self.color = color
#
#     def drive(self):
#         print("Mashina yurmoqda")
#
# car = Car("Qora")
# car.drive()

# class Car:
#
#     def __init__(self, color):
#         self.color = color
#
#     def drive(self):
#         print("Mashina yurmoqda")
#
# car = Car("Qora")
# car.drive()

# PARADIGMALAR

# def salom():
#     print("Salom")  #Procedural

# for i in range(5):
#     # print(i)     #Structured

# class Student:
#     # Class attribute
#     school = "Najot Ta'lim"
#
#     # Constructor
#     def __init__(self, name, age):
#         self.name = name      # Instance attribute
#         self.age = age
#
#     # Instance method
#     def introduce(self):
#         print(f"Salom, mening ismim {self.name}. Yoshim {self.age} da.")
#
#     # Instance method
#     def birthday(self):
#         self.age += 1
#         print(f"Tabriklaymiz! Endi {self.age} yoshdasiz.")
#
# # Object yaratish
# student1 = Student("Ali", 20)
# student2 = Student("Vali", 22)
#
# student1.introduce()
# student2.introduce()
#
# student1.birthday()
#
# print(student1.school)
# print(Student.school)       #OOP


# m = map(lambda x:x*x,[1,2,3])
#
# print(m)


# natija=[]
#
# for x in [1,2,3]:
#     natija.append(x*x)
# print(natija)             #map()

# # 1. Proseduraviy uslub (Sikl va qadamlar bilan)
# natija = []
# for x in [1, 2, 3]:
#     natija.append(x * x)
#
# # 2. Funksional uslub (Matematik oqim/map bilan)
# natija = list(map(lambda x: x*x, [1, 2, 3]))
#
# # 3. OOP uslubi (Obyekt xususiyati sifatida)
# class Matematika:
#     def __init__(self, sonlar):
#         self.sonlar = sonlar
#     def kvadrat(self):
#         return [x*x for x in self.sonlar]
#
# obj = Matematika([1, 2, 3])
# natija = obj.kvadrat()





# -----------test savoli--------------

# 1- OOP (Object-Oriented Programming) bu -Ma'lumotlar (atributlar) va ularni boshqaruvchi metodlarni bitta obyektga birlashtirib, dastur tuzish paradigmasi.

# class Student:
#     def __init__(self, name, age):
#         self.name = name      # atribut
#         self.age = age        # atribut
#
#     def study(self):          # metod
#         print(f"{self.name} dars qilmoqda")

# OOP ma'lumot va xatti-harakatni bitta obyektga jamlaydi.

# 2- Atribut (Attribute) bu ---Class ichidagi o‘zgaruvchi.

# class Car:
#     # ==========================
#     # Class Attributes
#     # ==========================
#     country = "Uzbekiston"
#     wheels = 4
#     color = "Qora"
#
#     # ==========================
#     # Constructor
#     # ==========================
#     def __init__(self, model, brand, year, price):
#         # Instance Attributes
#         self.model = model
#         self.brand = brand
#         self.year = year
#         self.price = price
#
#     # ==========================
#     # Instance Method
#     # ==========================
#     def info(self):
#         print("=== Avtomobil ma'lumotlari ===")
#         print(f"Brend   : {self.brand}")
#         print(f"Model   : {self.model}")
#         print(f"Yili    : {self.year}")
#         print(f"Narxi   : {self.price}$")
#         print(f"Rangi   : {self.color}")
#         print(f"Davlat  : {self.country}")
#         print(f"G'ildirak: {self.wheels}")
#
#     # ==========================
#     # Instance Method
#     # ==========================
#     def start(self):
#         print(f"{self.model} ishga tushdi.")
#
#     # ==========================
#     # Instance Method
#     # ==========================
#     def stop(self):
#         print(f"{self.model} o'chirildi.")
#
#     # ==========================
#     # Class Method
#     # ==========================
#     @classmethod
#     def change_color(cls, new_color):
#         cls.color = new_color
#
#     # ==========================
#     # Static Method
#     # ==========================
#     @staticmethod
#     def horn():
#         print("Bip Bip!")
#
# **************************
#
# # 2 ta alohida mashina obyekti yaratamiz
# car1 = Car("Gentra")
# car2 = Car("Malibu")
#
# # 1. Object atributlarini tekshiramiz (Har birida har xil)
# print(car1.model)  # Natija: Gentra
# print(car2.model)  # Natija: Malibu
#
# # 2. Class atributini tekshiramiz (Ikkalasida ham bir xil!)
# print(car1.color)  # Natija: Qora
# print(car2.color)  # Natija: Qora
#
# # Agar klassning o'zidan rangni so'rasak ham "Qora" chiqadi
# print(Car.color)   # Natija: Qora
#
# Car.color = "Oq"  # Umumiy qolip rangini "Oq" qildik
# print(car1.color)  # Natija: Oq
# print(car2.color)  # Natija: Oq
#
# # Lekin biror mashinaga shaxsiy rang bersak, u faqat o'ziniki bo'lib qoladi:
# car1.color = "Qizil" # car1 o'ziga shaxsiy object atributi yaratib oldi
# print(car1.color)  # Natija: Qizil
# print(car2.color)  # Natija: Oq (Klassniki bo'lib qolaveradi)
#
# car1 = Car("Malibu 2", "Chevrolet", 2024, 32000)
# car2 = Car("Cobalt", "Chevrolet", 2023, 17000)

# 3- Metod bu --Classga tegishli bo'lgan funksiya

# class Car:
#
#     def start(self):
#         print("Mashina ishga tushdi")

# Oddiy funksiya
# def hello():
#     print("Salom")
#
# hello()

# Method
# class Person:
#
#     def hello(self):
#         print("Salom")
#
# p = Person()
# p.hello()

# 4-Paradigma guruhlari berilgan qatorni belgilang

# sonlar = [1, 2, 3, 4]
# juftlar = []
#
# for x in sonlar:
#     if x % 2 == 0:
#         juftlar.append(x)
#
# print(juftlar)


# 5- self nima vazifa bajaradi --Klass ichidagi obyektning oziga ishora qiluvchi parametr.

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name)
#
# s1 = Student("Ali")
# s2 = Student("Vali")
#
# s1.show()  # Ali
# s2.show()  # Vali


# 6-Constructor bu nima --Klassdan obyekt yaratilganda avtomatik chaqiriladigan va obyekt atributlarini boshlangich qiymat bilan belgilovchi metod.

# class Car:
#     def __init__(self, model):
#         self.model = model
#
#
#     def hayda(self):
#         print(f"{self.model} harakatlanmoqda... Vrum-vrum!")
#
# mening_mashinam = Car("Malibu")
#
# mening_mashinam.hayda()

# 7- Destructor nima va u nima vazifa bajaradi -- Klassdan yaratilgan obyekt hayoti tugaganda avtomatik chaqiriladigan va resurslarni tozalash uchun ishlatiladigan metod.

# class Car:
#
#     def __init__(self, model):
#         self.model = model
#         print(f"{self.model} yaratildi")
#
#     def __del__(self):
#         print(f"{self.model} o'chirildi")

# s1 = Student("Ali")
# s2 = s1
#
# print("--- 1-qadam ---")
# del s1
# 
# print("--- 2-qadam ---")
# del s2

