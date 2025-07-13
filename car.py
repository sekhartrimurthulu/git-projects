command=''
started= False
while True:
    command = input(">").lower()
    if command =='start':
        if started:
            print("car already started")
        else: 
            started = True
            print("car is started..")
    elif command =='stop':
        if not started:
            print("car was already stoped")
        else:
            started=False            
            print("car is stoped..")
    elif command=='help':
        print("""\nstart - car was started\nstop - car was stoped\nquit - to exit""")
    elif command=='quit':
        print("to exit")
        break
    else:
        print("i don't understand")