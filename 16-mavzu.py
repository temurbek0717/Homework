# 1-misol
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def yosh_hisobla(ismizni_kiriting, tugilgan_yil, joriy_yil=2024):
    print(f"Siz {ismizni_kiriting.title()} {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla()




# 2-misol
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing
def kvadrat_kubini_hisobla(son_kiriting):
    print(f"{son_kiriting**2},{son_kiriting**3} ")
kvadrat_kubini_hisobla()



# 3-misol
# # Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def son_kiriting(son):
    if son%2:
        print(f"{son} toq")
    else:
        print(f"{son} juft")
son_kiriting()





# 4-misol
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def kattasini_top(a,b):
    if a>b:
        print(f"{a}")
    elif a<b:
        print(f"{b}")
    else:
        print(f"sonlar teng")
kattasini_top()




# 5-misol
#Foydalanuvchidan x va y sonlarini olib, x ning  y inchi darajasini konsolga chiqaruvchi funksiya yozing.
def daraja_hisobla(x,y=5):
    print(f"{x**y}")
daraja_hisobla()


# 6-misol
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsilga chiqaring
def qoldiqsiz_b_t(son):
    for a in range(2,11):
        if not son%a:
            print(f"{son} {a} ga bolinadi")
qoldiqsiz_b_t()