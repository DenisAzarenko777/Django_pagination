import csv

def function_csv2():
    content = list()
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['Name'],row['Street'],row['District'])
            content2 = list()
            content2.append(row['Name'])
            content2.append(row['Street'])
            content2.append(row['District'])
            content.append(content2)

    return content

content = function_csv2()

def function_csv():
    cont = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content = {}
            content['Name'] = row['Name']
            content['Street'] = row['Street']
            content['District'] = row['District']
            cont.append(content)
    return cont

content = function_csv()
