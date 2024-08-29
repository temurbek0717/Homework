import  json

with open('students.json','r') as f:
    students = json.load(f)


for student in students["student"]:
    ism=student["name"]
    familiya=student["lastname"]
    kurs=student["year"]
    fakultet=student["faculty"]
    print(f"Ismi:{ism} {familiya}, kurus:{kurs}, {fakultet} talabasi")