
dic = {}
dic['minwook'] = '09/04/1994'
dic['mango'] = '02/12/1932'
dic['orange']= '04/02/2000'
print('Welcome to Birth.Dictionary')
while True:
    print('------------------')
    print('Press the number that you want to do')
    print('1. Search birth by name')
    print('2. Add name & birth')
    select = int(input('What work do you want to?:'))
    if select  == 1:
       searchname = input("Enter your friend's name: ")
       if searchname in dic:
          print(dic[searchname])
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
               dic[searchname]=new_birth
               print("finish!")
               print("Do you want to continue?")
               cont = input("yes or no: ")
               if cont =='yes' :
                   continue
               else :
                   print("Thank you")
                   break
           else :
               continue
    elif select == 2:
        print("Enter your friend's name")
        new_name = input()
        if new_name in dic:
            print("Already exist")
            print('------------------')
            continue
        else :
         print("Enter his/her birthday by dd/mm/yyyy")
         new_birth = input()
         dic[new_name] = new_birth
         print("finish!")
         print("Do you want to continue?")
         cont = input("yes or no: ")
         if cont == 'yes':
            continue
         else:
            print("Thank you")
            break
    print('------------------')
