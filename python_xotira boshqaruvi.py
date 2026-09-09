# pythonda xotira boshqaruvi nima dep ataladi?

# a = [1, 2, 3]
# b = a
#
# del a
# del b

# refcount = 0

# obyekt darhol ochiriladi

# def test():
#     a = [1, 2, 3]
#     print(a)
#
# test()   #natija  [1, 2, 3] nega a bilan kelganda ishlayni b bilan kelganda bloklaydi

# x = None
#
# def test():
#     global x
#     x = [1, 2, 3]
#
# test()
# print(x) # Natija: [1, 2, 3]   shunday ishlaydi


#ozgaruvchiga bolgan ssilkalar "murojatlar" soni nechiga teng bolsa u xotiradan ochiradi?

# print(a[0] is a)        # True
# print(a[0][0][0] is a)  # True (Istalgancha chuqur kirsa bo'ladi)

# sababai 0 ga tushganda python kerak emas deb oylaydi va xotiradan ochiraib tashlaydi

# ogaruvchini xotiradagi manzilini qaysi funksiya orqali korishimiz mumkin?

# x = int("300")
# y = int("300")
#
# print(x is y) # False qaytardi Ular xotirada aynan bitta obyektga korsatib turibdi.

# x = 300
# y = 300
#
# print(x == y) #True qaytardi va -5 dan 256 gacha) intern (cache) qiladi  "==" taqoslashda shunday qilish k.k

#bir dona Arena hajmi qancha kb boladi?

# 4 KB — Bu bitta Pool (yoki tizim darajasidagi Page) ning hajmi.
# 256 KB — Biz qidirgan bitta Arena ning olchami.
# 1024 KB (1 MB) — Bu odatda Python dasturi ichida C stack'i uchun ajratiladigan

# CPython (PyMalloc) Xotira Ierarxiyasi: Kattadan Kichikka

# Arena Eng katta qism 256 KB (KiloBayt)

# Arena = 256 KB
# Pool = 4 KB
# Block = 8–512 B


# a = [1, 2, 3]
# b = a
# c = a.copy()
#
# b = a → yangi list yaratmaydi.
# a va b bitta obyektga qaraydi.
# c = a.copy() → yangi list yaratadi.

# a = [1, 2, 3 ]
# b = a
# a.append(4)
#
# print(a)   #a ozgarmaydi [1, 2, 3, 4]

# a = [1, 2, 3 ]
# b = a.copy()
# b.append(4)
#
# print(a)  # b ozgardi  [1, 2, 3]

# a = [1, 2, 3, [4, 5]]
# b = a.copy()
# b[3].append(6)
#
# print(a)