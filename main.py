from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
pattern_name = re.compile(r'([a-яёА-ЯЁ]*)[ |,]([a-яёА-ЯЁ]*)[ |,|-]([a-яёА-ЯЁ]*)')
pattern_number = re.compile(r'[\+]?[7|8]?[ ]?[\(]?(\d{3})[ |\)|\-]?[ ]?(\d{3})[ |\-]?(\d{2})[ |\-]?(\d{2})[\s*]?[\(]?(доб.)?[\s*]?(\d{4})?[\)]?')

pattern_name_sub = r'\1,\2,\3'
pattern_number_sub = r'+7(\1)\2-\3-\4 \5\6'

lastname_list = []
firstname_list = []
surname_list = []
organization_list = []
position_list = []
number_list = []
email_list = []

final_list = []

for items in contacts_list:

  if len(items[0].split(' ')) == 3:
    temp_l = items[0].split(' ')
    lastname_list.append(temp_l[0])
    firstname_list.append(temp_l[1])
    surname_list.append(temp_l[2])


  elif len(items[0].split(' ')) == 2:
    lastname_list.append(items[0].split(' ')[0])
    firstname_list.append(items[0].split(' ')[1])
    surname_list.append(items[2])

  else:
    if len(items[1].split(' ')) == 2:
      lastname_list.append(items[0])
      firstname_list.append(items[1].split(' ')[0])
      surname_list.append(items[1].split(' ')[1])
    else:
      lastname_list.append(pattern_name.sub(r'\1', items[0]))
      firstname_list.append(pattern_name.sub(r'\2', items[0]))
      surname_list.append(pattern_name.sub(r'\3', items[0]))

  organization_list.append(items[3])
  position_list.append(items[4])
  number_list.append(pattern_number.sub(pattern_number_sub, items[5]))
  email_list.append(items[6])


final_list.append(['lastname','firstname','surname','organization','position','phone','email'])

i = 1
n = len(lastname_list)

while i != n:
  final_list.append([lastname_list[i], firstname_list[i], surname_list[i], organization_list[i], position_list[i], number_list[i], email_list[i]])
  i += 1


final_list.sort()

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(final_list)