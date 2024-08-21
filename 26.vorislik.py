# 1-misol
class Talaba:
    def __init__(self,ism,familiya):
        self.ism=ism
        self.familiya=familiya
        self.fanlar=[]

    def fanga_yozil(self,fan):
        self.fanlar.append(fan)


    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print("Siz bu fanga yozilmagansiz.")

    def fanlarni_korsat(self):
        return self.fanlar


class Fan:
    def __init__(self,fan):
        self.nomi=fan


fan1=Fan("Matematika")
fan2=Fan("Fizika")
fan3=Fan("Tarix")

student=Talaba("Ali","eshmatov")

student.fanga_yozil(fan1)
student.fanga_yozil(fan2)
student.fanga_yozil(fan3)

print(student.fanlarni_korsat())
student.remove_fan("ona tili")
print(student.fanlarni_korsat())



# 2-misol

class Shaxs:
    def __init__(self, ism, yosh):
        self.ism=ism
        self.yosh=yosh

    def get_info(self):
        return f"Ism:{self.ism}, Yosh: {self.yosh}"



class Professor(Shaxs):
    def __init__(self, ism, yosh, fakultet):
        super().__init__(ism, yosh)
        self.fakultet = fakultet

    def get_info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Fakultet: {self.fakultet}"
professor=Professor("Temurbek","18","Matematika")
print(professor.get_info())
print()


class Foydalanuvchi(Shaxs):
    def __init__(self,ism,yosh,email):
        super().__init__(ism,yosh)
        self.email=email
    def get_info(self):
        return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email}"
foydalanuvchi=Foydalanuvchi("hasan","13","hasan21@gmail.com")
print(foydalanuvchi.get_info())
print()



class Admin(Foydalanuvchi):
    def __init__(self,ism,yosh,email,admin):
        super().__init__(ism,yosh,email)
        self.admin=admin

    def get_info(self):
        return f"Ismi:{self.ism},Yosh:{self.yosh},Email:{self.email},Admin:{self.admin}"

    def ban_user(self):
        print("Foydalanuvchi bloklandi")
admin=Admin("husan","32","husan11@gmail.com","admin")
print(admin.get_info())

admin.ban_user()







