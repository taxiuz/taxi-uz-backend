#topshririq: Python-dagi lugʻatlar Komiljon ustoz

# clear() — Lugʻatni butunlay boʻshatadi. {}

# d = {"a": 1, "b": 2}
# d.clear()
# print(d)

# pop(key) korsatilgan kalitni royxatdan ochiradi

# d = {"a": 1, "b": 2}
# qiymat = d.pop("a")
# print(qiymat)  # 1
# print(d)

# popitem() oxirgi qoshilgan elemntni ochiradi va qoshadi

# d = {"a": 1, "b": 2}
# ochirilgan = d.popitem()
# print(ochirilgan)
# print(d)

# keys() kalitlar roʻyxatini qaytaradi

# d = {"a": 1, "b": 2}
# print(d.keys())   # dict_keys(['a', 'b']

# values() qiymatlar roʻyxatini qaytarad!

# d = {"a": 1, "b": 2}
# print(d.values())

# items() umumiy roʻyxat qaytaradi!

# d = {"a": 1, "b": 2}
# print(d.items())

# get(key) Kalit boyicha qiymatni oladi!

# d = {"a": 1}
# print(d.get("a"))  # 1
# print(d.get("b"))  # None    agar kalit bolmasa eror bermaydi

# update() kalit qiymat juftliklarini qoshadi yoki borlarini yangilaydi!

# d = {"a": 1}
# d.update({"b": 2, "a": 10})
# print(d)

# setdefault()bu lugatda kalit yo'q bo'lsa boshlang'ich qiymat berish uchun ishlatilad

# hisob = {}
#
# hisob.setdefault("olma", 0)
# hisob["olma"] += 1
#
# print(hisob)

# copy() nusxalash metodi!
#1 False qaytarishi

# d1 = {"a": 1}
# d2 = d1.copy()
#
# print(d1 is d2)

#2 True qaytarishi

# d1 = {"a": 1}
# d2 = d1
#
# print(d1 is d2)

# ustoz orgatkanlaridek xirxil natija kopiyapas

# d1 = {"x": [1, 2]}
# d2 = d1.copy()
#
# d2["x"].append(3)
#
# print(d1)
# print(d2)

# dict.fromkeys() ushbu royxatdagi har bir element lugat kaliti boladi

# kalitlar = ["x", "y", "z"]
# yangi_lugat = dict.fromkeys(kalitlar, 0)
# print(yangi_lugat)

# bu yerda None bolishi mumkin boladi bunga etibor

# d = dict.fromkeys(["a", "b", "c"])
# print(d)

# fromkeys() qiymat bixil bolishini koramiz.

# d = dict.fromkeys(["ism", "familiya"], "kiritilmagan")
# print(d)


# Dictionary Methods Umumiy xulosasi

# Metod *****	Vazifasi
# get() *****	Kalit qiymatini xavfsiz olish
# keys() *****	Barcha kalitlarni olish
# values()***** Barcha qiymatlarni olish
# items() *****	Kalit va qiymat juftliklarini olish
# update() *****	Lugatni yangilash
# pop()	 ***** Elementni ochirish
# popitem() *****	Oxirgi elementni ochirish
# clear()**Lugatni tozalash
# copy()*Nusxa olish
# setdefault()*Kalit bolmasa qoshish
# fromkeys()*Bir nechta kalitlardan yangi lugat yaratish