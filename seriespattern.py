current=1
stop=1
for i in range(1,5):
    for column in range(1,i+1):
        print(current,end='')
        current=current+1
    print()
    stop=stop+1
