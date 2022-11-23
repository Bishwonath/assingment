#question1

cp=int(input("ENTER THE COST PRICE"))
if cp>10000:
    print("tax is 15%")
elif cp>50000 and cp<=100000:
    print("tax is 10% ")  
elif cp<=50000:
      print("tax is 5%")


#question2

age1=int(input('enter age1: '))
age2=int(input('enter age2: '))
age3=int(input('enter age3: '))
if age1>age2 and age1>age3:
    print('age1 is oldest')
elif age2>age1 and age2>age3:
    print('age2 is oldest')
else:
    print('age3 is oldest')
if age1<age2 and age1<age3:
    print('age1 is youngest')
elif age2<age1 and age2<age3:
    print('age2 is youngest')
else:
     print('age3 is youngest')






##question number4

marks=int(input("enter the marks"))

if marks>90:
    print("grade A+")
elif marks>80:
    print("grade A")
elif marks>70:
    print("grade b+")

elif marks>60:
 print("grade b")

elif marks>50:
    print("grade c+")

elif marks>40:
    print("grade c")
elif marks<30:
    print("YOU FAILED!!") 


    #question number 5
    