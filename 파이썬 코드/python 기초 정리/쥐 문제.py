# 쌀 100통 = 100kg = 100000g
# 하루에 -40g
# g = 100000 - 40 - 
# mouse = 2*m
# rice = int(input("몇g? "))

# for i in range(1,n+1):
    
rice = 100 * 1000
mouse = 2
day = 1

while True:
    rice -= 20 * mouse
    if day % 10 == 0:
        mouse *= 2
    if rice < 0:
        break
    day += 1
print("{}일 {}마리".format(day,mouse))



rice = 100 * 1000
mouse = 2
day = 1

while True:
    rice -= 20 * mouse
    if day % 10 == 0:
        mouse *= 2
    if rice < 0:
        break
    day += 1
print("{}일 {}마리".format(day,mouse))
