"""import json
my_dict = {
"id": 123,
"name": "Clementine Bauche",
"username": "Cleba",
"email": "cleba@corp.mail.ru",
"address": {
"street": "Central",
"city": "Metropolis",
"zipcode": "123456"
},
"phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'),
sort_keys=True)
print(res)"""

"""import json
a = 'Hello world!'
b = {key: value for key, value in enumerate(a)}
c = json.dumps(b, indent=3, separators=('; ', '= '))
print(c)"""
"""import csv
with open('quest.csv', 'w', newline='', encoding='utf-8') as f_write:
    csv_write = csv.DictWriter(f_write, fieldnames=["number",
    "name", "data"], restval='Hello world!', dialect='excel',
    delimiter='#', quotechar='=', quoting=csv.QUOTE_NONNUMERIC)
    csv_write.writeheader()
    dict_row = {}
    for i in range(10):
        dict_row['number'] = i
        dict_row['name'] = str(i)
        csv_write.writerow(dict_row)"""

#import pickle
#res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
#print(res)

import pickle
my_dict = {'numbers': [42, 4.1415, (7 + 3j)],
'functions': (sum, max),
'others': {False, True, 'Hello world!'}
}
res = pickle.dumps(my_dict)
with open('quest.pickle', 'wb') as f:
    pickle.dump(f'{res = }', f)

