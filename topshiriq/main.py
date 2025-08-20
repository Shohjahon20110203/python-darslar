# """1-topshiriq"""
# # Foydalanuvchi oy raqamini kiritadi (1 dan 12 gacha). Siz esa unga oy nomini chiqarasiz.
# oylar = {
#     1: "Yanvar",
#     2: "Fevral",
#     3: "Mart",
#     4: "Aprel",
#     5: "May",
#     6: "Iyun",
#     7: "Iyul",
#     8: "Avgust",
#     9: "Sentabr",
#     10: "Oktabr",
#     11: "Noyabr",
#     12: "Dekabr"
# }





























# """"2-topshiriq"""
# # Foydalanuvchi valyutani tanlaydi (USD, EUR, RUB) va miqdor kiritadi. Siz unga so‘mga aylantirib berasiz.
# kurslar = {
#     "usd": 12600,
#     "eur": 13700,
#     "rub": 140
# }


























# """3-topshiriq"""
# # Foydalanuvchi “w”, “a”, “s”, “d” tugmalaridan birini kiritsa, harfi qaysi yo‘nalishni anglatishini chiqaring 
# # (W - yuqoriga, A - chapga, S - pastga, D - o‘ngga)

# harakatlar = {
#     "w": "Yuqoriga harakat",
#     "a": "Chapga harakat",
#     "s": "Pastga harakat",
#     "d": "O‘ngga harakat"
# }






































# # Javoblar
# """1-topshiriq"""
# oylar = {
#     1: "Yanvar",
#     2: "Fevral",
#     3: "Mart",
#     4: "Aprel",
#     5: "May",
#     6: "Iyun",
#     7: "Iyul",
#     8: "Avgust",
#     9: "Sentabr",
#     10: "Oktabr",
#     11: "Noyabr",
#     12: "Dekabr"
# }

# oy_nomi = int(input("Oy raqamini kiriting (1-12): "))
# if oy_nomi in oylar:
#     print(f"{oy_nomi} - {oylar[oy_nomi]}")
# else:
#     print("Noto'g'ri oy raqami kiritildi. Iltimos, 1 dan 12 gacha bo'lgan raqam kiriting.")


























# """2-topshiriq"""
# kurslar = {
#     "usd": 12600,
#     "eur": 13700,
#     "rub": 140
# }
# valyuta = input("Valyutani tanlang(USD, EUR, RUB): ").lower()
# miqdor = float(input("Miqdorni kiriting: "))

# if valyuta in kurslar:
#     so‘m = miqdor * kurslar[valyuta]
#     print(f"{miqdor} {valyuta.upper()} = {so‘m} so‘m")
# else:
#     print("Bunday valyuta mavjud emas.")













# """3-topshiriq"""
# harakatlar = {
#     "w": "Yuqoriga harakat",
#     "a": "Chapga harakat",
#     "s": "Pastga harakat",
#     "d": "O‘ngga harakat"
# }

# harf = input("Yo‘nalishni belgilang (w/a/s/d): ").lower()

# if harf in harakatlar:
#     print(harakatlar[harf])
# else:
#     print("Noto‘g‘ri tugma!")
