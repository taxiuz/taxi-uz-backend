# Rekursiv Funksiya darsimizni organamiz

# def factorial(n):
#     if n < 0:
#         raise ValueError("Manfiy sonlarning faktoriali mavjud emas!")
#     if n <= 1:  # Base Case (0 va 1 uchun)
#         return 1
#     return n * factorial(n - 1)

# print(factorial(6))
# 6 × 5 × 4 × 3 × 2 × 1 = 720 #shunday ishlaydi

# Fibonachchi

# def fib(n):
#     # Base Case (Bazaviy holat)
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#     # Recursive Step (O'zidan oldingi ikkita sonni chaqirish)
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(6))  # Natija: 8


# from functools import lru_cache
#
# @lru_cache(maxsize=None)  # Python endi hisoblangan natijalarni eslab qoladi!
# def fib_fast(n):
#     if n < 2:
#         return n
#     return fib_fast(n - 1) + fib_fast(n - 2)
#
# print(fib_fast(100))  # Soniyadan ham kam vaqtda ulkan sonni chiqarib beradi!

# Rekursiya va Iteratsiya

# Fibonachchi misolida
# def fibonacci_rec(n):
#     if n <= 1:
#         return n
#     return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
# # n=40 bo'lsa, kompyuter qiynaladi
#
# # Iterativ usul
#
# def fibonacci_iter(n):
#     if n <= 1:
#         return n
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b
# # n=1000 bo'lsa ham ko'zni ochib yumguncha hisoblaydi!

# def fibonacci(n, cache={}):
#     if n in cache:
#         return cache[n]
#
#     if n == 0:
#         result = 0
#
#     elif n == 1:
#         result = 1
#
#     else:
#         result = fibonacci(n-1) + fibonacci(n-2)
#
#     cache[n] = result
#
#     return result
#
#
# print(fibonacci(50))

# python sortlash

# arr = [4,1,6,2,3,7]
# arr.sort()  #Tim sort
# print(arr)

# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#
#     pivot = lst[0]
#
#     left = [x for x in lst[1:] if x <= pivot]
#
#     right = [x for x in lst[1:] if x > pivot]

    # return quick_sort(left) + [pivot] + quick_sort(right)


# print(quick_sort([4,7,1,2,5,6,3]))

# [4, 7, 1, 2, 5, 6, 3]  (pivot = 4)
#                            /       \
#                           /         \
#               left: [1, 2, 3]     right: [7, 5, 6]
#                 (pivot = 1)         (pivot = 7)
#                  /       \           /       \
#              []-[1]- [2, 3]     [5, 6]-[7]-[]
#                      (pivot = 2) (pivot = 5)
#                       /     \     /     \
#                   []-[2]-  [3]  []-[5]- [6]
# Natija: shunday
# [1, 2, 3, 4, 5, 6, 7]

# vaifa  Xanoy minoralari

def hanoi(n, source, target, auxiliary):

    # Base Case
    if n == 1:
        print(f"Disk 1 ni {source} ustundan {target} ustunga ko'chiring")
        return

    hanoi(n - 1, source, auxiliary, target)

    print(f"Disk {n} ni {source} ustundan {target} ustunga ko'chiring")

    hanoi(n - 1, auxiliary, target, source)


hanoi(3, 'A', 'C', 'B')

# ---------------------TEST SAVOLI----------
#1-SAVOL  REKURSIV FUNKSIYANING ASOSIY VAZIFASI NIMA

 # Unda albatta har doim toxtash shart sababi uni toxtatish uchun umr yetmaydi..cheksiz sikl
# (base cese) bolishi shart

# 2 savol rekursiv funksiya toxtash shartisiz yozilsa nima boladi

# cheksiz davom etishi mumkin lekin maximumdan otsa xato beradi va Recursion eror beradi

# 3 savol quyidagi savolga nima qaytaradi

# def sanoq(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + sanoq(n-1)
#
# print(sanoq(3))

# 4 savol Iteratsiya sikllar (for, while) orqali, rekursiya esa o'zini chaqirish orqali ishlaydi /

# 5 savol Recursiya xar bir chaqirigi qayerda saqlaydi

# Stack (Stek) xotirada saqlaydi 

