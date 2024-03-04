time_list = []
score_list = []
for i in range(20):
    _, time, score = input().split()
    if score == 'A+':
        score_list.append(4.5 * float(time))
        time_list.append(float(time))
    elif score == 'A0':
        score_list.append(4.0 * float(time))
        time_list.append(float(time))
    elif score == 'B+':
        score_list.append(3.5 * float(time))
        time_list.append(float(time))
    elif score == 'B0':
        score_list.append(3.0 * float(time))
        time_list.append(float(time))
    elif score == 'C+':
        score_list.append(2.5 * float(time))
        time_list.append(float(time))
    elif score == 'C0':
        score_list.append(2.0 * float(time))
        time_list.append(float(time))
    elif score == 'D+':
        score_list.append(1.5 * float(time))
        time_list.append(float(time))
    elif score == 'D0':
        score_list.append(1.0 * float(time))
        time_list.append(float(time))
    elif score == 'F':
        score_list.append(0 * float(time))
        time_list.append(float(time))
    else:
        pass
    
print(sum(score_list) / sum(time_list))