# ismlar = []

# print("Do`stlaringiz ro`yhatini tuzamiz")
# n = 0
# while True:
#     ism = input(f"{n+1}-do`stingizni ismi: ")
#     ismlar.append(ism)
#     savol = input("Yana kiritasizmi? (ha/yo`q): ").lower()
#     if savol == "yo'q" or savol == 'yo`q':
#             print("Siz kiritgan do`stlaringiz ismi")
#             for dost in ismlar:
#                 print(dost.title())
#             break
#     elif savol == 'ha':
#         n += 1
#     else:
#         print("Iltimos tog`ri kiriting!")
#         break















# # Mashinalar ro'yxati, unda bir nechta "spark" bor
# mashinalar = ["spark", "malibu", "onix", "spark", "nexia 3", "gentra", "spark"]

# # "spark" ro'yxatda bor ekan, sikl davom etadi
# while "spark" in mevalar:
#     mashinalar.remove("spark")  # ro'yxatdan birinchi uchragan "olma" ni o'chiradi

# # Natijaviy ro'yxatni chiqaramiz
# print("Natijaviy ro'yxat:", mevalar)





















# # Talabalar ro'yxati
# talabalar = ["Ali", "Vali", "Diyor", "Laylo", 'Zarina', "Olim", "Gulnora"]

# # Har bir talabaning bahosini saqlash uchun bo'sh lug'at
# baholar = {}

# # 0-dan boshlab barcha talabalarni ko'rib chiqamiz
# i = 0
# while i < len(talabalar):  # i indeks ro'yxat uzunligidan kichik ekan
#     ism = talabalar[i]  # joriy talabaning ismi
#     baho = input(f"{ism}ning bahosi: ")  # foydalanuvchidan baho so'raymiz
#     baholar[ism] = baho  # ismga mos bahoni lug'atga qo'shamiz
#     i += 1  # navbatdagi talabaga o'tamiz

# # Natijada barcha baholarni chiqaramiz
# print("Talabani baholar ro'yxati:")
# for ism in talabalar:
#     print(f"{ism} - {baholar[ism]}")  # ism va uning bahosi