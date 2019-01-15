import json
from collections import OrderedDict

group_data = OrderedDict()

group_data = {"mellon": '24/08/1996',"Minwook": '09/04/1994',"watermellon": '12/12/1993',"lemon": '13/09/1992',
       "mango": '11/05/1982',"pear": '28/11/2003',"coconut": '30/12/2000',"passionfuit": '16/10/1994',
       "strawberry": '05/12/1992',"grape": '10/02/1998',"blackberry": '12/03/2001',"mandarin": '12/0/1998',
       "cranberry": '09/09/1999',"apple": '09/04/2009',"cherry": '21/08/1829',"pineapple": '05/12/1993',
       "blueberry": '19/07/1299',"rasberry": '18/07/1993',"orange": '29/06/1992',"banana": '04/05/1992'}
with open('problem2.json','w') as make_file:
    json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
with open('problem2.json') as data_file:
    data = json.load(data_file)

print('Welcome to Birth.Dictionary')
while True:
    print('------------------')
    print('Press the number that you want to do')
    print('1. Search birth by name')
    print('2. Add name & birth')
    select = int(input('What work do you want to?:'))
    if select  == 1:
       searchname = input("Enter your friend's name: ")
       if searchname in data:
          print(data[searchname])
          print("Do you want to continue?")
          cont = input("yes or no: ")
          if cont == 'yes':
              continue
          else:
              print("Thank you")
              break
       else :
           print("No data")
           print("Do you want to add data?")
           add = input("yes or no?: ")
           if add == 'yes' :
               print("Enter his/her birthday by dd/mm/yyyy")
               new_birth = input()
               data[searchname]=new_birth
               with open('problem2.json', 'w') as make_file:
                   json.dump(data, make_file, ensure_ascii=False, indent="\t")
               print("finish!")
               print("Do you want to continue?")
               cont = input("yes or no: ")
               if cont =='yes' :
                   continue
               else :
                   print("Thank you")
                   break
           else :
               print("Thank you")
               break
    elif select == 2:
        print("Enter your friend's name")
        new_name = input()
        if new_name in data:
            print("Already exist")
            print('------------------')
            continue
        else :
         print("Enter his/her birthday by dd/mm/yyyy")
         new_birth = input()
         data[new_name] = new_birth
         with open('problem2.json', 'w') as make_file:
             json.dump(data, make_file, ensure_ascii=False, indent="\t")
         print("finish!")
         print("Do you want to continue?")
         cont = input("yes or no: ")
         if cont == 'yes':
            continue
         else:
            print("Thank you")
            break
    else :
        print("Wrong number")
        continue
    print('------------------')
