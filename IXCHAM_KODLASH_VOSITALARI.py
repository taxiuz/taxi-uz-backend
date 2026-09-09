# contacts = {
#     "Nodir": "+998999991111",
#     "Laziz": "+998916726233"
# }
#
# contacts["Akmal"] = "+998916703070"
#
# print(contacts)

# contacts = {
#     "Nodir": "+998999991111",
#     "Laziz": "+998916726233"
# }
#
# contacts["Akmal"] = "+998916703070"
#
#
# while True:
#     print("""
# Kontakt qo'shish uchun: 1
# Kontaktni edit qilish uchun: 2
# Ro'yxatni ko'rish uchun: 3
# Chiqish uchun: 0
# """)
#
#     amal = input("Amal: ")
#
#     if amal == "1":
#         ism = input("Ism: ")
#         raqam = input("Raqam: ")
#
#         contacts[ism] = raqam
#
#         print("Kontakt qo'shildi:")
#         print(contacts)
#
#
#     elif amal == "2":
#         ism = input("O'zgartirmoqchi bo'lgan kontakt ismi: ")
#         raqam = input("Yangi raqam: ")
#
#         contacts[ism] = raqam
#
#         print("Kontakt yangilandi:")
#         print(contacts)
#
#
#     elif amal == "3":
#         print("Kontaktlar:")
#         print(contacts)
#
#
#     elif amal == "0":
#         print("Dastur tugadi")
#         break
#
#
#     else:
#         print("Noto'g'ri amal tanlandi")

#Nomer 2

# contacts = {
#     "Nodir": "+998999991111",
#     "Laziz": "+998916726233"
# }
#
# contacts["Akmal"] = "+998916703070"
#
#
# while True:
#     print("""
# ======================================
# 👤 KONTAKTLARNI BOSHQARISH TIZIMI
# ======================================
# 1 ➡️ Kontakt qo'shish
# 2 ➡️ Kontaktni tahrirlash (Edit)
# 3 ➡️ Ro'yxatni chiroyli ko'rish
# 4 ➡️ Kontaktni o'chirish (Delete)
# 0 ➡️ Chiqish (Exit)
# ======================================
# """)
#
#     amal = input("Amalni tanlang (0-4): ")
#
#     if amal == "1":
#         print("\n➕ YANGI KONTAKT QO'SHISH:")
#         ism = input("Ism: ").strip()
#         raqam = input("Raqam: ").strip()
#
#         # Ism allaqachon borligini tekshirish (ustidan yozib yubormaslik uchun)
#         if ism in contacts:
#             javob = input(f"  '{ism}' ismli kontakt bor. Raqamini yangilamoqchimisiz? (ha/yo'q): ")
#             if javob.lower() != 'ha':
#                 print("  Amaliyot bekor qilindi.")
#                 continue
#
#         contacts[ism] = raqam
#         print(f"  {ism} muvaffaqiyatli qo'shildi!")
#
#
#     elif amal == "2":
#         print("\n📝 KONTAKTNI TAHRIRLASH:")
#         ism = input("O'zgartirmoqchi bo'lgan kontakt ismi: ").strip()
#
#         # Oltin qoida: faqat bor kontaktni o'zgartirishga ruxsat beramiz
#         if ism in contacts:
#             raqam = input("Yangi raqam: ").strip()
#             contacts[ism] = raqam
#             print(f"  '{ism}' kontaktining raqami yangilandi!")
#         else:
#             print(f"  Xatolik: Ro'yxatda '{ism}' ismli kontakt topilmadi!")
#
#
#     elif amal == "3":
#         print("\n  BARCHA KONTAKTLAR RO'YXATI:")
#         if not contacts:
#             print("📭 Kontaktlar ro'yxati bo'sh!")
#         else:
#             # .items() view-metodi orqali chiroyli va tartibli chiqarish
#             for indeks, (ism, raqam) in enumerate(contacts.items(), 1):
#                 print(f"{indeks}. 👤 {ism}  {raqam}")
#
#
#     elif amal == "4":
#         print("\n KONTAKTNI O'CHIRISH:")
#         ism = input("O'chirmoqchi bo'lgan kontakt ismi: ").strip()
#
#         # .pop(key, default) orqali xavfsiz o'chirish
#         ochirilgan_raqam = contacts.pop(ism, None)
#
#         if ochirilgan_raqam:
#             print(f"🗑️ '{ism}' ({ochirilgan_raqam}) ro'yxatdan butunlay o'chirildi!")
#         else:
#             print(f" Xatolik: '{ism}' ismli kontakt topilmadi!")
#
#
#     elif amal == "0":
#         print("\n  Dastur tugadi. Sog' bo'ling!")
#         break
#
#
#     else:
#         print("\n  Noto'g'ri amal tanlandi! Iltimos, 0 dan 4 gacha raqam kiriting.")

# Nomer 3
# while True:  # 1. Sikl boshlandi
#     amal = input("Amal: ")
#
#     if amal == "1":
#         if ism in contacts:
#
#             continue
#
#     elif amal == "0":
#
#         break

#nomer 4

# if amal == "1":
#     print("\n YANGI KONTAKT QO'SHISH:")
#
#     ism = input("Ism: ").strip()
#     raqam = input("Raqam: ").strip()
#
#     ruxsat = True
#
#     if ism in contacts:
#         javob = input(
#             f"⚠️ '{ism}' ismli kontakt bor. "
#             "Raqamini yangilamoqchimisiz? (ha/yo'q): "
#         )
#
#         if javob.lower() != "ha":
#             print(" Amaliyot bekor qilindi.")
#             ruxsat = False
#
#     if ruxsat:
#         contacts[ism] = raqam
#         print(f" {ism} muvaffaqiyatli qo'shildi!")

# nomer 5

# Boshlang'ich ma'lumotlar strukturasi
# Kalit (Key) - Kitob nomi, Qiymat (Value) - Janrlar to'plami (Set)


# library = {
#     "O'tkan kunlar": {"Tarixiy", "Roman", "Drama"},
#     "Dunyoning ishlari": {"Klassika", "Drama"},
#     "Sariq devni minib": {"Sarguzasht", "Bolalar"}
# }
#
# while True:
#     def funksiya():
#         """
# ======================================
#  KUTUBXONA BOSHQARUV TIZIMI
# ======================================
# 1 ➡ Yangi kitob va janrlar qo'shish
# 2 ➡ Janr bo'yicha kitoblarni qidirish
# 3 ➡ Kutubxona statistikasini ko'rish
# 0 ➡ Chiqish (Exit)
# ======================================
#        """
#     pass
#
#     amal = input("Amalni tanlang (0-3): ").strip()
#
#     if amal == "1":
#         print("\n➕ YANGI KITOB QO'SHISH:")
#         kitob = input("Kitob nomi: ").strip()
#         janrlar_input = input("Janrlarni kiriting (vergul bilan ajrating): ")
#
#
#         yangi_janrlar = {j.strip().capitalize() for j in janrlar_input.split(",") if j.strip()}
#
#         ruxsat = True
#         if kitob in library:
#             javob = input(f"⚠️ '{kitob}' kitobi allaqachon bor. Janrlarini birlashtiraylikmi? (ha/yo'q): ")
#             if javob.lower() == "ha":
#
#                 library[kitob].update(yangi_janrlar)
#                 print(f" '{kitob}' kitobining janrlari yangilandi!")
#                 ruxsat = False
#             else:
#                 print(" Amaliyot bekor qilindi.")
#                 ruxsat = False
#
#         if ruxsat:
#             library[kitob] = yangi_janrlar
#             print(f" '{kitob}' kutubxonaga muvaffaqiyatli qo'shildi!")
#
#     elif amal == "2":
#         print("\n JANR BO'YICHA QIDIRISH:")
#         qidirilayotgan_janr = input("Qaysi janrdagi kitoblarni qidiryapsiz?: ").strip().capitalize()
#
#         topilgan_kitoblar = []
#
#
#         for kitob, janrlar in library.items():
#
#             if qidirilayotgan_janr in janrlar:
#                 topilgan_kitoblar.append(kitob)
#
#         if topilgan_kitoblar:
#             print(f" '{qidirilayotgan_janr}' janridagi kitoblar:")
#             for i, k in enumerate(topilgan_kitoblar, 1):
#                 print(f"{i}. {k}")
#         else:
#             print(f" Afsuski, '{qidirilayotgan_janr}' janrida kitob topilmadi.")
#
#     elif amal == "3":
#         print("\n KUTUBXONA STATISTIKASI:")
#         if not library:
#             print(" Kutubxona bo'sh!")
#         else:
#             print(f"Kitoblarning umumiy soni: {len(library)} ta")
#
#             # Barcha janrlarni bitta umumiy Set'ga yig'amiz (Noyoblarini bilish uchun)
#             barcha_noyob_janrlar = set()
#             for janrlar in library.values():
#                 barcha_noyob_janrlar.update(janrlar)
#
#             print(f"Kutubxonadagi jami noyob janrlar soni: {len(barcha_noyob_janrlar)} ta")
#             print(f"Janrlar ro'yxati: {', '.join(barcha_noyob_janrlar)}")
#
#     elif amal == "0":
#         print("\n Dastur tugadi. Mutolaadan to'xtamang!")
#         break
#
#     else:
#         print("\n⚠️ Noto'g'ri amal!")

# LIST COMPEHENSION

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# toqlar = []
# for i in l:
#     if i % 2 == 1:
#         toqlar.append(i*2)
#         print(toqlar)     #Natija:[2, 6, 10, 14, 18]

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# toqlar = [i*2 for i in l if i%2==1]
#
# print(toqlar)  #qisqa varyatni


# regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
#            ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
#
# from_city = [l[1] for l in regions]
# print(from_city)

# sonlar = [1, 2, 3, 4, 5]
# Ushbu listdagi toq sonlarni 2ga ko'paytirib yangi listga o'tkazing?

# sonlar = [1, 2, 3, 4, 5]
#
# yangi_list = []
#
# for son in sonlar:
#     if son % 2 != 0:
#         yangi_list.append(son * 2)
#
# print(yangi_list)

# qisqa varyanti! [son * 2  for son in sonlar  if son toq]

# sonlar = [1, 2, 3, 4, 5]
#
# yangi_list = [son * 2 for son in sonlar if son % 2 != 0]
#
# print(yangi_list)

# son % 2 != 0   son toq ekanligini tekshiradi
# append()   yangi listga qoshadi
# son * 2  2 ga kopaytiradi

# lst = ['Alice', 1, 2, 3, 'Alice', 'Alice']
#
# indice = lst.index('Alice')
#
# indicies = [i for i in range(len(lst)) if lst[i] == 'Alice']
#
# print(indicies)


# def find_millionaire(people):
#     return [name for name, money in people.items() if money >= 1_000_000]
#
#
# people_data1 = {
#     'Alice': 1_000_000,
#     'Bob': 998_170,
#     'Carol': 1_229_080,
#     'Frank': 881_230,
#     'Eve': 93_121
# }
#
# people_data2 = {
#     'Alice': 1_000_000,
#     'Bob': 998_170,
#     'Frank': 1_881_230,
#     'Eve': 93_121
# }
#
#
# def test():
#     assert find_millionaire(people_data1) == ['Alice', 'Carol']
#     assert find_millionaire(people_data2) == ['Alice', 'Frank']
#
#     print("Test o'tdi ")
#
#
# test()

# def find_millionaire(people):
#     return [name for name, money in people.items() if money >= 1_000_000]
#
#
# people_data1 = {
#     'Alice': 1_000_000,
#     'Bob': 998_170,
#     'Carol': 1_229_080,
#     'Frank': 881_230,
#     'Eve': 93_121
# }
#
# people_data2 = {
#     'Alice': 1_000_000,
#     'Bob': 998_170,
#     'Frank': 1_881_230,
#     'Eve': 93_121
# }
#
#
# def test():
#     assert find_millionaire(people_data1) == ['Alice', 'Carol']
#     assert find_millionaire(people_data2) == ['Alice', 'Frank']
#
#     print("Test o'tdi ")
#
#
# test()

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#
# l = []
# for x in range(3):
#     for y in range(3):
#         l.append((x, y))
#
# print([(x,y) for x in range(3) for y in range(5)])

# from itertools import product
#
# l = list(product(range(3), range(3)))
#
# print(l)

# l = [(x, y) for x in range(3) for y in range(3)]
#
# print(l)

# l = ((x, y) for x in range(3) for y in range(3))
#
# print(list(l))

# from itertools import product
#
# result = list(product(range(3), repeat=2))
#
# print(result)

# text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
# or no money in my purse, and nothing particular to interest me on shore, I thought I would
# sail about a little and see the watery part of the world. It is a way I have of driving off
# the spleen, and regulating the circulation. - Moby Dick '''
# # print([[i for i in line.split() if len(i)>7] for line in text.split("\n")])

# # ziplash varyanti

# lst_1 = ['ism', 'familiya', 'yosh']
# lst_2 = ['Akmal', 'Tohirov', 16]
#
# for i, j in zip(lst_1, lst_2):
#     print(i, j)

# ustun_nomlari = ['name', 'salary', 'job']
#
#
# qatorlar = [('Alice', 180_000, 'data scientist'),
#             ('Bob', 99_000, 'project manager'),
#             ('Frank', 87_000, 'backend developer')]
# db = [dict(zip(ustun_nomlari, row)) for row in qatorlar]
# print(db)

# f = lambda a: a * 2
# ==
# def f(a):
#     return a * 2

# def kvadrat(x):
#     return x ** 2

# Lambda varianti

# summa_lambda = lambda a, b, c: a + b + c
# print(summa_lambda.__name__)

# Def varianti

# def summa_def(a, b, c):
#     return a + b + c
# print(summa_def.__name__)

# juftliklar = [
#     (1, 'olma'),
#     (2, 'behi'),
#     (3, 'shaftoli')
# ]
#
# saralangan = sorted(juftliklar, key=lambda x: x[1])
#
# print(saralangan)

# str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
#
# int_nums = map(int, str_nums)
#
# print(list(int_nums))

# str_nums = ["4", "8", "6", "5", "3"]
# juft_kvadratlar = [int(x) ** 2 for x in str_nums if int(x) % 2 == 0]
#
# print(juft_kvadratlar)  #if da ishlash

# str_nums = ["4", "8", "6", "5", "3"]
#
# natija = [int(x) ** 2 if int(x) % 2 == 0 else int(x) ** 3 for x in str_nums]
#
# print(natija)
# Natija: [16, 64, 36, 125, 27]  if else

# str_nums = ["4", "8", "6", "5", "3"]
#
# juft_kvadratlar = [int(x) ** 2 for x in str_nums if int(x) % 2 == 0]
#
# print(juft_kvadratlar)
# Natija: [16, 64, 36] —— (5 va 3 ro'yxatga kirmay qoldi)

# str_nums = ["4", "8", "6", "5", "3"]
#
# natija = [int(x) ** 2 if int(x) % 2 == 0 else int(x) ** 3 for x in str_nums]
#
# print(natija)
# Natija: [16, 64, 36, 125, 27]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# juft_flat = [num for row in matrix for num in row if num % 2 == 0]
#
# print(juft_flat)
# Natija: [2, 4, 6, 8]

# map() va lambda

# numbers = [1, 2, 3, 4, 5]
#
# print(list(map(lambda x: x ** 2, numbers)))
#Natija:[1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5]
#
# def kvadrat(x):
#     return x ** 2
#
# print(list(map(kvadrat, numbers)))
# Huloasa:
# Sintaktik tozalik va tezlik kerak bo‘lsa  List Comprehension
# Xotirani tejash (Lazy evaluation) kerak bolsa va tayyor funksiya (masalan, int, str) ishlatilsa  map() birinchi tanlov!

# map() orqali ikki ta list elementlarini juftlab ayiradi

# print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
# Natija:[1, 1, 1]

# string_it = ["processing", "strings", "with", "map"]

# print(list(map(str.upper, string_it)))  #bu yerda hammasi katta harfga otdi

# reduce()  yigib borish accumulate

# from functools import reduce
#
# n = 4
#
# print(reduce(lambda x, y: x * y, range(1, n + 1)))  #Natija:24

# filter() — shart boyicha tanlash

# nums = [1, 2, 3, 4, 5, 6]
#
# result = list(filter(lambda x: x % 2 == 0, nums))
#
# print(result)   #Natija: [2, 4, 6]


# dirty_data = ["olma", "", None, "behi", False, "anor", 0]
#
# clean_data = list(filter(None, dirty_data))
# print(clean_data)   #filter() aslida nima? shartdan otkaz, qolganini tashla mexanizmi


# users = [
#     {"name": "Anvar", "age": 25},
#     {"name": "Samandar", "age": 16},
#     {"name": "Nodira", "age": 19}
# ]
#
#
# kattalar = filter(lambda u: u["age"] >= 18, users)
# print(list(kattalar))


# -------------------Test natijalari-----------------
#1 savol List Comprexesioning togri sintaksisi qaysi?
# A) [x for x in range(10) if x % 2 == 0]  #if operatori sikldan (for in) keyin — eng oxirida kelgan

# 2 savol Lambda funksiyalari haqida qaysi fikr notogri berilgan?
# lambda x: return x ** 2 # shu javop notogri
# def kvadrat(x):
#     return x ** 2
# print(kvadrat(4)) # tog`ri javop

# 3 savol map() funksiyasi nima vazifani bajaradi?
# map(int, str_nums) yoki map(lambda x: x2, numbers)
# funksiya ketmaketligini har bir elementga qollaydi

# 4 savol filter() funksiya sifatida nimani qaytaradi
# <filter object> (True) qaytaradi

# 5 savol  shu misol nimani qaytaradi

# nums = [1, 2, 3, 4]
#
# res = list(map(lambda x: x * 2, nums))
#
# print(res)

# 6 savol  resuce funksiyasi [1,2,3,4] kopaytirish amali bilan berilsa natija nechi boladi

# from functools import reduce
# nums = [1, 2, 3, 4]
# res = reduce(lambda a, b: a * b, nums)
#
# print(res)

# 7 savol filter yordamida juft sonlarni ajratish usuli qanday

# nums = [1, 2, 3, 4, 5, 6]
#
# result = filter(lambda x: x % 2 == 0, nums)
#
# print(list(result))

# 8 savol res = [x**2 for x in range(3)] natija nima [0, 1, 4]

# res = [x**2 for x in range(3)]
#
# print(res)


# ---------Rahmat salomat boling-----------------

