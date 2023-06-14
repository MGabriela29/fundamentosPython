
#Dictionarios
#{"Clave":"valor"}

teacher = {
    "name":"Francsico",
    "l_name": "Lopez",
    "phone":  "2471333902",
    "groups": ["3ADSM", "3BDSM"]
}

print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3CDSM")
teacher["phone"] ="2471224293"
teacher["city"] = "Huamantla"
print(teacher)