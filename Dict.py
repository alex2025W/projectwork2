person = {} # с помощью фигурных скобок можно создать словарь

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}

# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person)
# {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}

d = {'day' : 22, 'month' : 6, 'year' : 2015}

print("||".join(d.keys()))