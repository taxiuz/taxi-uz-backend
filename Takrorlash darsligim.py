# g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# oyinchi = "X"
#
# while True:
#
#     print(f"""
#  {g[0]} | {g[1]} | {g[2]}
# -----------
#  {g[3]} | {g[4]} | {g[5]}
# -----------
#  {g[6]} | {g[7]} | {g[8]}
# """)
#
#     x = int(input(f"{oyinchi} = "))
#
#     if g[x - 1] == "X" or g[x - 1] == "O":
#         print("Katak bo'sh emas!")
#         continue
#
#     g[x - 1] = oyinchi
#
#     if (
#         g[0] == g[1] == g[2] or
#         g[3] == g[4] == g[5] or
#         g[6] == g[7] == g[8] or
#         g[0] == g[3] == g[6] or
#         g[1] == g[4] == g[7] or
#         g[2] == g[5] == g[8] or
#         g[0] == g[4] == g[8] or
#         g[2] == g[4] == g[6]
#     ):
#         print(f"""
#  {g[0]} | {g[1]} | {g[2]}
# -----------
#  {g[3]} | {g[4]} | {g[5]}
# -----------
#  {g[6]} | {g[7]} | {g[8]}
# """)
#         print(f"{oyinchi} yutdi!")
#         break
#
#     if all(str(i) in ["X", "O"] for i in g):
#         print("Durrang!")
#         break
#
#     if oyinchi == "X":
#         oyinchi = "O"
#     else:
#         oyinchi = "X"         #x va 0 oyini shartlari toliq bajarildi.!
import numbers
from builtins import print
from tokenize import Number

from Tools.scripts.objgraph import flat

# def bir ():
#     return 1
#
# def ikki ():
#     return 2
# def uch ():
#     return 3
#
# def tort ():
#     return 4
#
# son = tort()
# print(son)     #sanoq sonlari

# royxat = {
#     "yanvar": 6000,
#     "fevral": 12000,
#     "mart": 18000,
#     "aprel": 22000
# }
#
# max_royxat = []
#
# def narx():
#     for v in royxat.values():
#         max_royxat.append(v)
#
# narx()
#
# print(max(max_royxat)) #

# royxat = {
#     "yanvar": 6000,
#     "fevral": 12000,
#     "mart": 18000,
#     "aprel": 22000
# }
#
# son = int(input("Narx kiriting: "))
#
# for oy, narx in royxat.items():
#     if narx == son:
#         print(oy)
#         break
# else:
#     print("Bunday narx topilmadi")  #

#shart opertorlar if elif else

# if shart1:
#     print(True)
# elif shart2:
#     print("2-shart bajarildi")
# elif shart3:
#     pass
# else:
#     print("Hech biri bajarilmadi")
#misol
# son = 5
#
# if son > 0:
#     print("Musbat")
# elif son == 0:
#     pass
# else:
#     print("Manfiy")

#ikkidan uchinchi elementgacha
# s = "Python"
# print(s[1:4])

# teskari xolatda elementlarni
# s = "Python"
# print(s[::-1])

# boshidan oxiragacha bersek
# s = "Python"
# print(s[::1])

# qadamlar keraklik uzunligi
# s = "Python"
# print(s[1:5:3])

#oralatib tashlab ketsin formulasi

# s = "Python"
# print(s[0], s[2], s[4])

#keraklik larini olish
#
# s = "Python"
# print(s[2],s[4],s[5])
# String metodlar

#list metodlar

#keraklik lelementlar
# list = 2,3,4,5,7
#
# print(list[1:4])

#keraklik elemrntlar
# list = 2,3,4,5,7
#
# print(list[1:5:3])

#teskari kerklik
# list = 2,3,4,5,7
#
# print(list[6:1:-1])
#star index qaysi elemetdan boshlab kesib olaman degani.
#stop index qaysi elementgacha kesib olaman degan manoni.
#step index qaysi element kerak bolsa oralatib kesib olish.

# shert operatorlari

#manfiy musbat larni tekshirish
# number = int(input("Bironta son kiriting: "))
#
# if number >= 0:
#     print(f"Musbat son: {number}")
# else:
#     print(f"Manfiy son: {number}")

#
# number = int(input("Bironta son kiriting: "))
#
# if number>0:
#     print(f"Musbat son: {number}")
#
# else:
#     print(f"Manfiy son {number}")   #natihja manfiy musbatligini aytadi

# number = int(input("Bironta son kiriting: "))
#
# if number>0:
#     print(f"Musbat son: {number}")
#
# elif number < 0:
#     print(f"Manfiy son {number}") # bu yerda elif ishlatsakxam else ishlatsakxam bir

# number = float(input("Bironta son kiriting: "))
#
# if number>0:
#     print(f"Musbat son: {number}")
#
# elif number < 0:
#     print(f"Manfiy son {number}")
#
# else:
#     print("son na manfiy na musban son") #bu yerda 0 bersak namusbat na manfiy deydi


# number = float(input("Biorta istagan raqam kirgazing: "))
# if number<0:
#     print(f"manfiy son {number}")
# if number<5:
#     print(f"besh raqamidan kichik musbat son{number}") #qiziqarlik

# number = float(input("Birorta istagan raqam kirgazing: "))
#
# if number < 0:
#     print(f"Manfiy son: {number}")
# elif 0 < number < 5:
#     print(f"5 dan kichik musbat son: {number}")
# else:
#     print("Son 5 ga teng yoki undan katta") #qachon else qachon elif ekanligini bilib oldik

# number = float(input("Birorta son kiriting: "))
#
# if number < 0:
#     print(f"Manfiy son: {number}")
# elif number < 5:
#     print(f"5 dan kichik musbat son: {number}")
# else:
#     print("Son 5 ga teng yoki undan katta")    #if-if va if-elif-else
# if shart1:
#     # kod
# elif shart2:#if va elif ketma-ketligida faqat birinchi rost bo'lgan shart ishlaydi
#     # kod
#     elif shart3 #2-elif tekshirmaydi birinchisini togri dep xisoblaydi
# else:
#     # kod

# man tiqiy operatorlar and va or -"and"-va ornida kelsa "OR"-yoki manosini beradi
#1-and
# n = int(input("Sonni kiriting: "))
#
# if n % 18 == 0:
#     print("Bu son 18 ga qoldiqsiz bo'linadi")
# else:
#     print("18 ga bo'linmaydi")

#
# yosh = 20
# talaba = True
#
# if yosh >=18:
#     if talaba:
#         print("Talabalarga chegirma 20%")
#     else:
#         print("Kattalar uchun chegirma10%")
# else:
#     print("Chegirma faqat kattalaruchun") #yosh >= 18 → 20 >= 18 →True|Ichki if talaba: → True →

# yosh = 20
# talaba = True
#
# if yosh >= 18 and talaba:
#     print("Talabalarga chegirma 20%")
# elif yosh >= 18:
#     print("Kattalar uchun chegirma 10%")
# else:
#     print("Chegirma faqat kattalar uchun") #bu yerda else ni orniga elif ishlatdik soddaroq varyanti

# yosh = 20
# talaba = "Alisher"
#
# if yosh >= 18:
#     if talaba=="Alisher":
#         print("Talabalarga chegirma 20%")
#     else:
#         print("Kattalar uchun chegirma 10%")
# else:
#     print("Chegirma faqat kattalar uchun") # bu yerda shart ichida shart ketmoqda

# yosh = int(input("Yoshingizni kiriting: "))
# jins = input("Jinsingizni kiriting (ayol/erkak): ")
#
# if yosh >= 18:
#     if jins == "ayol":
#         print("Ayollar uchun chegirma 30%")
#     else:
#         print("Kattalar uchun chegirma 10%")
# else:
#     print("Bolalar uchun chegirma 20%") # bu yerda jinsi va yoshiga qarab chegirma yozdim

# yosh = int(input("Yoshingizni kiriting: "))
#
# if yosh < 18:
#     print("Chegirma 40%")
# elif yosh >= 60:
#     print("Chegirma 25%")
# else:
#     print("Chegirma 20%")  #bu yerda yoshga qarab chegirma berdim

#mantiqiy operatorlat nima?AND va OR

#1-and

# n = int(input("Sonni kiriting: "))
#
# if n % 9 == 0 and n % 2 == 0:
#     print("Bu son 18 ga bo'linadi")
# else:
#     print("Bu son 18 ga bo'linmaydi")

#2-or

# n = int(input("Sonni kiriting: "))
#
# if n % 9 == 0 or n % 2 == 0:
#     print("Bu son 18 ga qoldiqsiz bo'lindi")
# else:
#     print("18 ga bo'linmaydi")

# in va not in operatorlari

# foydalanuvchi = None
#
# if not foydalanuvchi:
#     print("Hechkim tizimga kirmagan") #bu yerda True qaytaradi natija Hechkim tizimga kirmagan

# foydalanuvchi = "Alisher"
#
# if not foydalanuvchi:
#     print("Hech kim tizimga kirmagan")
# else:
#     print("Tizimga kirgan:", foydalanuvchi) #Natija Tizimga kirgan: Alisher

# foydalanuvchi = "Alisher"
#
# if not foydalanuvchi:
#     print("Hech kim tizimga kirmagan")
# else:
#     print("Tizimga kirgan:", foydalanuvchi)

# matn = "Bugun uchinchi takrorlash darsimiz"
# if 'u' in matn:
#     print(True)
# else:
#     print(False)  #True qaytaradi

# print("Python" in "Men Python o'rganyapman")  #bu yerda xam ichida shu true qaytarmoqda sababai in bor

# matn = "Bugun uchinchi takrorlash darsimiz"
# if 'e' in matn:
#     print(True)
# else:
#     print(False)   #bu yerda xam e ichida yoqligi uchun False qaytarmoqda

# yosh_input = input("Yoshingiz: ").strip()
#
# if not yosh_input:
#     print("Yosh kiritilmadi!")
# elif not yosh_input.isdigit():
#     print("Iltimos, faqat raqam kiriting!")
# else:
#     yosh = int(yosh_input)
#
#     if yosh >= 18:
#         print("Xush kelibsiz!")
#     else:
#         print("Sizga ruxsat yo'q") # bu yerda 18 yoshdan kichkina bolsa ruxsat yuq deydi kotta bolsa xush kelibsiz deydi!

# def get_full_name(first_name, last_name=None):
#     last = last_name or "Noma'lum"
#     return f"{first_name} {last}"
# print(get_full_name("Alisher"))  #bu yerda familya yuq demoqda
#
# def get_full_name(first_name, last_name=None):
#     last = last_name or "Noma'lum"
#     return f"{first_name} {last}"
# print(get_full_name("Alisher", "Yoqubov")) #bu yerda familya va ismni togri bermoqda or togri ishlamoqda

#and, or, not operatorlari

# user_role = "editor"
# is_active = True
# has_permission = False
#
# if (user_role == "admin" or user_role == "editor") and is_active and not has_permission:
#     print("Siz ma'lumotlarni ko'rishingiz mumkin, lekin tahrirlay olmaysiz")

# a = True
# b = False
#
# print(a and b or not b)  #True qaytaradi bu yerda

#umumiy xulosa takrorlash darsini

#and bu yerda hammasi togri bolishi kerak yoshj 18togri talaba togri 2 tasi togri True qaytardi ishladi
# yosh = 20
# talaba = True
#
# if yosh >= 18 and talaba:
#     print("Chegirma bor")

#or ichida bitta rost bolisa yetarli True bolsa xammasini rost deydi

# yosh = int(input("Yoshingizni kiriting: "))
# talaba = input("Talabamisiz? (ha/yo'q): ")
#
# if yosh >= 18 or talaba == "ha":
#     print("Ruxsat bor")
# else:
#     print("Ruxsat yo'q")   #bu yerda 18 dan kichkina bolsa rost deydi talabamisiz desa xa desa Ruxsat bor deydi

# not teskarisiga aylantiradi
#
# foydalanuvchi = None
#
# if not foydalanuvchi:
#     print("Tizimga hech kim kirmagan")

# in bu ichida bormi bor deydi rostligini
# matn = "Python"
#
# if "P" in matn:
#     print("Bor")

# True False bu yerda 'P' 'p' kotta kichikliginixam xal qiladi

# print("P" in "Python")  # True
# print("p" in "Python")  # False

# bu yerda olma bor True qaytarmoqda

# mevalar = ["olma", "anor", "nok"]
#
# print("anor" in mevalar)

#bu yerda natija 6 12 18 24 30 36 natija beradi

# def sanoq():
#     for i in range(1,41):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i)
#
# sanoq()            # i % 2 va i % 3 bolinadi

#bu yerda 2 xam 3 xam 6 ga bolinadi

# def sanoq():
#     for i in range(1, 41):
#         if i % 6 == 0:
#             print(i)
#
# sanoq()      # tepadagi va pasdagi kodlar birxil natija bweradi

# bu Codify dagi yechilgan kod

# def sanoq():
#     for i in range(1, 41):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i)
#
# sanoq()

#Funksiyalarni 2 xil turi bor 1-si qiymat qaytarmaydigon 2-qiymat qaytaradigon

#1-qiymat qaytarmaydigon
# def print_5_greetings():
#     for _ in range(5):
#         print("Hello world")
#
# print_5_greetings()

#2-qiymat qaytaradigon
# def print_5_greetings():
#     for _ in range(5):
#         print("Hello world")
#     return "Sanoq funksiya"
#
# print(print_5_greetings())

# 3-tashlab otib ketadi pass
# def print_5_greetings():
#     for _ in range(5):
#         pass
#         # print("Hello world")
#     return "Sanoq funksiya"   #qiymat qaytaradigon funksiya
#
# print(print_5_greetings())

#gerag paytda chaqiradigon funksiya

# def print_5_greetings():
#     for _ in range(5):
#         print("Hello world")
#
# print_5_greetings()
# print("_____________")
# print_5_greetings()

# qiymat qataradigon funksiya yaratib olamiz

# def bir():
#     return 1
#
# def ikki():
#     return 2
#
# def uch():
#     return 3
#
# def tort():
#     return 4
#
# son = uch()
# print(son)    #o`zgaruvchi funksiyani tenglasam qovuslarimiz o`zgaruvchi qaytaryotgan qiymatga teng boladi

# def bir():
#     return 1
#
# def ikki():
#     return 2
#
# def uch():
#     pass              #return qaytarsa  xam nanqaytaradi
#
# def tort():
#     return 4
#
# son = uch()
# print(son)


# def add(a,b):  #a,b => parametrlar (input uchun “bo‘sh konteyner”)
#     return a + b
#
# yigindi = add(2,3)  #2,3 => argumentlar (real qiymatlar)
# print(yigindi)


#bu funksiyada user_data funksiyadi 3ta parametr bilan qabul qiladi

# def user_data(first_name, last_name, age):
#     print("Ism:", first_name)
#     print("Familiya:", last_name)
#     print("Yosh:", age)
#
# user_data("Alisher", "Yoqubov", 36)

#bu misolda familya ism yoshni aloxida sorov bajaradi
# def user_data(first_name, last_name, age):
#     print("Ism:", first_name)
#     print("Familiya:", last_name)
#     print("Yosh:", age)
#
# ism = input("Ism: ")
# familiya = input("Familiya: ")
# yosh = int(input("Yosh: "))
#
# user_data(ism, familiya, yosh)

# tayyor shablon yozib chiqdik
# login = "administrator"
# parol = 123456
#
# def login_print(l, p):
#     print(f"""
#     ****************
#     * Login: {l}
#     * Parol: {p}
#     ****************
#     """)

# login_print(login, parol)
# login_print(login, parol)

#ikkimarta chaqirsek ikkimarta beradi


#ushbu funksiyada find_max a,b,c  qabul qilinadi va  ichidan eng kotta raqamni topadi

# def find_max(a, b, c):
#     print("Eng katta son =", max(a, b, c))
#
# find_max(5, 10, 7)

# funksiyasiz yechim va ichidan eng kotta sonni topadi

# def find_max(a, b, c):
#     if a >= b and a >= c:
#         print("Eng katta son =", a)
#     elif b >= a and b >= c:
#         print("Eng katta son =", b)
#     else:
#         print("Eng katta son =", c)
#
# find_max(5, 10, 7)

#Eng katta son - A va B = 10 va bu yerda qaysi ozgaruvchilar kottaligni  biladigon bolsak!
# def find_max(a, b, c):
#     if a == b == c:
#         print(f"Eng katta son - A va B va C = {a}")
#     elif a == b and a > c:
#         print(f"Eng katta son - A va B = {a}")
#     elif a == c and a > b:
#         print(f"Eng katta son - A va C = {a}")
#     elif b == c and b > a:
#         print(f"Eng katta son - B va C = {b}")
#     elif a > b and a > c:
#         print(f"Eng katta son - A = {a}")
#     elif b > a and b > c:
#         print(f"Eng katta son - B = {b}")
#     else:
#         print(f"Eng katta son - C = {c}")
#
# find_max(10, 10, 5)

# find_letter_count(word, letter) funksiyasi berilgan soz ichida harf necha marta qatnashganini topish k/r

# def find_letter_count(word, letter):
#     print(f'"{word}" soʻzida "{letter}" dan {word.count(letter)} ta.')
#
# find_letter_count("Programming", "r")

#count funksiya ishlatilmasdan ishlangan

# def find_letter_count(word, letter):
#     sanoq = 0
#
#     for harf in word:
#         if harf == letter:
#             sanoq += 1
#
#     print(f'"{word}" soʻzida "{letter}" dan {sanoq} ta.')
#
# find_letter_count("Programming", "r")

# bu yerda sanoq

# def find_letter_count(word, letter):
#     return word.count(letter)
# natija = find_letter_count("worddjsnwordbdwordsjword","word")
# print(natija)

# eng baland bolgan sotilgan oyni topshirigi berilgan

# def big_sales(sales):
#
#     return max(sales, key=sales.get)
#
# sales_data = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# print(big_sales(sales_data))


# berilgan qaysi oyni qimmat sotiganini aniqlash returni

# def big_sales(sales):
#     max_month = None
#     max_value = 0
#
#     for month, amount in sales.items():
#         if amount > max_value:
#             max_value = amount
#             max_month = month
#
#     return max_month
# sales_data = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# print(big_sales(sales_data))



# def find_max(d):
#     return max(d, key=d.get)
# print(find_max({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))

# def find_max(d):
#     mk = list(d.keys())[0]
#     mv = list(d.values())[0]
#
#     for k, v in d.items():
#         if v > mv:
#             mv = v
#             mk = k
#
#     return mk
#
# print(find_max({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))

# def find_max(d):
#     return max(d, key=d.get)
#
# print(find_max({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))


# list_sum(myList) funksiyasini bilish

# def list_sum(myList):
#     yigindi = sum(myList)
#     print(f"Listning elementlar yig'indisi = {yigindi}")
#
# # Tekshirish:
# list_sum([10, 5, 7, 10])

# daraja(a, b) a va b ning darajasi

# def daraja(a, b):
#     print(a ** b)
#
# # Tekshirish:
# daraja(2, 3)  # 2 ning 3-darajasi: 8

# daraja4(a, b, c, d) funksiyasi

# def daraja4(a, b, c, d):
#     print(f"{a} ning {b}-darajasi: {a ** b}")
#     print(f"{a} ning {c}-darajasi: {a ** c}")
#     print(f"{a} ning {d}-darajasi: {a ** d}")
#
# # Tekshirish:
# daraja4(2, 2, 3, 4)

# digit_count_and_sum(word)

# def digit_count_and_sum(word):
#     raqamlar = [int(belgi) for belgi in word if belgi.isdigit()]
#
#     yigindi = sum(raqamlar)
#     soni = len(raqamlar)
#
#     print(f"Raqamlar yig'indisi: {yigindi}, Nechtaligi: {soni}")


# # Tekshirish:
# digit_count_and_sum("salom23orif5")

# add_right(a, b) funksiyasi 1234 chiqarishi kerak

# def add_right(a, b):
#     natija = int(str(a) + str(b))
#     print(natija)
#
#
# add_right(12, 34)

# add_left(a, b)  almashtirish funksiya

# def add_left(a, b):
#     natija = int(str(b) + str(a))
#     print(natija)
#
# # Tekshirish:
# add_left(12, 34)

# work_with_list(a) list ichida kichigini topib xar birga kopaytirish

# def work_with_list(a):
#     eng_kichik = min(a)
#
#
#     for i in range(len(a)):
#         a[i] = a[i] * eng_kichik
#
#     print(a)
#
#
#
# work_with_list([3, 5, 2, 4])

#shu usulda aniqlik ozgarmagan usuli

# def work_with_list(a):
#     eng_kichik = min(a)
#     return [x * eng_kichik for x in a]
#
# natija = work_with_list([3, 5, 2, 4])
# print(natija)

# eng kichkina son 2 uni 3*2=6,5*2=10,2*2=4,4*2=8 shu usul menga yaxshiroq varyanti
