# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kopaytma(*sonlar):
    """Kiritilgan sonlar kopaytmasini hisoblaydigan funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma
print(kopaytma(5,6))




# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin
def talaba(ismi,familiyasi,**malumotlar):
    malumotlar['ism']=ismi.title()
    malumotlar['familiya']=familiyasi.title()
    return malumotlar
print(talaba('temurbek','urolboyev',tyil=2006))

