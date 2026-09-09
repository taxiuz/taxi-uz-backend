# vaifa  Xanoy minoralari
#
# def hanoi(n, source, target, auxiliary):
#
#     # Base Case
#     if n == 1:
#         print(f"Disk 1 ni {source} ustundan {target} ustunga ko'chiring")
#         return
#
#     hanoi(n - 1, source, auxiliary, target)
#
#     print(f"Disk {n} ni {source} ustundan {target} ustunga ko'chiring")
#
#     hanoi(n - 1, auxiliary, target, source)
#
#
# hanoi(3, 'A', 'C', 'B')


# boshqa varyanti

# def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
#
#     if n == 1:
#         print("Move disk 1 from rod", from_rod, "to rod", to_rod)
#         return
#
#     TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
#
#     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
#
#     TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
#
#
# n = int(input("Enter the number of disk: "))
#
# TowerOfHanoi(n, 'A', 'C', 'B')

# def countdown(n):
#     if n == 0:
#         return
#
#     print(n)
#     countdown(n-1)

# def countdown_reversed(n):
#     if n == 0:
#         return
#
#     countdown_reversed(n - 1)
#
#     print(n)

# def try_generator(y):
#     n = y
#     n += 1
#     print("Performed addition")
#     yield n
#
#     n *= 2
#     print("Performed multiplication")
#     yield n
#
#
# result = try_generator(5)
# print(next(result))
# print(next(result))


# def return_squared(min, max):
#     for i in range(min, max):
#         yield i**2
#
#
# result = return_squared(1, 5)
#
# for item in result:
#     print(item)

# ------------------------savol javop 4ta-----------

# 1 Har safar chaqirganda kegingi tub sonni generatsiya qiladigon generator yarating?

# def tub_son_generator():
#     son = 2
#
#     while True:
#         tub = True
#
#         for i in range(2, son):
#             if son % i == 0:
#                 tub = False
#                 break
#
#         if tub:
#             yield son
#
#         son += 1
#
#
# gen = tub_son_generator()
#
# for i in range(6):
#     print(next(gen))

# 2 kiritilgan malumotlardan generator parol yarating/?

# def parol_generator(s):
#     if len(s) == 1:
#         yield s
#         return
#
#     for i in range(len(s)):
#         belgi = s[i]
#
#         qolgan = s[:i] + s[i+1:]
#
#         for p in parol_generator(qolgan):
#             yield belgi + p
#
#
# for p in parol_generator("abs"):
#     print(p)

# 3 cheksiz fibonachi generatsiya qiladigon generator yararting?

# def fibonacci():
#     a = 0
#     b = 1
#
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# fib = fibonacci()
#
# for i in range(8):
#     print(next(fib))

# 4 List elementlarini n tadan guruhlash generator

# def guruh_generator(lst, n):
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             yield (lst[i], lst[j])
#
#
# my_list = [1,2,3,4]
#
# for guruh in guruh_generator(my_list, 2):
#     print(guruh)

# --------------Test--------------------------------

# 1-Interator bolishi uchun qaysi ikki metod bolishi kerak?

# __iter__ va __next__ bolishi shart

# buninng sabababi iterator obyektini qaytaradi-__iter__().
# Next bu kegingi obekt qaytaradi-__next__().

# 2-Generator orniga return ishlatish uchun qaysi  kalit sozidan foydalanasiz?
# Javob:yield qiymatni beradi va funksiyaning holatini saqlab qoladi.

# import math
#
# def tub_son_generator_tezkor():
#     son = 2
#     while True:
#         tub = True
#         # Faqat kvadrat ildizigacha tekshiramiz
#         for i in range(2, int(math.isqrt(son)) + 1):
#             if son % i == 0:
#                 tub = False
#                 break
#         if tub:
#             yield son
#         son += 1
#
# gen = tub_son_generator_tezkor()
#
# for i in range(10):
#     print(next(gen))

# 3- Interatorni barcha elementlarini tugaganidan kegin next() funksiyada qanday xatolik qaytaradi?

# lst = [1,2]
#
# it = iter(lst)
#
# print(next(it))
# print(next(it))
# print(next(it))

# Generator va oddiy funksiya o‘rtasidagi asosiy farq nima?

# 4- Generator va oddiy funksiya ortasida nima farq bor?

# Generator ishni toxtatgan joydan davom etirib keta oladi va saqlaydi!

# 5-quyidagi ifoda nima dep ataladi? gen = (x**2 for x in range(5))
# () qavs ichida for ishlatilsa va yield yozilmasa — bu generator expression bo‘ladi.

# 6-Generatorning afzalligi nimada?

# U xotirani tejaydi  Generator barcha qiymatlarni birdan yaratmaydi, kerak bolganda bittadan beradi.

# 7- iter() funksiyasini vazifasi nima?

# "Interable"  (Royxatni satr) obektiga iterator olish

# lst = [1,2,3]

# it = iter(lst)

# print(next(it))

# 8- Nima uchun generatorlarda len() funksiyasini ishlatib bolmaydi?

# Ular hali hisoblanmagan va uzunligi nomalum ("oqim")(stream) hisoblanadi

# 9- Generator ichida yield necha marta ishlatilishi mumkin?
# istalgancha olish mumkin

# 10-Generator obyektdan malmot olishning eng keng tarqalgan usuli qaysi?

# gen = (x for x in range(5))
#
# for i in gen:
#     print(i)

----------------Rahmat_____________

| #  | Konsept                | To‘g‘ri qoida                   | Mantiq                                                                                     |
| -- | ---------------------- | ------------------------------- | ------------------------------------------------------------------------------------------ |
| 1  | Iterator yaratish      | `__iter__` va `__next__`        | Iterable obyekt `iter()` orqali iteratorga aylanadi, `next()` esa keyingi qiymatni beradi. |
| 2  | Generator kalit so‘zi  | `yield`                         | `return` funksiyani tugatadi, `yield` esa qiymat berib, holatni saqlaydi.                  |
| 3  | Element tugaganda xato | `StopIteration`                 | `next()` boshqa element topmasa shu signalni beradi. `for` uni avtomatik ushlab qoladi.    |
| 4  | Asosiy farqi           | Holatni saqlab davom etadi      | Generator qayerda to‘xtaganini eslab qoladi.                                               |
| 5  | Dumaloq qavsli for     | Generator Expression            | `[]` → list comprehension, `()` → generator expression.                                    |
| 6  | Asosiy afzalligi       | Xotira tejash (Lazy evaluation) | Qiymatlar oldindan emas, kerak bo‘lganda yaratiladi.                                       |
| 7  | `iter()` vazifasi      | Iterable → iterator             | Masalan listni `next()` bilan boshqarish mumkin bo‘ladi.                                   |
| 8  | `len()` ishlamasligi   | Generator uzunligi saqlanmaydi  | Chunki elementlar hali yaratilmagan bo‘lishi mumkin.                                       |
| 9  | `yield` soni           | Istalgancha                     | Bir generator ichida ko‘p marta ishlatilishi mumkin.                                       |
| 10 | Ma’lumot olish         | `for` sikli orqali              | `for` ichida `next()` avtomatik chaqiriladi.                                               |

Iterator:
__iter__ + __next__

Generator:
yield

Olish:
next()

Ko‘p
ishlatilishi:
for

Tugashi:
StopIteration
-----------------
gen = (x for x in range(3))

print(next(gen))
print(next(gen))