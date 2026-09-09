# 13-dars boshladik

# for i in son:
#     pass

# bir xonalik sonni aniqlash uchun

# son_h = [
#     "nol",
#     "bir",
#     "ikki",
#     "uch",
#     "to'rt",
#     "besh",
#     "olti",
#     "yetti",
#     "sakkiz",
#     "to'qqiz",
#     "o'n",
#     "yigirma",
#     "o'ttiz",
#     "qirq",
#     "ellik",
#     "oltmish",
#     "yetmish",
#     "sakson",
#     "to'qson",
#     "yuz",
#     "ikki yuz",
#     "uch yuz",
#     "tort yuz",
#     "besh yuz",
#     "olti yuz",
#     "yetti yuz",
#     "sakkiz yuz",
#     "toqqiz yuz",
#
# ]
#
# son = input("Son kiriting: ")
#
# if len(son) == 1:
#     nat = son_h[int(son)]
#     print(nat)
#
# elif len(son) == 2:
#     nat = son_h[int(son[0]) + 9]
#     nat2 = son_h[int(son[1])]
#
#     if son[1] == "0":
#         print(nat)
#     else:
#         s = str(nat) + " " + str(nat2)
#         print(s)

# minglik qilaman qilaman

# birlik = [
#     "nol",
#     "bir",
#     "ikki",
#     "uch",
#     "to'rt",
#     "besh",
#     "olti",
#     "yetti",
#     "sakkiz",
#     "to'qqiz"
# ]
#
# onlik = [
#     "",
#     "o'n",
#     "yigirma",
#     "o'ttiz",
#     "qirq",
#     "ellik",
#     "oltmish",
#     "yetmish",
#     "sakson",
#     "to'qson"
# ]
#
# son = input("Son kiriting: ")
#
# natija = ""
#
# if len(son) == 1:
#     natija = birlik[int(son)]
#
# elif len(son) == 2:
#
#     if son[0] != "0":
#         natija += onlik[int(son[0])]

#     if son[1] != "0":
#         natija += " " + birlik[int(son[1])]
#
# elif len(son) == 3:
#
#     if son[0] != "0":
#         natija += birlik[int(son[0])] + " yuz"
#
#     if son[1] != "0":
#         natija += " " + onlik[int(son[1])]
#
#     if son[2] != "0":
#         natija += " " + birlik[int(son[2])]
#
# elif len(son) == 4:
#
#     if son[0] != "0":
#         natija += birlik[int(son[0])] + " ming"
#
#     if son[1] != "0":
#         natija += " " + birlik[int(son[1])] + " yuz"
#
#     if son[2] != "0":
#         natija += " " + onlik[int(son[2])]
#
#     if son[3] != "0":
#         natija += " " + birlik[int(son[3])]
#
# print(natija.strip())


# 1 dan 25000 gacha bolgan sonlarni chiqaraman

# def sonni_sozga_aylantir(son):
#     if son == 0:
#         return "nol"
#
#     birliklar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
#     onliklar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
#
#     natija = []
#
#
#     minglar = son // 1000
#     qoldiq = son % 1000
#
#     if minglar > 0:
#
#         if minglar >= 10:
#             natija.append(onliklar[minglar // 10])
#             if minglar % 10 > 0:
#                 natija.append(birliklar[minglar % 10])
#         else:
#             natija.append(birliklar[minglar])
#
#         natija.append("ming")
#
#
#     yuzlar = qoldiq // 100
#     qoldiq = qoldiq % 100
#     if yuzlar > 0:
#         if yuzlar > 1:  # "bir yuz" emas, odatda "yuz" deyiladi, lekin "ikki yuz" yoziladi
#             natija.append(birliklar[yuzlar])
#         natija.append("yuz")
#
#
#     onlik = qoldiq // 10
#     if onlik > 0:
#         natija.append(onliklar[onlik])
#
#
#     birlik = qoldiq % 10
#     if birlik > 0:
#         natija.append(birliklar[birlik])
#
#
#     return " ".join(natija).strip()
#
#
#
# son = 25000
# print(f"{son} -> {sonni_sozga_aylantir(son)}")
#
#
# test_son = int(input("Istalgan son kiriting: "))
# print(f"{test_son} -> {sonni_sozga_aylantir(test_son)}")

#bir biriga qoshib chiqamiz!

#1

# def list_sum(my_list):
#     s = 0
#     for i in my_list:
#         s += i
#     return s
#
# print(list_sum([1, 2, 3]))

#2

# def list_sum(my_list):
#     return sum(my_list)
#
# print(list_sum([1, 2, 3]))

# 3

# def list_sum(my_list):
#     s = 0
#     for i in my_list:
#         s = s + i
#     return s
#
# print(list_sum([1, 2, 3,4]))

#4

# def sum(iterable, start=0):
#     result = start
#     for item in iterable:
#         result = result + item
#     return result

#5

# PyObject *
# builtin_sum(PyObject *iterable, PyObject *start)
# {
#     PyObject *result = start;
#     PyObject *iter = PyObject_GetIter(iterable);
#
#     if (!iter)
#         return NULL;
#
#     Py_INCREF(result);
#
#     for (;;) {
#         PyObject *item = PyIter_Next(iter);
#         if (!item) {
#             if (PyErr_Occurred())
#                 goto error;
#             break;
#         }
#
#         PyObject *temp = PyNumber_Add(result, item);
#         Py_DECREF(item);
#         Py_DECREF(result);
#
#         if (!temp)
#             goto error;
#
#         result = temp;
#     }
#
#     Py_DECREF(iter);
#     return result;
#
# error:
#     Py_DECREF(iter);
#     Py_DECREF(result);
#     return NULL;
# }

#6

# def my_is_digit(my_str):
#     for i in my_str:
#         if i < '0' or i > '9':
#             return False
#     return True

#7

# def work_with_list(a):
#     m = min(a)
#     for i in a:
#         i *= m
#     return a
#
#
# print(work_with_list([1,2,3]))

#8

# def work_with_list(a):
#     m = min(a)
#
#     for i in range(len(a)):
#         a[i] *= m
#
#     return a
#
# print(work_with_list([2, 4, 3]))

# 9

# def expensiveProduct(products):
#     eng_qimmat = products[0]
#
#     for product in products:
#         if product["price"] > eng_qimmat["price"]:
#             eng_qimmat = product
#
#     print(eng_qimmat["name"])
#
#
# products = [
#     {"name": "iPhone X", "price": 600},
#     {"name": "iPhone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100}
# ]
#
# expensiveProduct(products)

#10

# def expensiveProduct(products):
#
#     max_price = 0
#     max_product = {}
#
#     for product in products:
#
#         if product["price"] > max_price:
#             max_price = product["price"]
#             max_product = product
#
#     return max_product["name"]
#
#
#
# arr = [
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung S10",
#         "price": 800
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 1100
#     },
# ]
#
#
# print(expensiveProduct(arr))

# 11

# def min_max(numbers, max_num, min_num):
#     min1 = min(numbers)
#     max1 = max(numbers)
#     if max == max_num:
#         print("Maximum togri topdingiz")
#     else:
#         print("Maximum xato!")
#     if min1 == min_num:
#         print("Minimum togri topdigiz")
#     else:
#         print("Minimum xato!")
#
#
# min_max([2,3,1,4,7,8,2],8,1)

# 12

# d =    {
#     "name": "I phone X",
#     "prince": 600,
#     "colur": "bleck",
#
# }
#
# for i in d.items():
#     print(i)

# 13

# d =    {
#     "name": "I phone X",
#     "prince": 600,
#     "color": "bleck",
#
# }
#
# for i in d.keys():
#     print(i)        #chap tomoni

# 14

# d =    {
#     "name": "I phone X",
#     "prince": 600,
#     "color": "bleck",
#
# }
#
# for i in d.items():
#     print(i)               #ikkala tomoni

# 15


# d =    {
#     "name": "I phone X",
#     "prince": 600,
#     "color": "bleck",
#
# }
#
# for i in d.items():
#     print(i)

# 17

# d =    {
#     "name": "Iphone X",
#     "prince": 600,
#     "color": "bleck",
#
# },
#
# for i in d :
#     print(i)

#18

# l=[0,1,2,3,4,5,True]
# l.remove(True)
# print(l)       #bu yerda 1 ni True dep oylaydi va ochirib tashlaydi

# 18

# l = [0, 1, 2, 3, 4, 5, True]
# l.pop(-1)
# print(l)  #shunda 1 ni ochirmaydi tog`ri ishlaydi

# 19

# l = [3,2,5,1,4,6,9,2]
# i = 0
# while i < len(l):
#     print(l[i])
#     i+=1

# 20

# l = [10, 20, 30, 40]
#
#
# for x in l:
#     print(x)


# 20#

a = [1, 2, 3]
b = a

del a
del b