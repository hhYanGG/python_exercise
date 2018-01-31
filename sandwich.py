sandwich_orders = ['sahabi','nahuya','loriha','shiyuki']
finished_sandwiches = []

while sandwich_orders:
    out_sandwich = sandwich_orders.pop()
    print(" out sandwich : " + out_sandwich.title())
    finished_sandwiches.append(out_sandwich)

print("\n the sandwich is out ")
for sandwich in finished_sandwiches:
    print(sandwich)


