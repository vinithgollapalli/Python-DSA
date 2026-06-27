lis=[5,3,8,2,4]
for i in range(len(lis)):
    min_index=i
    for j in range(i+1,len(lis)):
        if lis[j] < lis[min_index]:
            min_index = j
    lis[i],lis[min_index] = lis[min_index],lis[i]
print(lis)