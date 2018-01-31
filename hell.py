msg = ''
flag = True
while flag:
    msg = input("input your pizza adding")
    if msg == 'quit':
        flag = False
        break
    else:
        print("we will add "+msg+" in your pizza")
        print("input quit to quit")
    