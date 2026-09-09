# takrorlashdan Mehmonxona darsimizi takrorlab olamiz

# mehmonlar = {}
#
# band_xonalar = set()
#
# XONA_TURLARI = {"Ekonom", "Standart", "Lux"}
#
#
# def mehmon_qoshish(ism, xona_raqami, xona_turi):
#
#     if ism in mehmonlar:
#         print(f"{ism} ismli mehmon mavjud.")
#         return False
#
#     if (xona_raqami, xona_turi) in band_xonalar:
#         print(f"{xona_raqami}-xona ({xona_turi}) band.")
#         return False
#
#     mehmonlar[ism] = (xona_raqami, xona_turi)
#
#     band_xonalar.add((xona_raqami, xona_turi))
#
#     print(f"{ism} mehmon ro'yxatga qo'shildi.")
#
#     return True
#
#
# def mehmonlar_royxati():
#     print("\nMehmonlar ro'yxati")
#
#     if not mehmonlar:
#         print("Hozircha mehmonlarimiz yo'q")
#         return False
#
#     print(f"{'Ismi':<20}{'Xona raqami':<15}{'Xona turi':<15}")
#     print("-" * 50)
#
#     for ism, (xona_raqami, xona_turi) in mehmonlar.items():
#         print(f"{ism:<20}{xona_raqami:<15}{xona_turi:<15}")
#
#     return True
#
#
# def royxat_ochirish(ism):
#
#     if ism not in mehmonlar:
#         print(f"{ism} ismli mehmon mavjud emas.")
#         return False
#
#     xona_raqami, xona_turi = mehmonlar.pop(ism)
#
#     band_xonalar.remove((xona_raqami, xona_turi))
#
#     print(f"{ism} ismli mehmon ro'yxatdan o'chirildi.")
#
#     return True
#
#
# def main():
#
#     while True:
#
#         print("\n===== Samarqand Mehmonxonasi =====")
#         print("1. Mehmon qo'shish")
#         print("2. Mehmonlar ro'yxatini ko'rish")
#         print("3. Mehmonni ro'yxatdan o'chirish")
#         print("4. Dasturdan chiqish")
#
#         try:
#             tanlov = int(input("Tanlovingiz (1-4): "))
#         except ValueError:
#             print("Faqat son kiriting!")
#             continue
#
#         if tanlov == 1:
#
#             ism = input("Mehmon ismini kiriting: ").strip().capitalize()
#
#             if not ism:
#                 print("Ism bo'sh bo'lmasligi kerak.")
#                 continue
#
#             try:
#                 xona_raqami = int(input("Xona raqamini kiriting: "))
#             except ValueError:
#                 print("Xona raqami son bo'lishi kerak.")
#                 continue
#
#             if xona_raqami <= 0:
#                 print("Xona raqami 0 dan katta bo'lishi kerak.")
#                 continue
#
#             xona_turi = input(
#                 "Xona turini tanlang (Ekonom, Standart, Lux): "
#             ).strip().capitalize()
#
#             if xona_turi not in XONA_TURLARI:
#                 print(
#                     f"Noto'g'ri xona turi! Quyidagilardan birini tanlang: {', '.join(XONA_TURLARI)}"
#                 )
#                 continue
#
#             mehmon_qoshish(ism, xona_raqami, xona_turi)
#
#         elif tanlov == 2:
#
#             mehmonlar_royxati()
#
#         elif tanlov == 3:
#
#             ism = input(
#                 "Ro'yxatdan chiqariladigan mehmon ismini kiriting: "
#             ).strip().capitalize()
#
#             if ism:
#                 royxat_ochirish(ism)
#             else:
#                 print("Ismni kiriting.")
#
#         elif tanlov == 4:
#
#             print("Dasturdan chiqyapsiz...")
#             break
#
#         else:
#
#             print("Noto'g'ri tanlov! Faqat 1-4 oralig'idagi sonni kiriting.")
#
#
# if __name__ == "__main__":
#     main()

# OOP uslubidagi toʻliq kod yozib kordim

# import json
# import os
#
#
# class Mehmon:
#     def __init__(self, ism):
#         self.ism = ism
#
#     def __str__(self):
#         return self.ism
#
#
# class Xona:
#     def __init__(self, raqam, turi):
#         self.raqam = raqam
#         self.turi = turi
#         self.band = False
#
#     def band_qilish(self):
#         self.band = True
#
#     def boshatish(self):
#         self.band = False
#
#     def __str__(self):
#         return f"{self.raqam} ({self.turi})"
#
#
# class Mehmonxona:
#
#     XONA_TURLARI = {"Ekonom", "Standart", "Lux"}
#
#     def __init__(self, nom, fayl_nomi="mehmonxona_baza.json"):
#         self.nom = nom
#         self.fayl_nomi = fayl_nomi
#         self.xonalar = {}
#         self.bandlovlar = {}
#
#     def xona_qoshish(self, raqam, turi):
#
#         if turi not in self.XONA_TURLARI:
#             print("Noto'g'ri xona turi.")
#             return False
#
#         if raqam in self.xonalar:
#             print("Bu xona allaqachon mavjud.")
#             return False
#
#         self.xonalar[raqam] = Xona(raqam, turi)
#         return True
#
#     def mehmon_joylashtirish(self, ism, xona_raqami):
#
#         yangi_mehmon = Mehmon(ism)
#
#         for mehmon in self.bandlovlar:
#             if mehmon.ism == yangi_mehmon.ism:
#                 print(f"{ism} ismli mehmon allaqachon mavjud.")
#                 return False
#
#         if xona_raqami not in self.xonalar:
#             print("Bunday xona mavjud emas.")
#             return False
#
#         xona = self.xonalar[xona_raqami]
#
#         if xona.band:
#             print("Bu xona band.")
#             return False
#
#         xona.band_qilish()
#         self.bandlovlar[yangi_mehmon] = xona
#
#         print(f"{ism} {xona.raqam}-xonaga muvaffaqiyatli joylashtirildi.")
#
#         self.faylga_saqlash()
#
#         return True
#
#     def mehmonlar_royxati(self):
#
#         print("\n========== Mehmonlar ==========")
#
#         if not self.bandlovlar:
#             print("Hozircha mehmonlar yo'q.")
#             return
#
#         print(f"{'Ismi':<20}{'Xona':<10}{'Turi':<15}")
#         print("-" * 45)
#
#         for mehmon, xona in self.bandlovlar.items():
#             print(f"{mehmon.ism:<20}{xona.raqam:<10}{xona.turi:<15}")
#
#     def mehmonni_chiqarish(self, ism):
#
#         topilgan = None
#
#         for mehmon in self.bandlovlar:
#             if mehmon.ism == ism:
#                 topilgan = mehmon
#                 break
#
#         if topilgan is None:
#             print("Mehmon topilmadi.")
#             return False
#
#         xona = self.bandlovlar.pop(topilgan)
#
#         xona.boshatish()
#
#         print(f"{ism} ro'yxatdan chiqarildi.")
#
#         self.faylga_saqlash()
#
#         return True
#
#     def faylga_saqlash(self):
#
#         baza = {}
#
#         for mehmon, xona in self.bandlovlar.items():
#             baza[mehmon.ism] = {
#                 "xona": xona.raqam,
#                 "turi": xona.turi
#             }
#
#         with open(self.fayl_nomi, "w", encoding="utf-8") as f:
#             json.dump(
#                 baza,
#                 f,
#                 indent=4,
#                 ensure_ascii=False
#             )
#
#     def fayldan_yuklash(self):
#
#         if not os.path.exists(self.fayl_nomi):
#             return
#
#         with open(self.fayl_nomi, "r", encoding="utf-8") as f:
#
#             baza = json.load(f)
#
#             for ism, info in baza.items():
#
#                 xona_raqami = info["xona"]
#
#                 if xona_raqami in self.xonalar:
#
#                     mehmon = Mehmon(ism)
#
#                     xona = self.xonalar[xona_raqami]
#
#                     xona.band_qilish()
#
#                     self.bandlovlar[mehmon] = xona
#
#
# def main():
#
#     hotel = Mehmonxona("Samarqand Mehmonxonasi")
#
#     for i in range(101, 121):
#         hotel.xona_qoshish(i, "Ekonom")
#
#     for i in range(201, 211):
#         hotel.xona_qoshish(i, "Standart")
#
#     for i in range(301, 306):
#         hotel.xona_qoshish(i, "Lux")
#
#     hotel.fayldan_yuklash()
#
#     while True:
#
#         print("\n========== MENU ==========")
#         print("1. Mehmon qo'shish")
#         print("2. Mehmonlar ro'yxati")
#         print("3. Mehmonni chiqarish")
#         print("4. Chiqish")
#
#         try:
#             tanlov = int(input("Tanlang: "))
#         except ValueError:
#             print("Faqat son kiriting.")
#             continue
#
#         if tanlov == 1:
#
#             ism = input("Mehmon ismi: ").strip().capitalize()
#
#             if not ism:
#                 print("Ism bo'sh bo'lmasligi kerak.")
#                 continue
#
#             try:
#                 xona = int(input("Xona raqami: "))
#             except ValueError:
#                 print("Faqat son kiriting.")
#                 continue
#
#             hotel.mehmon_joylashtirish(ism, xona)
#
#         elif tanlov == 2:
#
#             hotel.mehmonlar_royxati()
#
#         elif tanlov == 3:
#
#             ism = input("Mehmon ismi: ").strip().capitalize()
#
#             hotel.mehmonni_chiqarish(ism)
#
#         elif tanlov == 4:
#
#             print("Dastur tugadi.")
#             break
#
#         else:
#             print("Noto'g'ri tanlov.")
#
#
# if __name__ == "__main__":
#     main()


# Mustaqil ish

# from datetime import datetime, timedelta
#
#
# class Mehmon:
#     def __init__(self, ism, telefon, pasport, kunlar_soni, tolov_holati="To'lanmagan"):
#         self.ism = ism.strip().capitalize()
#         self.telefon = telefon.strip()
#         self.pasport = pasport.strip().upper()  # AB1234567 ko'rinishida saqlash uchun
#         self.kunlar_soni = int(kunlar_soni)
#
#         # Ro'yxatga olingan aniq vaqt
#         self.kelgan_sana = datetime.now()
#         # Chiqish sanasini kelgan vaqtga kunlarni qo'shib avtomatik hisoblaymiz
#         self.chiqish_sana = self.kelgan_sana + timedelta(days=self.kunlar_soni)
#
#         self.tolov_holati = tolov_holati  # "To'langan" yoki "To'lanmagan"
#         self.jami_to_lov = 0  # Hisoblash xona aniqlangandan keyin service.py da bajariladi
#
#     def __str__(self):
#         return f"{self.ism} ({self.pasport})"
#
#
# class Xona:
#     # Xona turlari bo'yicha narxlar jadvali
#     NARXLAR = {
#         "Ekonom": 150000,
#         "Standart": 300000,
#         "Lux": 600000
#     }
#
#     def __init__(self, raqam, turi):
#         self.raqam = int(raqam)
#         self.turi = turi if turi in self.NARXLAR else "Standart"
#         self.kunlik_narx = self.NARXLAR[self.turi]
#         self.band = False
#
#     def band_qilish(self):
#         self.band = True
#
#     def boshatish(self):
#         self.band = False
#
#     def __str__(self):
#         return f"{self.raqam}-xona ({self.turi}) - {self.kunlik_narx} so'm/kun"
#
#
# class Mehmonxona:
#     def __init__(self, nom):
#         self.nom = nom
#         self.xonalar = {}  # {xona_raqami: Xona obyekti}
#
#         # Siz taklif qilgan professional struktura:
#         # { pasport: {"mehmon": Mehmon obyekti, "xona": Xona obyekti} }
#         self.bandlovlar = {}
#
#         # Biznes moliya ko'rsatkichlari
#         self.umumiy_daromad = 0

