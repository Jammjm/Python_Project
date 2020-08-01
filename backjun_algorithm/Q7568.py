num = int(input())
info = []
rank = []
for nownum in range(num):
    input_info = input()
    weight = int(input_info.split(" ")[0])
    height = int(input_info.split(" ")[1])
    info.append([weight, height])

for student_idx, student_info in enumerate(info):
    weight = student_info[0]
    height = student_info[1]
    student_rank = 0
    
    for compare_info in info:
        compare_weight = compare_info[0]
        compare_height = compare_info[1]

        if weight < compare_weight:
            if height < compare_height:
                student_rank += 1

    rank.append(student_rank + 1)


print(rank) 

#https://www.acmicpc.net/problem/7568
            