# fruits = ["olma", "banan", "anor"]
#
# for fruit in fruits:
#     print(fruit)

# TESTNI YECHMOQDAMAN?
# 1-test

# def funksiya_nomi():  #def dan foydalanailad funksiya elon qilish uchun
#     # funksiya tanasi
#     pass

# 2-test

# def salom_ber(ism="Mehmon"):
#     return f"Salom, {ism}"
#
# print(salom_ber("Ali")) #Natija Salom, Ali

# 3-test

# def hisobla(a, b=2):
#     return a ** b
#
# x = hisobla(3)
# print(x)          #natija 9 bu yerda Return qaytarmoqda

# def test():
#     return 10         # Funksiya shu yerda tugadi
#     print("Salom")    # Bu qatorga hech qachon yetib kelinmaydi
#
# print(test()) #natija 10 sababai

# def test():
#     print("Salom")
#     return 10
#
# print(test())    #natija Salom10 chiqadi sababi return pastga tushurdim+

# def son():
#     print("A")
#     return 5
#     print("B")     #bu kod ishlamaydi sababi bu yerdaxam return tepada qolib ketgan
#
# print(son())  #natija A 5

# 4-test

# def hisobla(a, b=2):
#     return a ** b
#
# print(hisobla(3))  #natija 9 bu yerda print bermasdan test berilgan

# 5-test

# def f(a, b=[]):
#     b.append(a)
#     return b
# print(f(1), f(2))  #[1, 2] [1, 2]

# def f(a, b=[]):
#     b.append(a)
#     return b
#
# x = f(1)
# y = f(2)
#
# print(x)
# print(y)

# natija [1, 2]
# [1, 2]

# 6-test

# def salom():
#     return "Salom!"
#
# def ishlat(funksiya):
#     print(funksiya())
#
# ishlat(salom)  #funksiyalar birinchi darajali obyekt (first-class object) hisoblanadi sababi "Salom" emas salom

#6-savol

# def kvadrat(x):
#     return x * x
#
# def apply(f, qiymat):
#     return f(qiymat)
#
# print(apply(kvadrat, 5))  #bu yerda 5*5=25 chaqadi

# def kvadrat(x):
#     return x * x

# def kub(x):
#     return x * x * x
#
# def apply(f, qiymat):
#     return f(qiymat)

# print(apply(kub, 3))  #natija 3 * 3 * 3 = 27 nima qilyapti bu yerda f = kub qiymat = 3

# def kvadrat(x):
#     return x * x
#
#
# def apply(func, qiymat):
#     return func(qiymat)
#
# print(apply(kvadrat, 2))  #natija 4

# 7-test savoli

# def calc(a, b):
#     print(a + b)
#
# x = calc(2, 3)  #nima bolyapti bu yerda a + b = 2 + 3 = 5  return None avtomat python qiladi

# 8-savol

# def f():
#     print("A")
#
# def g():
#     return "B"
#
# x = f()
# y = g()

# 9-savol

# def add(x, y):
#     return x + y
#
# print(add(3, 5))   #argument parametrlari

# 10- savolga misollar

# def salom()   #  ikki nuqta yuq
#     print("Salom")

# def salom():
#     print("Salom")  # bu togri javob varyanti

