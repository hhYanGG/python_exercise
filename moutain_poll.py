responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    name = input("\n what is your name? ")
    response = input("Which mountain would you like to climb someday?")

    #将答案存储在字典里
    responses[name] = response

    #看看是否还有人参与调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active =False

print("\n--- poll results ---")

for name,response in responses.items():
    print(name + " would like to climb" + response + ".")
