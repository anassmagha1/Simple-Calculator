1# Calculator for multiplication

x = float(input("Num1 :"))
y = float(input("Num2 :"))
z = input("sign :")



def Calculator():
    if z == "+" :
     print("x+y :",x+y)
    elif z == "*" :
     print("x*y :",x*y)
    elif z == "-" :
     print("x-y :",x-y)
    elif z == "/" :
      print("x/y :",x/y)



Calculator()
