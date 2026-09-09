# ✅ pythonda ma'lumot turlari - data types ✅ Sonlar va ular ustida amallar
from typing import Tuple

# a = 5
# b = 5//2  #2 tabutun son bor bu yerda natija 2
# print(b)

# a = 5
# c = a % 2  # bu yerda qoldiq xisoblanadi
# print(c)

# a = 5
# b = 7/3  # bu yerda qoldiqlik bolish
# print(b)

# a = 5
# b = 5 ** 5
# print(a)  #natija 5
# print(b)  #natija 3125

# a = 4
# b = 3
# print(a ** b)  #natija64
# print(b ** a)  #natija 81

# a = 2
# b = 5
# print(a ** b)   #32 natoja
# print(b ** 2)   #25 natija
# print(10 % 3)   #1 natija
# print(10 // 3)  #3 natija

# a = 5.2
# c = a ** 2  #natija:27.040000000000003
# print(c)

# son  = 24  #variable
# s = 30  # int - integer - butun son
# print(son)
# print(type(son))


# son = 24
# son = 30
# son2 = 3.2
# print(type(son2))  #kasr float

# savatcha = [1,2,3,567,-1,0]  #list
# print(savatcha[2])

# savatcha = [1,2,3,567,-1,0]  #list
# print(savatcha[0])

# matn = 'salom'
# matn2 = "salom"
# print(matn)
# print(matn2)

# matn = 'o`zbekistion'
# matn2 = "o`zbekiston"
# print(matn)
# print(matn2)

# matn = 'o`zim'
# matn2 = "o`zim"
# matn3 = """O'zbekisnon vatanim
#  manin
#  o`zbekiston vatanim manim"""
# print(matn)
# print(matn2)
# print(matn3)

# ifoda = True  #rost
# ifoda2 = False  #yolgon
# print(type(ifoda)) #boolean - bool- mantiqiy malumot turi

# int - butun sonlar uchun
# float - kastr sonlar uchun
# str - matnlik malumotlar uchun
# bool - rost yoki yolgon uchun
# list - ichiga xammasi kiradi sig`di

#Metodlar string methodis
# Method — bu obyektga tegishli bo'lgan funksiya.

# ism = "alisher"

# print(ism.upper())

# 1. upper() -- bu barcha harflarini kattaga aylantirib beradigon funksiya

# matn = "python"

# print(matn.upper())

# 2. lower() -- Barcha harflarni kichik qiladi.

# matn = "PYTHON"

# print(matn.lower())

# 3. capitalize() -- Birinchi harfni katta qiladi.

# ism = ("alisher")

# print(ism.capitalize())

# 4. title() -- Har bir so'zning birinchi harfini katta qiladi.

# matn = "paython dasturlash tili o`rgandim bunga juda qiziqaman"

# print(matn.title())

# 5. strip() -- Boshi va oxiridagi bo'sh joylarni olib tashlaydi.

# 6. replace() -- Matnni almashtiradi.

# matn = "Men Pythonni yaxshi ko'raman"

# print(matn.replace("Python", "Java"))

# 7. find() -- Qidiradi.

# matn = "Paython"

# print(matn.find("x"))

# matn = "Paython"

# print(matn.find("t"))

# 8. count() -- Nechta ekanini sanaydi.

# matn = "banana"

# print(matn.count("a"))

# 9. startswith() -- Boshlanishini tekshiradi. True qaytishi rost yoki yolgon

# ism = "Alisher"

# print(ism.startswith("Ali"))

# 10. endswith() -- Oxirini tekshiradi.

# fayl = ("rasm.jpg")

# print(fayl.endswith(".jpg"))  #True qaytaradi

# misol

# ism = input("Ism: ").strip().capitalize()  # bu kod mexmonxona dasturida qollaganmiz

# input() - foydalanuvchidan ma'lumot oladi.
# .strip() - ortiqcha bo'sh joylarni olib tashlaydi.
# .capitalize() - ismni chiroyli formatlaydi.

# matn = "   python dasturlash   "

# print(matn.strip().title())

# matn = "   pYtHoN DaStUrLaSh   "

# print(matn.strip().lower())
# print(matn.strip().upper())
# print(matn.strip().capitalize())
# print(matn.strip().title())

# txt = "Hello, welcome to my world."

# x = txt.index("welcome")

# print(x)


# txt = "Programming"

# print(txt.index("g"))
# print(txt.find("m"))
# print(txt.index("P"))

# List Metodlar

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(list1)
# print(list2)
# print(list3)

# list1 = ["abc", 34, True, 40, "male"]

# print(list1[0])   # abc
# print(list1[1])   # 34
# print(list1[2])   # True
# print(list1[3])   # 40
# print(list1[4])   # male
# print(list1[-1])  # male
# print(list1[-2])  # 40
# print(list1[-3])  # True

# print(True == 1)    # True
# print(False == 0)   # True

# print(isinstance(True, int))  # True

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))
# print(type(10))          # <class 'int'>
# print(type(3.14))        # <class 'float'>
# print(type("Hello"))     # <class 'str'>
# print(type(True))        # <class 'bool'>
# print(type(["a", "b"]))  # <class 'list'>
# print(type((1, 2)))      # <class 'tuple'>
# print(type({"a": 1}))    # <class 'dict'>
# print(type({1, 2, 3}))   # <class 'set'>

# thislist = list(("apple", "banana", "cherry")) # E'tibor bering: ikki qavat qavs
# print(thislist)

# numbers = (1, 2, 3, 4)
# print(list(numbers))

# 1️- append() --List oxiriga bitta element qo'shadi.

# fruits = ["apple","banana"]
# fruits.append("chery")

# print(fruits)

# 2- extend() --Boshqa list elementlarini qo'shadi.

# fruits = ["apple", "banana"]
# fruits.extend(["orange","kiwi"])

# print(fruits)

# 3- insert() --Belgilang indeksga element qo'yadi.

# fruits = ["apple","banana"]
# fruits.insert(1,"orange")

# print(fruits)

# 4 - remove()  -- Qiymat bo'yicha o'chiradi.

# fruits = ["apple ","banana","cherry"]
# fruits.remove("banana")

# print(fruits)

# 5- pop()-- Indeks bo'yicha elementni o'chiradi va qaytaradi.

# fruits = ["apple", "banana", "cherry"]
# item = fruits.pop(1)

# print(item)
# print(fruits)

# 6-clear() --Barcha elementlarni o'chiradi.

# fruits = ["apple", "banana"]
# fruits.clear()

# print(fruits)

# 7-copy() -- Element necha marta qatnashganini hisoblaydi.

# numbers = [1,2,2,3,2]

# print(numbers.count(2))

# 9-index() -- Elementning indeksini topadi.

# fruits = ["apple","banana","chery"]

# print(fruits.index("banana"))

# 10- sort() --Listni saralaydi.

# numbers = [5, 2, 8, 1]

# numbers.sort()

# print(numbers)

# 11- reverse() -- Elementlar tartibini teskari qiladi.

# numbers = [1, 2, 3]

# numbers.reverse()

# print(numbers)

# mustaqil ish

# fruits = ["apple", "banana", "cherry"]

# fruits.append("orange")   # Element qo'shish
# fruits.remove("banana")   # Elementni o'chirish
# fruits.sort()             # Saralash
# fruits.reverse()          # Teskari tartiblash

# print(fruits)

# Takrorlash vs For sikli

# savol = input("Savol: ").lower()
#
# if "dasturlash" in savol:
#
#     if "python" in savol:
#         print("Siz mentorimiz Komiljonga murojaat qiling")
#
#     if "js" in savol:
#         print("Siz mentorimiz Rashidga savol bering")
#
# if "smm" in savol:
#     print("Siz mentorimiz Alisherga savol bering")
#
# if "mobilograf" in savol:
#     print("Siz mobilograf Komiljonga savol bering")
#
# if "menejer" in savol:
#     print("Siz mentorimiz Abdullo savol bering")

# qoliq qoldiq qaysi kottaligi

# a = 5.4
# b = 3.4
# a1 = a - int(a)
# b1 = b - int(b)
#
# print(a1,b1)

# a = 5.4
# b = 3.4
#
# a1 = abs(a) - int(abs(a))
# b1 = abs(b) - int(abs(b))
#
# if a1 > b1:
#     print("A ning kasr qismi katta")
# elif a1 < b1:
#     print("B ning kasr qismi katta")
# else:
#     print("Ikkalasining kasr qismi teng")
# ----------------

# 1-sikl turlari: For sikli
# 2-sikl turlari: Wile sikli

# mevalar = ["olma", "anor", "nok"]
#
# for meva in mevalar:
#     print(meva,"mevasi")
#     print(meva, "ni olamiz")

#sikl bu har bitta royhatnu ustida elemetlarga birmabir yondashadi ustida

# mevalar = ["olma", "anor", "nok"]
#
# for meva in mevalar:
#
#     print(meva,"mevasi")
#     print(meva, "ni olamiz")
#
#     if meva == "uzum":
#          break

# mevalar = ["olma", "anor", "nok"]
#
# for meva in mevalar:
#
#     print(meva,"mevasi")
#     print(meva, "ni olamiz")
#
#     if meva == "anor":
#          break

# mevalar = ["olma", "anor", "nok"]
#
# for meva in mevalar:
#     if meva == "uzum":
#         continue
#     print(meva, "mevasi")

# talaba = {
#     "ism": "Ali",
#     "yosh": 20,
#     "shahar": "Marg'ilon"
# }
#
# print(talaba)

# yangi element qoshish


# kitob = {
#     "nomi": "Python",
#     "muallif": "Mark Lutz",
#     "narxi": 150000
# }
# meva = {
#     "olma": 12000,
#     "anor": 18000
# }
#
# print(meva["anor"])

# fayllar bilan ishlash

# 1. Getter

# class User:
    # def __init__(self, age):
        # self.__age = age

    # def get_age(self):
        # return self.__age

# user = User(25)

# print(user.get_age())  #natija 25
#
# class User:
#     def __init__(self, age):
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Yosh manfiy bo‘lishi mumkin emas")
#
# user = User(25)
#
# user.set_age(30)

# print(user.get_age())

Sql 



