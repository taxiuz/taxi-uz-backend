# Kod va Natija

# def prime_generator():
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
# primes = prime_generator()
# for _ in range(6):
#     print(next(primes))

# Generatorka va kombinatorka?

# import itertools
#
# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         yield "".join(pwd)
#
# input_string = "abs"
# passwords = password_generator(input_string)
#
# for _ in range(6):
#     print(next(passwords))

# bu ichida 2 ta print bor tekshirish uchun

# import itertools
# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         print((pwd))
#         yield "".join(pwd)
# input_string = "abs"
# passwords = password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))

# cheksiz fibonachi sozlarini generatsiya qilish

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fibonacci = fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))

# list elemet;larini guruhlash

# import itertools
# def group_generator(lst, n):
#     for group in itertools.combinations(lst, n):
#         yield group
# my_list = [1, 2, 3, 4]
# n = 2
# groups = group_generator(my_list, n)
#
# for group in groups:
#     print(group)

# import itertools
# def group_generator(lst, n):
#     for group in itertools.combinations(lst, n):
#         yield group
#
# my_list = [1, 2, 3, 4]
# n = 2
# groups = group_generator(my_list, n)
# for group in groups:
#     print(group)

# def group_generator(lst, n):
#         if n == 0:
#         yield ()
#         return
#
#     for i in range(len(lst)):
#         current_element = lst[i]
#
#         remaining_elements = lst[i + 1 :]
#         for next_group in group_generator(remaining_elements, n - 1):
#             yield (current_element,) + next_group
#
# my_list = [1, 2, 3, 4]
# n = 2
# groups = group_generator(my_list, n)
# for group in groups:
#     print(group)

# ------------------Closures-------------

# def tashqi_funksiya(x):
#     def ichki_funksiya(y):
#         return x + y
#
#     return ichki_funksiya
#
#
# qo_shish = tashqi_funksiya(10)
#
# print(qo_shish(5))

# Holat saqlash

# def counter():
#     son = 0
#
#     def oshir():
#         nonlocal son
#         son += 1
#         return son
#
#     return oshir
#
#
# c = counter()
#
# print(c())
# print(c())
# print(c())

# a = [4, 5]
# def f1():
#     print(a)
#
# def f2():
#     global a
#     a
#     print(a)
#
# f2()
# print(a)

# a = [4, 5]
# def f1():
#     print(a)
#
# def f2():
#     global a
#     a.append(6)
#     print(a)
# f2()
# print(a)

# a = [4, 5]
# def f1():
#     a.append(6)
#     # print(a)
#
# # def f2():
# #     global a
# #     a.append(6)
# #     print(a)
#
# f1()
# print(a)

# Global scope

# a = 4

# def f1():
#     print(a)

# def f2():
#     global a
#     a -= 1
#     print(a)
# f1()
# f2()
# f1()


# Local Scoble

# a = 10
#
# def f1():
#     print(a)
#
# f1()

# Nomlocal scope

# def f1():
#     a = 4
#
#     def f2():
#         print(a)
#
#     f2()
#
# f1()

# Global Scope  Funksiyalardan tashqarida yaratilgan o‘zgaruvchi.

# a = 10   # Global
#
# def f1():
#     print(a)
#
# f1()
# print(a)

# Local Scope Funksiya ichida yaratilgan o‘zgaruvchi.
# def f1():
#     a = 5   # Local
#     print(a)
#
# f1()

# NameError
# def f1():
#     a = 5
#
# f1()
#
# print(a)

# Nonlocal Scope  Bu ichma-ich funksiyalarda ishlatiladi.

# def tashqi():
#     a = 10
#
#     def ichki():
#         nonlocal a
#         a += 1
#         print(a)
#
#     ichki()
#
# tashqi()

# x = "global"
#
# def f1():
#     x = "local"
#
#     def f2():
#         print(x)
#
#     f2()
#
# f1()

# global bilan chaqirib ichida ozgartirish kirgizsa local deyiladi

# a = 10   # global
#
# def f1():
#     global a
#     a = 20
#     print(a)
#
# f1()
#
# print(a)


# Ozgaruvchiga saqlanishi mumkin

# def salom_ber():
#     return "Assalomu alaykum!"
#
# ko_prik = salom_ber
#
# print(ko_prik())  # Natija: Assalomu alaykum!

# Boshqa funksiyaga argument bo‘lishi mumkin

# def kvadratga_oshir(x):
#     return x**2
#
#
# def amallarni_bajar(funksiya, qiymat):
#
#     return funksiya(qiymat)
# print(amallarni_bajar(kvadratga_oshir, 5))  # Natija: 25

# Return orqali qaytishi mumkin

# def darajaga_oshiruvchi(n):  # Tashqi funksiya
#     def daraja(x):  # Ichki funksiya
#         return x**n  # 'n' o'zgaruvchisini eslab qoladi
#
#     return daraja
#
#
# kubi = darajaga_oshiruvchi(3)
#
# print(kubi(4))  # Natija: 64 (4 ning kubi)

# return a ️ qiymat qaytaradi

# return g ➡ funksiyaning ozini qaytaradi

# Global o‘zgaruvchi

# a = 4  #global a
#
# def f1():
# 	print(a)
#
# def f2():
# 	global a
# 	a+=1
# f1()
#
# f2()
#
# f1()
# print(a)

# Local = funksiya tugashi bilan o‘ladi

# def f1():
#     a = 4  # funksiya chaqirilganda 'a' xotirada tug'iladi
#     print(a)
#
# f1()  # Natija: 4

# Nonlocal Scope

# def f1():
#     a = 4  # f1 uchun local, f2 uchun nonlocal
#
#     def f2():  # ichki funksiya
#         print(a)  # nonlocal o'zgaruvchini o'qish
#
#     f2()  # ichki funksiyani ishga tushiramiz
# # Tashqi funksiyani chaqiramiz
# f1()

# global/local/nonlocal

# def f(x):
#     z = 2
#
#     def g(y):
#         return z*x + y
#
#     return g
# a = 5
# b = 1
# h = f(a)
#Natija:10 + 1 = 11
# print(h(b))

# Free Variables va Bound Variables nima

# def f(x):
#     z = 2
#
#     def g(y):
#         return z * x + y
#
#     return g
#
#
# a = 5
# h = f(a)  # Closure hosil bo'ldi
#
# # Python orqa fonda nimalarni saqlayotganini tekshiramiz:
# print("Erkin o'zgaruvchilar nomlari:", h.__code__.co_freevars)
# print("Xotirada saqlangan 'x' qiymati:", h.__closure__[0].cell_contents)
# print("Xotirada saqlangan 'z' qiymati:", h.__closure__[1].cell_contents)



# def f(x):
#     def g(y):
#         def h(z):
#             return x * y * z
#
#         return h
#
#     return g
#
#
# g_func = f(5)
# h_func = g_func(2)
#
#
# print("g() qaysi freevarlarni biladi:", g_func.__code__.co_freevars)
#
# print("h() qaysi freevarlarni biladi:", h_func.__code__.co_freevars)

# def h(z):
#     return z * 2
#
# print(h.__code__.co_freevars)


# def f(x):
#     def h(z):
#         return x * z
#     return h
#
#
# h = f(5)
#
# print(h.__code__.co_freevars)

# Lambda funksiyalar bilan Closure hosil qilish


# def double(x):
#     return x * 2
#
#
# def add_10(x):
#     return x + 10
#
#
# print(add_10(double(5)))

# def compose(g, f):
#     def h(*args, **kwargs):
#         return g(f(*args, **kwargs))
#
#     return h
#
#
# def double(x):
#     return x * 2
#
#
# def add_10(x):
#     return x + 10
#
#
# composed = compose(add_10, double)
#
# print(composed(5))  # add_10(double(5)) -> add_10(10) -> 20

# def compose(*functions):
#     def composed(x):
#         for f in reversed(functions):
#             x = f(x)
#         return x
#
#     return composed
#
# result = compose(
#     lambda x: x + 3,
#     lambda x: x * 2,
#     lambda x: x - 1
# )
#
# print(result(5))

# def pipeline(*functions):
#     def composed(x):
        # reversed yo'q, funksiyalar yozilgan tartibida ishlaydi
    #     for f in functions:
    #         x = f(x)
    #     return x
    #
    # return composed


# Ma'lumot oqimi tartib bilan o'qiydigan qilib joylashtiriladi:
# o_qim = pipeline(
    # lambda x: x - 1,  # 1-bajariladi: 5 - 1 = 4
    # lambda x: x * 2,  # 2-bajariladi: 4 * 2 = 8
    # lambda x: x + 3,  # 3-bajariladi: 8 + 3 = 11
# )

# print(o_qim(5))  # Natija: 11

# ----------Bugungi darsimizga umumiy xulosa------------

#1- Global Scope

#2-Local Scope

#3- Nonlocal Scope

# Global kalit so‘zi  global a

# a = 4
#
# def f():
#     global a
#     a += 1
#
# f()
# print(a)

# Closure - Ichki funksiya tashqi funksiyaning o‘zgaruvchilarini eslab qolish

# def f(x):
#     def g(y):
#         return x + y
#
#     return g
# add = f(10)
#
# print(add(5))


# Free variables-Funksiya ichida yaratilmagan, tashqaridan olingan o‘zgaruvch

# def f(x):
#     def g():
#         return x
#
#     return g  # ichki funksiyani qaytaramiz
#
#
#
# h = f(100)
#
#
# print(h.__code__.co_freevars)
# print(h.__closure__[0].cell_contents)
# Natija: 100

# Bir necha qatlamli closure

# def f(x):
#     def g(y):
#         def h(z):
#             return x*y*z
#
#         return h
#
#     return g
# print(f(2)(3)(4))

# Natija: 24 (2 * 3 * 4)

# Lambda + Closure

# def make_multiplier(n):
#
#     return lambda x: x * n
#
#
# 1-qadam: f(x) darajasi
# double = make_multiplier(2)
# triple = make_multiplier(3)
#
 # 2-qadam: h(b) darajasi
# print(double(5))  # Natija: 10 (5 * 2)
# print(triple(5))  # Natija: 15 (5 * 3)

# Function Composition

# def compose(f, g):
#     return lambda x: f(g(x))
#
#
# add_1 = lambda x: x + 1
# square = lambda x: x**2
#
#
# yangi_funksiya = compose(square, add_1)
#
# print(yangi_funksiya(4))

# Natija 25


# --- o‘zgaruvchiga beriladi
# ---argument sifatida uzatiladi
# ---return orqali qaytariladi
# --- boshqa funksiyalarni eslab qoladi
# ----yangi funksiyalar yaratadi


# --------Rahmat----------

-------Test---------

# 1 savol Funksiya Closure" bo'lishi uchun quyidagi shartlardan qaysi biri majburlik EMAS?

# Tashqi funksiya ichki funksiyani qaytarishi (return) shart, aks holda tashqi funksiya tugagach ichki muhit yo'qoladi.

# 2 savol Closures xotiraning qaysi xususiyatidan foydalanadi?

# Funksiya kamida 2 ta argument qabul qilishi shart emas,Non-local scope xususiyatidan foydalanadi

# 3 savol quyidagi kod nima natija qaytaradi?

# def tashqi(x):
#     def ichki(y):
#         return x + y
#
#     return ichki
#
#
# f = tashqi(10)
#
# print(f(5))
#
# Natija:15

# 4 savol Ichki funksiya tashqi funksiyadan "meros" qilib olgan o'zgaruvchilar qayerda saqlanadi?

# __closure__ atributi ichida

#5- savol  Closures nima uchun ishlatiladi?
# Ma’lumotlarni yashirish (Data encapsulation) va funksiya fabrikalarini yaratish uchun ishlatiladi

# 6- savol Funksiya ichida yaratilgan va faqat o'sha funksiya ichida ishlatilishi mumkin bo'lgan o'zgaruvchi nima deyiladi?

# Lokal = funksiya ichida tug'iladi va funksiya ichida o'ladi -Lokal o‘zgaruvchi


# 7-savol Funksiya ichidan turib, funksiya tashqarisidagi (global) o‘zgaruvchining qiymatini o‘zgartirish uchun qaysi kalit so‘z ishlatiadi?
# javob global


# 8-savol nonlocal kalit so‘zi qaysi holatda ishlatiladi?

# Ichma-ich joylashgan funksiyalarda, ichki funksiyadan turib tashqi funksiya o‘zgaruvchisini o‘zgartirish uchun

# 9 savol quyidagi kodni javobi nima


# x = 100
#
# def funksiya():
#     x = 10
#     print(x)
#
# funksiya()
# print(x)

# natija 10 100

