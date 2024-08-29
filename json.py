import json

data ={"Model":"Malibu","Model":"Qora","yil":"2020","Narh":"40000"}
data_json=json.dumps(data)
print(type(data))

talaba_json={"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba=json.loads(talaba_json)
print(f"{talaba['ism']} {talaba['familiya']}")


with open("data.json", "w") as f:
    json.dump(data,f)

with open("talaba.json", "w") as f:
    json.dump(talaba,f)