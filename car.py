user = input("Enter command: ")
a="help"
b="start"
c="stop"
d="quit"
if user==a:
    print("start - car is started")
    print("stop - car stoped")
    print("quit - to exit")
    enter=input("Enter: ")
    if enter==b:
        print("car is started")
    elif enter==c:
        print("car is stoped")
    else:
        print("to  exit")
        