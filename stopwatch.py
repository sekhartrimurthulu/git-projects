import time
my_time= int(input("enter the time in seconds:"))

for x in range(my_time,0,-1):
    seconds= x % 60
    minutes= x // 6
    hours= x // 3600
    print(f"00:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("time is up!")