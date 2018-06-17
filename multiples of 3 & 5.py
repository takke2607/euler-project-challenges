list3 = []
list5 = []
for i in range(1,1000):
    if i % 3 == 0:
        list3.append(i)
    elif i % 5 == 0:
        list5.append(i)
    else:
        continue

final_answer = sum(list3) + sum(list5)
print "final answer:%d"%(final_answer)
print list3
print list5

