grades={'ram':20,'shyam':30,'hari':80}

# print(type(grades))
# print(len(grades))
# print('ram'in grades)
# grades.clear()
# print(grades)

# print(grades.keys())
# print(grades.values())
# print(grades.items())
# print(grades)

# grades={'ram':20,'shyam':30,'hari':80}
# print(grades.items())
# a = [('ram', 20), ('shyam', 30), ('hari', 80)]
# print(a[0][1])
# print(a[2][1]) 


# nested dictionaries

info={
    'name': 'ram',
    'address':{'city':'sifal','district':'ktm'}
}
print(info['name'])
print(info['address']['city'])
print(info['address']['district'])
info['address']['district']='lalitpur'
