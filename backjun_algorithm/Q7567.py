#Q7567
#https://www.acmicpc.net/problem/7567

import sys

dish_input = input()

if len(dish_input) < 3 or len(dish_input) > 50 :
    print("ERROR")
    sys.exit()

dishes = list(dish_input)

result = 0

prev_dish = None
for idx, dish in enumerate(dishes):
    
    if idx == 0 :
        result += 10
        prev_dish = dish
    else: 
        if prev_dish == dish:
            result += 5
        else:
            result += 10
        prev_dish = dish

print(result)
    


    
