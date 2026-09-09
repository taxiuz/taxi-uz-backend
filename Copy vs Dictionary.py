# Copy vs Dictionary
from itertools import count

# a = [1,2,3]
# b = a
#
# print(a)     #referens count 2


# a = [1,2,3]
# b = a
# b = a.copy()
#
# print(a)    #b = a qilinganda, b va a xotiradagi aynan bitta ro‘yxatga ko‘rsatkich (pointer) bo‘lib bog‘lanadi.

# a = [1,2,3]
# b = a
# b.append(4)

# print(a)            #id(a) == id(b) !

# a = [1,2,3]
# b = a.copy()
# b.append(4)
#
# print(a)       #print(a) o‘zining asl holatini saqlab qoladi.

import copy

# a = [1, 2, 3]
# b = a
#
# b.append(4)
#
# print(a)

# a = [1, 2, 3, [4, 5]]
# b = copy.deepcopy(a)  # Chuqur nusxa yaratish

# b[3].append(6)

# print(a)  # Natija: [1, 2, 3, [4, 5]] — Endi asos o'zgarmasdan qoldi!
# print(b)  # Natija: [1, 2, 3, [4, 5, 6]]

# a = [[1], [2]]
#
# b = a.copy()
#
# b[0].append(99)
#
# print(a)      #[[1, 99], [2]]


# a = [1, 2, 3, [4, 5]]
# b = a.copy()
#
# b[3].append(6)
#
# print(a)   #shallow copy yuzaki kopiya

# import copy
#
# a = [1, 2, 3, [4, 5]]
#
# b = copy.deepcopy(a)
#
# b[3].append(6)
#
# print(a)      #deep copy chuqur kopiya


# import copy
#
# a = [1, 2, 3, [4, 5]]
# b = copy.deepcopy(a)  # Chuqur nusxa yaratish
#
# b[3].append(6)
#
# print(a)  # Natija: [1, 2, 3, [4, 5]] — Endi asos o'zgarmasdan qoldi!
# print(b)  # Natija: [1, 2, 3, [4, 5, 6]]

# from copy import deepcopy
#
# a = [1, 2, 3, [4, 5]]
# b = deepcopy(a)
#
# # Tashqi ro'yxatlar manzili har xil
# print(id(a) == id(b))        # False
#
# # Ichki ro'yxatlar manzili ham endi butunlay boshqa-boshqa!
# print(id(a[3]) == id(b[3]))  # False

# from copy import deepcopy #import asosan  Professional kod  import tepasida yoziladi!

# a = [1, 2, 3, [4, 5]]

# b = deepcopy(a)

# b[3].append(6)

# print(a)
# print(b)

# shart bloki

# if x > 0:
#     print("Musbat")   #conditional block blok if/elif/else orqali ishlaydi

# Takrorlash bloki

# for i in range(5):
#     print(i)        #loop block

# Funksiya bloki

# def salom():
#     print("Salom")   #function block

# bularni indentation (chekinish) orqali ajratadi:

# if True:
#     print("Ichki blok")
#
# print("Tashqi blok")

#algoritm va malumotlar strukturasi hash table ->dict Dictionary nima?

# user = {
#     "name": "Alisher",
#     "age": 30,
#     "job": "Developer"
# }
# user = ["Alisher", 30, "Developer"]
#
# print(user)


# car = {
#     "brand": "BMW",
#     "year": 2026
# }

# print(car["brand"])

# Arena
#  └── Pool
#       └── Block #shunday ishlaydi

# a = [1,2,3]
# del a
# pymalloc allocator ishlaydi

# id([1, 2, 3]) == id([4, 5, 6])


# a = [1,2,3]
# del a
#
# b = [4,5,6]

# a = [1, 2, 3]
# eski_manzil = id(a)  # a ning manzilini yozib olamiz
#
# del a  # O'chirdik, manzil Free-List'ga tushdi
#
# b = [4, 5, 6]
# yangi_manzil = id(b)  # b olgan manzilni tekshiramiz
#
# print(eski_manzil == yangi_manzil)

#CRUD - Crete - Read - Update -Delete

# "hash table"  "->dict"  {} va dict() tezligini solishtirish uchun

# import timeit
#
# # {} literalini 10 million marta sinab ko'ramiz
# vaqt_literal = timeit.timeit("x = {}", number=10_000_000)
#
# # dict() konstruktorini 10 million marta sinab ko'ramiz
# vaqt_konstruktor = timeit.timeit("x = dict()", number=10_000_000)
#
# print(f"{{}} usuli: {vaqt_literal:.4f} soniya")
# print(f"dict() usuli: {vaqt_konstruktor:.4f} soniya")

# dictionary == another_dictionary  True -Qiymati va turi bir xil
# dictionary is another_dictionary  False -Xotirada mutlaqo boshqa-boshqa manzillarda yashaydi

# d = {"ism":"Nodir","yoshi": 23}
# d2 = dict(ism="Nodir",yoshi=23)
# d3 = dict([("ism","Nodir"), ("yoshi",23)])
# print(d)
# print(d2)
# print(d3)
#bu yerda datani ozini yaratishni organdik

# d = {"ism":"Nodir","yoshi": 23}
# d2 = dict(ism="Nodir",yoshi=23)
# d3 = dict([("ism","Nodir"), ("yoshi",23)])
# d["bal"] =[5,4,3,2]
# print(d["bal"])
# print(d2)
# print(d3)

# kay mavzusi

#1
# duplicated_keys = {"key1": "value1", "key1": "value2","key1": "value3"}
#
#
# print(duplicated_keys["key1"])

#2
# d = {}
#
# d["key1"] = "value1"
# d["key1"] = "value2"
# d["key1"] = "value3"
#
# print(d)

#3
# data = {
#     "key1": ["value1", "value2", "value3"]
# }
#
# print(data["key1"])

#1
# harry_potter_dict = {
#     "Harry Potter": "Gryffindor",
#     "Ron Weasley": "Gryffindor"
# }
#
# add_characters_1 = {
#     "Albus Dumbledore": "Gryffindor",
#     "Luna Lovegood": "Ravenclaw"
# }
#
# harry_potter_dict.update(add_characters_1)
#
# print(harry_potter_dict)

#2
# a = {
#     "Ali": 20
# }
#
# b = {
#     "Ali": 25,
#     "Vali": 30
# }
#
# a.update(b)
#
# print(a)


#3

# d = {}
#
# d["key1"] = "value1"
# d["key1"] = "value2"
# d["key1"] = "value3"      #key bir xil bolsa boshqa turini olamaiz
#
# print(d)

#4

# d = {}
#
# print(d["x"])    #eror beradi

#5

# from collections import defaultdict
#
# default_d = defaultdict(list)
#
# print(default_d["missing_key"])   #bosh list qaytaradi

# 6

# for i in range(1, 6):
#     default_d["missing_key"].append(f"value{i}")
#
# print(default_d["missing_key"])     #value1 2chi aylanishda value1 value2 qaytaradi

# 7

# from collections import defaultdict
#
# students = defaultdict(list)
#
# students["Python"].append("Ali")
# students["Python"].append("Vali")
# students["Java"].append("Hasan")
#
# print(students)             #defaultdict(<class 'list'>, {'Python': ['Ali', 'Vali'], 'Java': ['Hasan']})

# ------------------------------------------------------------------------------------------------------------
# Vazifa uyga CRUD (Create, Read, Update, Delete)

# Qiymat olish

# user = {
#     "name":"Ali",
#     "age":25
# }
# print(user ["name"])  #natija Ali

# user = {
#     "name": "Ali",
#     "age": 25
# }
#
# print(user["job"])      #xato eror beradi

# user = {
#     "name": "Ali",
#     "age": 25
# }
#
# # 1. Agar kalit bo'lmasa, None qaytaradi
# print(user.get("job"))         # Natija: None
#
# # 2. Agar kalit bo'lmasa, default qiymat qaytaradi
# print(user.get("job", "Ishsiz")) # Natija: Ishsiz

# if "job" in user:
#     print(user["job"])
# else:
#     print("Kechirasiz, 'job' kaliti mavjud emas.")


# try:
#     print(user["job"])
# except KeyError:
#     print("Xatolik ushlab qolindi: Bunday kalit yo'q!")

# user = {
#     "name": "Ali",
#     "age": 25
# }
#
# ochirilgan = user.pop("age", None)
#
# print(ochirilgan)
# print(user)         #pop metodi

# To'g'ri lug'at ko'rinishida update qilish

# user = {
#     "name": "Ali",
#     "age": 25
# }
#
#
# user.update({
#     "city": "Toshkent",
#     "job": "Developer",
#     "age": 30
# })
#
# print(user)

# user = {
#     "name": "Ali",
#     "balance": 100
# }
#
# # Read
# print(user.get("balance", 0))
#
# # Update
# user.update({
#     "balance": 150,
#     "status": "active"
# })
#
# # Delete
# user.pop("status", None)
#
# print(user)


# -------------------Test bajaramiz-------------------------------
#1

# a = b ko‘rinishida nusxa olinsa nima sodir bo‘ladi?


# a = [1, 2, 3]

# b = a             #ikkala obektxam bitta obektga boglanadi yani:[1, 2, 3]ga

# b.append(4)

# print(a)          #osha javop shunday ishlatamiz [1, 2, 3, 4]

# a = [1,2,3]

# b = a.copy()

# b.append(4)

# print(a)
# print(b)         #yuqorida bajargan formulamiz copiya qilish metodi

# 2
# dict.copy() (shallow copy) metodining asosiy xususiyati nima?

# a = {
#     "ism": "Ali",
#     "hobbiy": ["sport", "kitob"]
# }
#
# b = a.copy()              #copy() → 1 qatlam nusxa (shallow)
# b["hobbiy"].append("kino")
#
# print(a)

# a = {
#     "ism": "Ali",
#     "hobbiy": ["sport", "kitob"]
# }

# import copy

# b = copy.deepcopy(a)    #deepcopy() → hamma qatlam nusxa

# print(a)

# mutable (list, dict) va immutable (str, int) farqlash muxim xisoblanar ekan.

# 3

# Murakkab ichma ich joylashgan obektga bir biriga bogliq bolmagan xolda toqliq nusxalash

# import copy

# user_data = {
#     "name": "Ali",
#     "skills": ["Python", "Django"]
# }

# new_data = copy.deepcopy(user_data)

# new_data["skills"].append("FastAPI")

# print(user_data["skills"])
# print(new_data["skills"])

#QUYIDAGI KODNI JAVOBI NIMA

# d1 = {'a': [1, 2]}
# d2 = d1.copy()
# d2['a'].append(3)
# print(d1['a'])     #natija [1, 2, 3]

# from copy import deepcopy

# d1 = {'a': [1, 2]}
# d2 = deepcopy(d1)  # Chuqur nusxa!

# d2['a'].append(3)

# print(d1['a'])
# print(d2['a'])   # Natija: [1, 2] —— Asl holati saqlanib qoldi!N: [1, 2, 3]

# lugat ichida kalit va qiymatlarini  juftliklarni korish uchun qaysi metod ishlatiladi

# user = {"name": "Ali"}
#
# barcha_juftliklar = user.items()
#
# # Lug'atga yangi element qo'shamiz
# user["age"] = 25
#
# print(barcha_juftliklar)          #natihja Yangi element avtomatik ravishda aks etdi!


# user = {"name": "Ali"}
#
# barcha_juftliklar = list(user.items())
#
# user["age"] = 25
#
# print(barcha_juftliklar)     #Yangi element ro‘yxatda aks etmadi!

#lugatdan ochirish clear ishlatilishi


# user = {"name": "Ali", "age": 25}
#
# user.clear()
#
# user["city"] = "Toshkent"
#
# print(user)         #user.clear() Tozalash va Yangi Ma'lumot Qo‘shish

# user = {"name": "Ali", "age": 25}
#
# user.clear()
#
# print(user)        #butunlay tozalaydi Tozalash va Tekshirish



