
classDict = {'Azarenchyk': {'surname': "Azarenchyk", 'name': "Artur", 'fname': "Alekseevich", 'address': "Hovorova, 17", 'phone': "0994345692"},
             'Antosonov': {'surname': "Antosonov", 'name': "Maxim", 'fname': "Vitalievich", 'address': "Segedska, 28", 'phone': "-"},
             'Bairam': {'surname': "Bairam", 'name': "Israil", 'fname': "Mehmadovich", 'address': "Chernachovskoho, 22", 'phone': "0994345692"},
             'Burakova': {'surname': "Burakova", 'name': "Arina", 'fname': "Vasilievna", 'address': "Shevchenko, 10", 'phone': "0504345692"},
             'Veremov': {'surname': "Veremov", 'name': "Kiril", 'fname': "Danilovich", 'address': "Armeiska, 5", 'phone': "099-434-56-92"},
             'Kiosova': {'surname': "Kiosova", 'name': "Tatiana", 'fname': "Borisovna", 'address': "Haharina, 58", 'phone': "067-434-56-92"},
             'Kolenov': {'surname': "Kolenov", 'name': "Alaeksei", 'fname': "Alekseevich", 'address': "Hovorova, 4", 'phone': "0674345692"},
             'Mirzoanov': {'surname': "Mirzoanov", 'name': "Ernest", 'fname': "Batkovich", 'address': "Dneprovska doroga, 228", 'phone': "-"},
             'Pasararov': {'surname': "Pasararov", 'name': "Andrei", 'fname': "Kirilovich", 'address': "Lunnii, 1", 'phone': "0634345692"},
             'Slezovko': {'surname': "Slezovko", 'name': "Karina", 'fname': "Maximovna", 'address': "Franzuskii bulvar, 40", 'phone': "-"},}

print("There are students with no phone numbers")
for student in classDict:
    if classDict[student]['phone'] == '-':
        print(classDict[student]['surname'], classDict[student]['name'], classDict[student]['address'])