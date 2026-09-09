# 1 Python Sets  NATIJA yaratilish {'apple', 'banana', 'cherry'}


# myset = {"apple", "banana", "cherry"}

# print(myset)

# 2Set xususiyatlari Unordered (tartibsiz) {'cherry', 'banana', 'apple'} bu yerda index yuq

# s = {"apple", "banana", "cherry"}

# print(s)

# 3 Unchangeable (element o‘zgarmaydi)  s.add("orange")

# s = {"apple", "banana"}

# s.add("orange")        #s[0] = "orange" xati beradi

# 4 Duplicate yo‘q Bir xil qiymatni saqlamaydi  {'apple', 'banana'} apple bitta qoladi

# s = {
#     "apple",
#     "banana",
#     "apple"

# }
# print(s)

# {True, 2} qaytaradi bu yerda


# s = {True, 1, 2}

# print(s)

# Set uzunligi  len():

# s = {"a", "b", "c"}

# print(len(s))

# Set ichidagi data turlari va set ichida bitta tuzoq bor mutable ishlaydi imutable ishlamaydi

# s = {
#     "Ali",
#     25,
#     True
# }
#
# print(s)

# type()  set obyektlari set data type (ma’lumot turi) sifatida aniqlanadi,set yaratganingizda uning turi set bo‘ladi

# myset = {"apple", "banana", "cherry"}

# print(type(myset))

# a = ["apple", "banana"]

# print(type(a))

# c = {
#     "name": "Ali"
# }
#
# print(type(c))

# d = {"apple", "banana"}
#
# print(type(d))

# x = {}
#
# print(type(x))

# x = set()
#
# print(type(x))

# ----------------------------------------

# 1 savol set yaratish uchun qanday usuldan foydalanamiz?

# s = {1, 2, 2, 3}

# print(s)

# 2 savol agar toplamga add element qoshsak nima boladi?

# s = {"apple", "banana"}
# s.add("orange")
# print(s)

# 3 savol  remove() va discard() ikalasini farqi nimada?

# id="5u2z0q"
# s = {"apple", "banana", "cherry"}

# s.remove("banana")   #remove xam ochiradi farqlari ...element bolmasa key error beradi.

# print(s)

# id="4h8n3p"
# s = {"apple", "banana", "cherry"}

# s.discard("banana")    #discard ochiradi agar element bolasa hechnarsa qilmaydi

# print(s)

# s = {"Python", "Django"}
#
# # 1 remove()
# s.remove("Python")
#
#
# # 2 discard()
# s.discard("Django")
# s.discard("FastAPI")
#
# print(s)

# toplamda tasodifiylik randomnes

# s = {"Python", "Django", "FastAPI"}

# .pop() o'chirilgan elementni qaytaradi

# sug_urilgan_element = s.pop()

# print(sug_urilgan_element)
# print(s)

# shu kotda natijani aniqlang:{3}

# set1 = {1,2,3}
# set2 = {3,4,5}
# set1.intersection_update(set2)
# print(set1)


# ---------------trenirovka-----------------------

# thisset = {"apple","banana","chery"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)   #False"1" qaytardi xar soraganimda boshqa tartib bermoqda

# thisset = {"apple", "banana", "cherry", False, True, 0}
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# print(len(thisset))   #sanoq 3


# Access Items

# thisset = {"apple", "banana", "cherry"}
#
# for x in thisset:
#     print(x)         #bu yerda tartibga ishonch yoq

