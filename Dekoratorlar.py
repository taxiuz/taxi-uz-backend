# Dekorator — bu argument sifatida boshqa bir funksiyani qabul qilib, uning ishlash mantiqini o'zgartiradigan va yangi funksiya qaytaradigan yuqori tartibli funksiyadir
# def group_generator(lst, n):
#     stack = [(0, [])]
#
#     while stack:
#         idx, current_group = stack.pop()
#
#         if len(current_group) == n:
#             yield current_group
#             continue
#
#         for i in range(idx, len(lst)):
#             stack.append(
#                 (i + 1, current_group + [lst[i]])
#             )
#
#
# lst = [1,2,3,4]
#
# for group in group_generator(lst, 2):
#     print(group)

# def group_generator(lst, n):
#     stack = [(0, [])]
#
#     while stack:
#         idx, current_group = stack.pop()
#
#         if len(current_group) == n:
#             yield current_group
#             continue
#
#         for i in range(len(lst) - 1, idx - 1, -1):        #BU YERDA Aylantirib oldim
#             stack.append(
#                 (i + 1, current_group + [lst[i]])
#             )
#
#
# lst = [1,2,3,4]
#
# for group in group_generator(lst, 2):
#     print(group)

# Dekoratorlar

#  Bu bizning dekorator oddiy usuli

# def my_decorator(original_function):
#     def wrapper():
#         print("-" * 20)
#         original_function()
#         print("-" * 20)
#
#     return wrapper
#
#
#
# def say_hello():
#     print("Salom, Dunyo!")
#
# bezatilgan_funksiya = my_decorator(say_hello)
#
# bezatilgan_funksiya()

#sintatik shakllari bilan dekorator

# def my_decorator(original_function):
#     def wrapper():
#         print("-" * 20)
#         original_function()
#         print("-" * 20)
#
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Salom, Dunyo!")
#
# say_hello()

# argument bila dekaratirni bezash.

# def universal_decorator(original_function):
#
#     def wrapper(*args, **kwargs):
#         print("[Tizim] Funksiya ishga tushmoqda...")
#
#
#         result = original_function(*args, **kwargs)
#
#         print("[Tizim] Funksiya muvaffaqiyatli tugadi.")
#         return result
#
#     return wrapper
#
#
# @universal_decorator
# def xushkelibsiz(ism, yosh):
#     print(f"Xush kelibsiz, {ism}! Siz {yosh} yoshdasiz.")
#
#
# xushkelibsiz("Anvar", 25)

