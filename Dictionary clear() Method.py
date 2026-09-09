# Dictionary clear() Method shu xaqida dars boshladim
# bu yerda clear va car ham ichini boshatadi

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car.clear()
# print(car)

# bu yerda copy() metod ishlatilib nusxalaydi
#1

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.copy()
#
# print(x)

# 2 bunda True qaytaradi
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# x = car
#
# print(car is x)

#3 bunda False qaytaradi

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
#
# x = car.copy()
#
# print(car is x)

# bu yerda fromkeys() bitta umumiy value obekt beradi

# x = ('key1', 'key2', 'key3')
# y = 0
#
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)

# bizda  get() kalitini topib uning qiymatini qaytaradi!

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.get("model")
#
# print(x)

# bizda bu pop() berilgandan kegin ochiradi va uning qiymatini qaytaradi!

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# car.pop("model")
#
# print(car)

# values() bu yerda lugatdagi barcha qiymatlar royxatini qaytaradi!

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.values()
#
# print(x)

# update() lugatni belgilangan kalit qiymat juftliklari bilan yangilaydi

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# car.update({"color": "White"})
#
# print(car)
