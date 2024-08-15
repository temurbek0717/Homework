# 1-masala: Sonlarni ko'paytirish
# Vazifa: Berilgan sonlar ro'yxatidagi barcha sonlarni o'zaro ko'paytirib,
# yakuniy natijani qaytaruvchi funksiyani lambda yordamida yozing.
a=[12,2,36,25,22]
b=[1,10,0,27,99]
kopaytr=list(map(lambda a,b:a*b,a,b))
print(kopaytr)


# 2-masala: So'zlar uzunligini aniqlash
# Vazifa: Berilgan so'zlar ro'yxatidagi har bir so'zning uzunligini aniqlab,
# (so'z, uzunlik) shaklidagi tuplamlar ro'yxatini hosil qiling
mevalar=['olma','anjir','shaftoli','behi','qovun']
suz_uzunlik=list(map(lambda meva:len(meva),mevalar))
print(suz_uzunlik)




# 3-masala: Musbat sonlarni ajratib olish
# Vazifa: Berilgan sonlar ro'yxatidan faqat musbat sonlarni ajratib oluvchi lambda funksiyasini yozing.
sonlar=[1,-9,6,-15,-99,8,24]
m_son=list(filter(lambda sonlar:sonlar>=0,sonlar))
print(m_son)
