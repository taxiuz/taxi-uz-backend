# Type() Funksiya qiymat qaytarish kerak.

# def room_type():
#     while True:
#         t = input("e-ekonom, s-standart, l-lyuks: ")
#
#         if t == "e":
#             return "ekonom"
#
#         elif t == "s":
#             return "standart"
#
#         elif t == "l":
#             return "lyuks"
#
#         print("Noto'g'ri tanlov!")
#
# xona = room_type()
# print(f"Siz {xona} xonasini tanladingiz.")

# Kotta xarf bilan kirgazsaxam ishlaydi /

# def room_type():
#     while True:
#         t = input("e-ekonom, s-standart, l-lyuks: ").strip().lower()
#
#         if t == "e":
#             return "ekonom"
#         elif t == "s":
#             return "standart"
#         elif t == "l":
#             return "lyuks"
#
#         print(" Noto'g'ri tanlov! Faqat e, s yoki l kiriting.")
# room = room_type()
# print(room)

# Bu qator kodimiz chiroylik chiqishi uchun (table header)

# print("{:<15}{:<10}{:<15}".format(
#     "Ismi",
#     "Xona",
#     "Tur"
# ))
#
# print("-"*40)
#
# print("{:<15}{:<10}{:<15}".format(
#     "Ali",
#     "12",
#     "Standart"
# ))
#
# print("{:<15}{:<10}{:<15}".format(
#     "John",
#     "25",
#     "Lyuks"
# ))
#
# print("{:<15}{:<10}{:<15}".format(
#     "Doe",
#     "8",
#     "Ekonom"
# ))

# Formatlash oddiy!/

# name = "Ali"
# age = 25

# print("Ismi: {}, Yoshi: {}".format(name, age))

# indeks orqali

# print("{0} {1}".format("Ali", 25))

# index qayta ishlatish orqali

# print("{0} {0} {1}".format("Ali", 25))

# Nomlangan parametrlar orqali

# print("Ismi: {name}, Yoshi: {age}".format(
#     name="Ali",
#     age=25
# ))

# chepga telislash (<)

# print("{:<10}".format("Ali"))

# O'nga tekislash

# print("{:>10}".format("Ali"))

# O'rtaga joylash (^)

# print("{:^10}".format("Ali"))

# Belgilar bilan toldirish

# print("{:*^20}".format("Taxi Lux"))

# son formatlash

# print("{:.2f}".format(12.34567))

# minglik ajratish

# print("{:,}".format(12500000))

# foiz

# print("{:.1%}".format(0.875))

# Jadval chiqarish Dicionary bilan

# print("{:<15}{:<10}{:<15}".format(
#     "Ismi",
#     "Xona",
#     "Tur"
# ))
#
# print("-"*40)
#
# print("{:<15}{:<10}{:<15}".format(
#     "Ali",
#     "12",
#     "Standart"
# ))
#
# print("{:<15}{:<10}{:<15}".format(
#     "John",
#     "25",
#     "Lyuks"
# ))
#
# print("{:<15}{:<10}{:<15}".format(
#     "Doe",
#     "8",
#     "Ekonom"
# ))
# person = {
#     "name":"Ali",
#     "age":25
# }
#
# print("Ism: {name}, Yosh: {age}".format(**person))

# Mexmonxona usuli

# print("{:<18} {:<25} {:<20}".format(
#     "Ismi",
#     "Xonasi",
#     "Xona turi"
# ))
# print("-"*65)
#
# d = {
#     "John":["12","Standart"],
#     "Doe":["15","Lyuks"],
#     "Ali":["7","Ekonom"]
# }
#
# for name, info in d.items():
#     print("{:<18} {:<25} {:<20}".format(
#         name,
#         info[0],
#         info[1]
#     ))

# OOP (Object-Oriented Programming) да meros olish

# class Mashina:
#
#     def gaz(self):
#         print("Mashina yurmoqda...")
#
#     def tormoz(self):
#         print("Mashina to'xtadi.")
#
# car = Mashina()
#
# car.gaz()
#
# car.tormoz()

# Абстракция нима?

# Абстракция — фойдаланувчига фақат керакли функцияларни кўрсатиш, ички мураккаб ишлаш жараёнини яширишдир.
# "Қандай ишлаши эмас, нима қилишини билиш кифоя."

# OOP 4 ta asosiy prinsipi 1-Abstraction

# class Car:
#     def start(self):
#         print("Mashina ishga tushdi")
#
# car = Car()
# car.start()

# 2- si Encapsulation

# Malumotlarni ximoya qilish va ularni togridan togri kirishini cheklash

# class Bank:
#
#     def __init__(self):
#         self.__balance = 100000
#
#     def deposit(self, money):
#         self.__balance += money
#
#     def get_balance(self):
#         return self.__balance
# bank = Bank()
#
# bank.deposit(5000)
#
# print(bank.get_balance())

# Inheritance bu meros olsih

# class Odam:
#     def salom(self):
#         print("Assalomu alaykum")
#
# # Talaba klassi Odam klassidan tashqarida bo'lishi kerak
# class Talaba(Odam):
#     pass
#
# # Obyekt yaratamiz va tekshiramiz
# t = Talaba()
# t.salom()  # Konsolga: Assalomu alaykum

# Polymorphism bu bir xil metod xar xil obektlarda turlicha ishlaydi.

# class Mushuk:
#
#     def ovoz(self):
#         print("Miyov")
#
# tom = Mushuk()
#
# tom.ovoz()

# class It:
#
#     def ovoz(self):
#         print("Vov")
#
# sharik = It()
#
# sharik.ovoz()

# Ota klass - barcha hayvonlar uchun umumiy shablon
# class Hayvon:
#     def __init__(self, ism):
#         self.ism = ism

    # def ovoz(self):
    #     # Bu metod ota klassda shunchaki e'lon qilinadi,
    #     # har bir bola klass uni o'ziga moslab qayta yozishi (override qilishi) shart
    #     pass

# Mushuk klassi Hayvon klassidan vorislik oladi
# class Mushuk(Hayvon):
#     def ovoz(self):
#         return f"{self.ism}: Miyov"

# # It klassi Hayvon klassidan vorislik oladi
# class It(Hayvon):
#     def ovoz(self):
#         return f"{self.ism}: Vov"


# # 1. Turli hayvonlarning obyektlarini yaratamiz (ism bergan holda)
# animals = [
#     Mushuk("Tom"),
#     It("Sharik"),
#     Mushuk("Mura"),
#     It("Рeks")
# ]

# # 2. Polimorfizm yordamida sikl ichida ishlatamiz
# for animal in animals:
#     print(animal.ovoz())


# Ota klass - barcha transportlar uchun umumiy shablon
# class Transport:
#     def __init__(self, nom):
#         self.nom = nom

#     def yur(self):
#         # Bu metod ota klassda shunchaki e'lon qilinadi
#         pass


# class Car(Transport):
#     def yur(self):
#         return f"{self.nom} mashinasi yo'lda yurmoqda."


# class Bicycle(Transport):
#     def yur(self):
#         return f"{self.nom} velosipedi pedal yordamida yurmoqda."


# class Plane(Transport):
#     def yur(self):
#         return f"{self.nom} samolyoti osmonda uchmoqda (yurmoqda)."



# transports = [
#     Car("Chevrolet Malibu"),
#     Bicycle("Sport-X"),
#     Plane("Boeing 747"),
#     Car("Tesla Model S")
# ]

# for transport in transports:
#     print(transport.yur())

# Кўпчилик "полиморфизм" деганда фақат мерос (inheritance) ни ўйлайди.
# Лекин асосий ғоя мерос эмас,
# бир хил интерфейс орқали турли объектлар билан ишлай олиш

# ------test savol javoblar------

# 1- Instance Method bu aniq bir obekt bilan ishlaydi (instance)

# class Car:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         print(self.name)
# c = Car("Malibu")
# c.info()

# 2- Class Method obekt emas bu @classmethod bilan ishlaydi

# class Car:
#
#     count = 0
#
#     @classmethod
#     def show_count(cls):
#         print(cls.count)
# Car.show_count()

# 3- Static Method bu oddiy funksiya

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b

# Natijani ekranga chiqaramiz
# print(Math.add(5, 3))  # Konsolga: 8

# Public bu xamma joyda ishlagtiladi

# class Employee:
#
#     def __init__(self):
#         self.__salary = 5000
#
#     def get_salary(self):
#         return self.__salary
#
# emp = Employee()
#
# print(emp.get_salary())  #Getter

# Getter  bu qiymat faqat oqiydi

# class Employee:

#     def __init__(self):
#         self.__salary = 5000

#     def get_salary(self):
#         return self.__salary

# emp = Employee()

# print(emp.get_salary())

# Setter bu qiymat xafsiz ozgartiradi

# class Employee:
#     def __init__(self):
#
#         self.__salary = 5000
#
#     # GETTER metod - oylikni xavfsiz ko'rish uchun
#     def get_salary(self):
#         return self.__salary

#     # SETTER metod - oylikni shart asosida o'zgartirish uchun
#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Xatolik: Oylik miqdori 0 dan katta bo'lishi kerak!")


# ---- Kodni tekshiramiz ----

# emp = Employee()
#
# # 1. Dastlabki oylikni ko'ramiz
# print("Eski oylik:", emp.get_salary())
#
# # 2. Oylikni noto'g'ri qiymatga o'zgartirishga urunib ko'ramiz
# emp.set_salary(-1500)  # Konsolga xatolik matni chiqadi
# print("O'zgarmagan oylik:", emp.get_salary())
#
# # 3. Oylikni to'g'ri qiymatga o'zgartiramiz
# emp.set_salary(7500)
# print("Yangi oylik:", emp.get_salary())

# umumiy 26 darsdan olgan xulosamiz
# Instance Method bu -self obekt bilan ishlaydi
# Class Method bu - cls klas bilan ishlaydi
# Static Method bu - xech biri bilan ishlamaydi
# Public bu - xammaga ochiq
# Protected bu - ichki foydalanish uchun tafsiya
# Private bu - ma`lumot yashiradi (__name)
# Getter bu -qiymat oqiydi
# Setter bu -qiymat tekshirib ozgartiradi
