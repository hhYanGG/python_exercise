sandwich_orders = ['pastrami','pastrami','pastrami','saaasdd','jjhfbn','pastrami']
finished_orders = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    out_sandwich =sandwich_orders.pop()
    finished_orders.append(out_sandwich)
print(" 'pastrami' has been sold out ")
print(finished_orders)

places = []    
flg = True
while flg:
    place = input("If you could visit one place in the world ")
    places.append(place)    
    if place == 'q':
        flg = False

while 'q' in places:
    places.remove('q')
   
    

print(places)
