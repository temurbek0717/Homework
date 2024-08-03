# #
# # Python izohli lug'atnini yarating va luga'tga kamida 10 so'z qoshing.lugatdagi bir kalit va quiymatni for tsikli yordamida,alifbo ketma-ketligida chiroyli qilib konsilga chiqaring
# P_lugat={
#     'Boolean':'Mantiqiy qiymat',
#     'Float':"O'nlik son",
#     'For':'Biror bir amalni qayta-qayta bajarish tsikili',
#     'If':'Sharlarni tekshirish operatori',
#     'Integer':'Butun son'
#     }
# for key, value in sorted(P_lugat.items()):
#     print(f"{key} - {value}")




# davlatlar={
#     'AQSH':'Washengton',
#     'ITALIYA':'Rim',
#     'MALAYZIYA':'Kuala-limpur',
#     'OZBEKISTON':'Toshkent',
#     'QIRGIZISTON':'Nursulton',
#     'QOZOGISTON':'Bishkek',
#     'ROSSIYA':'Moskva',
#     'SINGAPUR':'Dushanbe',
#     'TOJIKISTON':'Sungapur'
#
#     }
# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.upper())
#
# print('Davlatlar poytaxti:')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


# davlat=input('Qaysi davlatning poytaxtini bilishni istaysiz?')
# poytaxt = davlatlar.get(davlat)
# if poytaxt==None:
#     print("Kechirasiz, bizda bu haqida malumot yo'q")
# else:
#     print(f"{davlat.upper()}ning poytaxti {poytaxt.title()} shahri")




# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }
# for ism, info in hamkasblar.items():
#     print(f"{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. "
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
#
# # 1-misol
alomalar={
    'abu':{'familiya':'ismoliy',
           'tyil':810,
           'y_manzil':'buxora',
           'umr':60,
           'asarlar':['Al-jome as-sahih','Al-adab al-mufrad',"At-tarix as-sag'ir"]
           },
    'abdulla':{'familiya':'qodriy',
               'tyil':1894,
               'y_manzili':'toshkent',
               'umr':44,
               'asarlar':["O'tkan kunlar",'Mehrobdan Chayon','Obit ketmon']
               },
    'erkin':{'familiya':'vohidov',
             'tyil':1936,
             'y_manzil':'forgona',
             'umr':80,
             'asarlar':['Tong nafasi',"Qo'shiqlarim sizga","O'zbegim"]
             },
    'alishr':{'familiya':'navoiy',
              'tyil':1441,
              'y_manzil':'xirotda',
              'umr':60,
              'asarlar':['Xamsa','Munojat','Mahbub Al-Qulub']
              }
}

# for ism,info in alomalar.items():
#     print(f"{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda {'y_manzil'}da tavallud topgan."
#           f"{info['umr']} yil umr korgan")



# 2-misol
# for ism, info in alomalar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}ning mashhur asarlari:")
#     for asar in info['asarlar']:
#         print(asar.upper())


# #3-misol
# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
#
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)


# #4-misol
# davlatlar={
#     "o'zbekiston":{'poytaxt':'toshkent',
#                    'hudud':448978,
#                    'aholi':33000000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya": {'poytaxt': 'moskva',
#                     'hudud': 17098246,
#                     'aholi': 144000000,
#                     'pul birligi': "rubl"
#                     },
#     "aqsh": {'poytaxt': 'vashington',
#                     'hudud': 9631418,
#                     'aholi': 327000000,
#                     'pul birligi': "dollar"
#                     },
#     "malayziya": {'poytaxt': 'kuala-lumpur',
#                     'hudud': 329750,
#                     'aholi': 25000000,
#                     'pul birligi': "rinngit"
#                     }
#     }
# for davlat,info in davlatlar.items():
#     print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}\n"
#           f"Hududi: {info['hudud']} kv.km \n"
#           f"Aholisi: {info['aholi']}\n"
#           f"Pul birligi: {info['pul birligi']}")
#
# for ism,info in alomalar.items():
#     print(f"{ism.title()} {info['familiya'].title()}ning mashgur asarlari: ")
#     for asar in info['asarlar']:
#         print(asar.uppend())
#
#  for ism, info in alomalar.items():
# #     print(f"\n{ism.title()} {info['familiya'].title()}ning mashhur asarlari:")
# #     for asar in info['asarlar']:
# #         print(asar.upper())
