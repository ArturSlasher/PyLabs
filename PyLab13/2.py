# 13.20
def findWithPhoneNumber(phone):
    notFound = True
    for human in phoneDict:
        if phoneDict[human]['phone'] == phone:
            notFound = False
            print("Surname:",phoneDict[human]['surname'])
            print("Name:",phoneDict[human]['name'])
            print("Address:",phoneDict[human]['address'])
    if notFound:
        print("Not found")

def findWithSurname(surname):
    notFound = True
    for human in phoneDict:
        if phoneDict[human]['surname'] == surname:
            notFound = False
            print("Phone:", phoneDict[human]['phone'])
            print("Surname:",phoneDict[human]['surname'])
            print("Name:",phoneDict[human]['name'])
            print("Address:",phoneDict[human]['address'])
    if notFound:
        print("Not found")

phoneDict = {'Azarenchyk': {'surname': "Azarenchyk", 'name': "Artur", 'fname': "Alekseevich", 'address': "Hovorova, 17", 'phone': "0994340346"},
             'Antosonov': {'surname': "Antosonov", 'name': "Maxim", 'fname': "Vitalievich", 'address': "Segedska, 28", 'phone': "-"},
             'Bairam': {'surname': "Bairam", 'name': "Israil", 'fname': "Mehmadovich", 'address': "Chernachovskoho, 22", 'phone': "0957652984"},
             'Burakova': {'surname': "Burakova", 'name': "Arina", 'fname': "Vasilievna", 'address': "Shevchenko, 10", 'phone': "0504345692"},
             'Veremov': {'surname': "Veremov", 'name': "Kiril", 'fname': "Danilovich", 'address': "-", 'phone': "0634560109"},
             'Kiosova': {'surname': "Kiosova", 'name': "Tatiana", 'fname': "Borisovna", 'address': "Haharina, 58", 'phone': "0675395692"},
             'Kolenov': {'surname': "Kolenov", 'name': "Alaeksei", 'fname': "Alekseevich", 'address': "Hovorova, 4", 'phone': "0674345692"},
             'Mirzoanov': {'surname': "Mirzoanov", 'name': "Ernest", 'fname': "Batkovich", 'address': "Dneprovska doroga, 228", 'phone': "-"},
             'Pasararov': {'surname': "Pasararov", 'name': "Andrei", 'fname': "Kirilovich", 'address': "-", 'phone': "0634345692"},
             'Slezovko': {'surname': "Slezovko", 'name': "Karina", 'fname': "Maximovna", 'address': "Franzuskii bulvar, 40", 'phone': "-"},}

currentEnter = ""
while(True):
    print("Enter:\n"
          "1 - if you want to search with phone number\n"
          "2 - if you want to search with surname")
    currentEnter = input()
    if currentEnter == '1':
        print("Enter a phone number:")
        findWithPhoneNumber(input())
    elif currentEnter == '2':
        print("Enter a surname:")
        findWithSurname(input())
    else:
        "You entered invalid value. Try again."
    print("Do you want to continue? (yes/no)")
    if input() == "yes":
        continue
    else:
        break

print("Thank you for using")