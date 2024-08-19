class Avto:
    def __init__(self,model,rang,narh,karopka,km=0):
        self.model=model
        self.rang=rang
        self.narh=narh
        self.karopka=karopka
        self.km=km
    def get_info(self):
        return (f"Model:{self.model} "
                f"Rang:{self.rang} "
                f"Narh:{self.narh} "
                f"Karopka:{self.karopka} "
                f"Km:{self.km}")

    def update_km(self, yangi_km):
        self.km=yangi_km

avto=Avto("matiz","qora","3000$","mexanik")
print(avto.get_info())

avto.update_km(1500)
print(avto.get_info())






class Yangi_Avtosalon:
    def __init__(self,nomi,manzil):
        self.sotuvdagi_avtolar=[]
        self.nomi=nomi
        self.manzil=manzil

    def add_avto(self, yangi_avto):
        self.sotuvdagi_avtolar.append(yangi_avto)
        # return self.sotuvdagi_avtolar

    def get_name(self):
        return (f"salon nomi:{self.nomi}")

    def get_address(self):
        return (f"Manzil:{self.manzil} ")

avto=Yangi_Avtosalon("Temur_avto_saloni","Urganch")
print(avto.get_address(),avto.get_name())

avto.add_avto("MALIBU")
avto.add_avto("BMW M5")
avto.add_avto("NISSAN GTR")
avto.add_avto("SUPRA")
print(avto.sotuvdagi_avtolar)


