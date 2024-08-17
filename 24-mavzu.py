1,2-misol
class Foydalanuvchi:

    def __init__(self,foydalanuvchi,ism,email):
        self.f_ismi = foydalanuvchi
        self.ism = ism
        self.email = email

    def get_info(self):
        return (f"Foydalanuvchi:{self.f_ismi}, "
                f"ismi:{self.ism}, "
                f"email:{self.email}")
foydalanuvchi=Foydalanuvchi("temurbek06","Temurbek","orolboyev00@gmail.com")
print(foydalanuvchi.get_info())




# 3-misol
class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya


    def get_fullname(self):
        return f"{self.ism} {self.familiya}"


talaba1=Talaba("Ali","aliyev","1999")
talaba2=Talaba("Vali","valiyev","2003")
talaba3=Talaba("Hasan","olimov","2000")

print(talaba3.get_name())




