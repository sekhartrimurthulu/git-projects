# caluculators of (+,-,//,*)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply (x,y):
    return x*y
def division(x,y):
    if y==0:
        return "cant divide by zero!"
    else:
        return x/y
    
def caliculator():
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. division")
       
while True:
    choice=input("enter your choice 1/2/3/4/:")
    if choice in ('1', '2', '3', '4'):
        try:
            num1=int(input("enter first number:"))
            num2=int(input("enter second number:"))
        
            if choice == '1':
                print(f"{num1}+{num2}={add(num1,num2)}")
            elif choice == '2':
                print(f"{num1}-{num2}={subtract(num1,num2)}")
            elif choice == '3':
                print(f"{num1}*{num2}={multiply(num1,num2)}")
            elif choice == '4':
                print(f"{num1}/{num2}={division(num1,num2)}")
        except ValueError:
            print("entrer number only")
    else:
        print("enter only 1 to")
        
    next_sum=input("do you whant next caliculation(yes/no)")
    if next_sum.lower()!="yes":
        break    